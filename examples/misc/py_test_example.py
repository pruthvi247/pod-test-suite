
# import sys
# sys.path.append("../../../..")

import json
import pytest

# prop = util_functions.load_properties_from_json("/conf_test/testing_configurations.json")
#
# @pytest.mark.smoke
# def test_corr():
#     query = '''(SELECT * FROM Ds_training.dbo.Sensor_Data_ts)t'''
#
#     pys = pyscale_init.Pyscale(host=prop['TESTING']['LIVY_HOST'], spark_submit_config=json.loads(prop['TESTING']['spark_submit_config']))
#     pys.start_spark()
#
#     # commenting below lines as we have depricated "DBDetailToFetchData" function, we will be using parquet files of ahai app
#
#     # dbtype = prop['TESTING']['dbtype']
#     # url = prop['TESTING']['sql_server_url']
#     # user = prop['TESTING']['sql_server_user']
#     # password = prop['TESTING']['sql_server_password']
#     # condet = connection.DBDetailToFetchData(dbtype=dbtype, url=url, user=user, password=password)
#     condet = connection.ParquetDetailToFetchData(url=prop['TESTING']['hdfs_url'], port=prop['TESTING']['hdfs_port'],
#                                                  filepath=prop['TESTING']['parquet_file_path'],
#                                                  sel_col='*')
#     qa = stat.Correlation(condet)
#
#     qa.corr(query)
#
# @pytest.mark.regression
# def test_sample():
#     print("sample test case")

def compare_json(json1, json2,result=None):
    # json1 is expected output
    # json2 is http output

    if result is None:
        result={}
    #Compare all keys
    for key in json1.keys():
        #if key exist in json2:
        if key in json2.keys():
            # print(key)
            #If subjson
            if type(json1[key]) == dict:
                dict_keys = {}
                compare_json(json1[key], json2[key],result)
            elif type(json1[key]) == list:
                # print("list values")
                # print(len(json1[key]))
                # print(json1[key][0])
                # print(type(json1[key][0]))
                print("========")
                if type(json1[key][0]) == dict:
                    compare_json(json1[key][0], json2[key][0], result)

            else:
                if json1[key] != json2[key]:
                    # print("These entries are different:")
                    result[key] = [json1[key],json2[key]]
        else:
            print("found new key in json1 %r" % key)
    return result

if __name__ == "__main__":
    # test_corr()
    # prop = util_functions.load_properties_from_json("conf_test/testing_configurations.json")
    # print(prop)
    expected= '{ "items": [ { "id": "f48ef5d4-8434-40df-b92e-520916b30a16", "code": "abc1234", "owner": { "userId": "owner1011" }, "customer": { "userId": "cust101" }, "dateOfBooking": "2019-11-14T09:22:25.619Z", "parkingStartDate": "2019-11-13T09:21:25.619Z", "parkingEndDate": "2019-11-14T09:23:25.62Z", "parkingSpotId": "spot101", "status": "BOOKED" } ], "totalSize": 1 }'
    httpout = '{ "items": [ { "id": "f48ef5d4-8434-40df-b92e-520916b30a16", "code": "abc123", "owner": { "userId": "owner101" }, "customer": { "userId": "cust101" }, "dateOfBooking": "2019-11-14T09:22:25.619Z", "parkingStartDate": "2019-11-13T09:21:25.619Z", "parkingEndDate": "2019-11-14T09:23:25.62Z", "parkingSpotId": "spot101", "status": "BOOKED" } ], "totalSize": 1 }'
    result = compare_json(json1=json.loads(expected),json2=json.loads(httpout))
    print(result)

