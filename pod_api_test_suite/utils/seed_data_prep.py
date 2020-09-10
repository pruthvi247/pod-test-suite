import pandas as pd
import json


def read_csv(input_file):
    # ## float precision is needed because
    # ##lat lang values is getting changed when read into pd data frame
    return pd.read_csv(input_file, float_precision='round_trip').dropna(how='all', axis=1)


def write_to_csv(filepath, dict):
    # pd.DataFrame(dict).to_csv(filepath,index=False)
    pdseries = pd.Series(dict).to_frame()
    pd.DataFrame(pdseries).to_csv(filepath, header=['output'])

    return pd.read_csv(filepath)


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



def prepare_parkingSpot_data(input):
    test_id_counter = 0
    final_dict = {}

    ip_pd_df = read_csv(input)
    ip_col_list = list(ip_pd_df.columns)
    final_col_list = ["ID", "TESTCASE", "METHOD", "URL", "API_INPUT", "EXPECTED_OUTPUT", "EXPECTED_STATUS_CODE",
                      "NOTES"]

    def prep_aip_input(temp_dict, val, key):
        temp_dict.update(nested_set(temp_dict, key, val, create_missing=True))
        # print(f'temp dict : {temp_dict}')
        return temp_dict

    for index, row in ip_pd_df.iterrows():
        test_id_counter = test_id_counter + 1
        code = str(test_id_counter).zfill(4)
        lat_key = ['geoLocation', 'latitude']
        lang_key = ['geoLocation', 'longitude']
        owner_first_name_key = ['owner','firstName']
        owner_last_name_key = ['owner','lastName']
        owner_id_key = ['owner','id']


        # print(f"index: {index}, row: {row['STATION']} - lat :{row['LAT']} - lang :{row['LANG']}")

        final_dict.update(prep_aip_input(temp_dict=final_dict, val=row['LANG'], key=lang_key))
        final_dict.update(prep_aip_input(temp_dict=final_dict, val=row['LAT'], key=lat_key))
        final_dict.update(prep_aip_input(temp_dict=final_dict, val=code, key='code'))
        final_dict.update(prep_aip_input(temp_dict=final_dict, val="testing", key='description'))
        final_dict.update(prep_aip_input(temp_dict=final_dict, val='owner'+code, key=owner_id_key))
        final_dict.update(prep_aip_input(temp_dict=final_dict, val='owner'+code + '_first', key=owner_first_name_key))
        final_dict.update(prep_aip_input(temp_dict=final_dict, val='owner'+code + '_last', key=owner_last_name_key))
        break

    return final_dict


if __name__ == "__main__":
    input_file_path = '/home/avatar/Documents/pythonProjects/pod-test-suite/pod_user_service_suite/data/geoPoints_users.csv'
    output_file_path = '/home/avatar/Documents/pythonProjects/pod-test-suite/pod_user_service_suite/data/data_prep.csv'

    output_dict = prepare_parkingSpot_data(input_file_path)

    # print(output_dict)
    app_json = json.dumps(output_dict)
    print(app_json)
