import pandas as pd
import json
import requests
import math


def read_csv(input_file):
    # ## float precision is needed because
    # ##lat lang values is getting changed when read into pd data frame
    return pd.read_csv(input_file, float_precision='round_trip').dropna(how='all', axis=1)


def write_to_csv(filepath, dict):

    pd_series = pd.Series(dict).to_frame()
    pd.DataFrame(pd_series).to_csv(filepath, header=['output']) ### this works fine
    return True

def post_json(csv_file,column,endpoint,headers):

    ip_df = pd.read_csv(csv_file, float_precision='round_trip').dropna(how='all', axis=1)

    for i,r in ip_df.iterrows():

        print(json.loads(r[column])['code'])

        http_output = requests.post(endpoint, data=json.dumps(json.loads(r[column])), headers=headers)
        if http_output.status_code != 201:
            print(http_output)
        print(http_output.status_code)

    return True

def nested_set(dic, keys, value, create_missing=True):
    # ## [source: https://stackoverflow.com/questions/13687924/setting-a-value-in-a-nested-python-dictionary-given-a-list-of-indices-and-value,
    # ## reference : https://hackersandslackers.com/extract-data-from-complex-json-python/]
    d = dic
    if type(keys) == list:
        for key in keys[:-1]:
            if key in d:
                d = d[key]
            elif create_missing:
                d = d.setdefault(key, {})
            else:
                return dic
        if keys[-1] in d or create_missing:
            d[keys[-1]] = value
        return dic
    else:
        if keys in d or create_missing:
            d[keys] = value
            return dic

def isNaN(num):
    # #### this method is to check if any value is Nan, math.isnan() will not work for string datatypes
    return num != num

def prepare_parkingSpot_data(input):
    test_id_counter = 0

    final_dict = {}

    ip_pd_df = read_csv(input)

    def prep_aip_input(temp_dict, val, key):
        if isNaN(val):
            val = ""

        temp_dict.update(nested_set(temp_dict, key, val, create_missing=True))
        # print(f'temp dict : {temp_dict}')
        return temp_dict

    for index, row in ip_pd_df.iterrows():
        # print(f'>>>>>>>>>>> {row["STATION"]}')
        semifinal_dict = {}
        test_id_counter = test_id_counter + 1
        code = str(test_id_counter).zfill(4)
        ### list of nested key , these are put in json in nested structure
        lat_key = ['geoLocation', 'latitude']
        lang_key = ['geoLocation', 'longitude']
        owner_first_name_key = ['owner','firstName']
        owner_last_name_key = ['owner','lastName']
        owner_id_key = ['owner','id']
        owner_user_id_key = ['owner','userId']
        add_city_key = ['address','city']
        station_key = ['station','type']

        # print(f"index: {index}, row: {row['STATION']} - lat :{row['LAT']} - lang :{row['LANG']}")


#       #### this is the source of truth, all key values for json are present below
        semifinal_dict.update(prep_aip_input(temp_dict=semifinal_dict, val=row['LANG'], key=lang_key))
        semifinal_dict.update(prep_aip_input(temp_dict=semifinal_dict, val=row['LAT'], key=lat_key))
        semifinal_dict.update(prep_aip_input(temp_dict=semifinal_dict, val='spot'+code, key='code'))
        semifinal_dict.update(prep_aip_input(temp_dict=semifinal_dict, val="testing", key='description'))
        semifinal_dict.update(prep_aip_input(temp_dict=semifinal_dict, val='owner'+code, key=owner_id_key))
        semifinal_dict.update(prep_aip_input(temp_dict=semifinal_dict, val='owner'+code + '_first', key=owner_first_name_key))
        semifinal_dict.update(prep_aip_input(temp_dict=semifinal_dict, val='owner'+code + '_last', key=owner_last_name_key))
        semifinal_dict.update(prep_aip_input(temp_dict=semifinal_dict, val='owner'+code + '@pod.com', key=owner_user_id_key))
        semifinal_dict.update(prep_aip_input(temp_dict=semifinal_dict, val='Bengaluru', key=add_city_key))
        semifinal_dict.update(prep_aip_input(temp_dict=semifinal_dict, val='ind', key=['address','country']))
        semifinal_dict.update(prep_aip_input(temp_dict=semifinal_dict, val='Karnataka', key=['address','state']))
        semifinal_dict.update(prep_aip_input(temp_dict=semifinal_dict, val=row['ADDRESS_1'], key=['address','street']))
        semifinal_dict.update(prep_aip_input(temp_dict=semifinal_dict, val=row['ADDRESS_8'], key=['address','zipCode']))
        semifinal_dict.update(prep_aip_input(temp_dict=semifinal_dict, val=row['STATION'], key=['address','landmark']))
        semifinal_dict.update(prep_aip_input(temp_dict=semifinal_dict, val=code, key=['address','doorNo']))
        semifinal_dict.update(prep_aip_input(temp_dict=semifinal_dict, val='RESIDENCE', key=station_key))

        semifinal_dict.update(prep_aip_input(temp_dict=semifinal_dict, val=[{"fileName": "/root/file/photo.png","id":code,"ownerId":'owner'+code}], key='photos'))

        final_dict[code] = json.dumps(semifinal_dict)

    return final_dict


if __name__ == "__main__":
    # input_file_path = '/home/avatar/Documents/pythonProjects/pod-test-suite/pod_user_service_suite/data/geoPoints_users.csv'
    # output_file_path = '/home/avatar/Documents/pythonProjects/pod-test-suite/pod_user_service_suite/data/data_prep.csv'

    input_file_path = '/Users/pruthvikumar/Documents/workspace/eclipse-work-space/pod-test-suite/pod_user_service_suite/data/geoPoints_users.csv'
    output_file_path = '/Users/pruthvikumar/Documents/workspace/eclipse-work-space/pod-test-suite/pod_user_service_suite/data/data_prep_new.csv'


    #### Below step is to create a json from the raw input geo file -eoPoints_users.cs
    #### we should un comment it when we want to create a different json structure
    # output_dict = prepare_parkingSpot_data(input_file_path)
    # write_to_csv(output_file_path, output_dict)

    #### Below steps are to create parking spots in DB using parking spot API
    # end_point = 'http://192.168.0.194:8080/parkingspot'
    # end_point = 'http://192.168.0.177:8082/parkingspot'
    end_point = 'http://192.168.0.177:8080/parkingspot'
    Headers = {"Content-Type": "application/json"}

    post_json(output_file_path, 'output', end_point, Headers)
