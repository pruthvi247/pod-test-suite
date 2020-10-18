import sys,os
import subprocess
import json
import webbrowser
sys.path.insert(0, os.path.abspath(os.path.abspath('')))


import pod_api_test_suite.utils.csv_util as csv
import pod_api_test_suite.utils.pandas_util as pandasUtil
import pandas as pd
from functools import reduce
from operator import getitem



def prepare_api_input(api_input_json,dependent_json):
    print("preparing input")
    print(type(api_input_json))
    print(type(dependent_json))
    print(dependent_json["dependent_test_case_outPutPath"])

    temp_df = pd.read_csv(str(dependent_json["dependent_test_case_outPutPath"]))
    temp_df.set_index('Unnamed: 0', inplace=True)
    parent_testcase_json = temp_df.loc[str(dependent_json["dependent_test_case_id"])].to_json()
    out_json = json.loads(parent_testcase_json)['output']
    actual_parent_json = json.loads(out_json)
    *path, key = dependent_json["dependent_test_case_key"]
    print(reduce(getitem,path,actual_parent_json)[key])
    *dest_path,dest_key = dependent_json["current_test_case_key"]
    reduce(getitem, dest_path, api_input_json)[dest_key] = reduce(getitem,path,actual_parent_json)[key]
    print(api_input_json.keys())
    # print(json.loads(out_json)["id"])
   # print(json.loads(json.loads(parent_testcase_json)['output'])['id'])


    # print(parent_testcase_json[str(temp_df.loc[str(dependent_json["dependent_test_case_id"])])])
    # api_input_json["parkingSpotId"] = "custom id"

    return json.dumps(api_input_json)




pd_df = csv.csv_reader_pandas(filepath="/home/avatar/Documents/pythonProjects/a1m/pod-test-suite/pod_user_service_suite/data/booking_service_test_cases.csv")
ip_dict = pandasUtil.pandas_to_dict(pd_df)
out_columns_list = ["ID","TESTCASE","METHOD","URL","API_INPUT","DEPENDENT","EXPECTED_OUTPUT","EXPECTED_STATUS_CODE","NOTES"]

out_df = pd.DataFrame( columns = out_columns_list)
# print(out_df.columns)
# dependent_json = {}
# print(pd_df.shape)
# print(pd_df.columns)
# print(pd_df.index.values.tolist())

for index in pd_df.index.values.tolist():
    new_row = []
    print(index)
    new_row.append(index)
    new_row.append(pd_df["TESTCASE"][index])
    new_row.append(pd_df["METHOD"][index])
    new_row.append(pd_df["URL"][index])
    if str(pd_df["DEPENDENT"][index]).lower() != "no":
        new_row.append(prepare_api_input(json.loads(pd_df["API_INPUT"][index]),json.loads(pd_df["DEPENDENT"][index])))
    else:
        new_row.append(pd_df["API_INPUT"][index])

    new_row.append("No")
    new_row.append(pd_df["EXPECTED_OUTPUT"][index])
    new_row.append(pd_df["EXPECTED_STATUS_CODE"][index])
    new_row.append(pd_df["NOTES"][index])
    # out_df.append(new_row)
    out_df.loc[index]=new_row
# print(out_df.head(2))
out_df.to_csv("/home/avatar/Documents/pythonProjects/a1m/pod-test-suite/pod_user_service_suite/data/booking_service_test_cases_out.csv",index=False)










