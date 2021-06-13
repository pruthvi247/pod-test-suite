import os
import sys
import logging
import requests
import json


sys.path.insert(0, os.path.abspath(os.path.abspath('')))

from pod_user_service_suite.utils.json_utils import load_properties_from_json
# from pod_user_service_suite.utils import json_utils
from pod_user_service_suite.utils.csv_utils import csv_pandas


props = load_properties_from_json(filepath='pod_user_service_suite/config/user_service_properties.json')
logging.getLogger().setLevel(props["TEST"]["LOGGING_LEVEL"]) # setting log levels = CRITICAL = 50,FATAL = CRITICAL,ERROR = 40,WARNING = 30,WARN = WARNING,INFO = 20,DEBUG = 10,NOTSET = 0
logger = logging.getLogger(__name__)
logger.info("info logs")


pd_input = csv_pandas(props["TEST"]["IP_TEST_DOC_FILEPATH"])
# headers = {'Content-Type': 'application/json'}

# headers = {'Content-Type': 'application/json'}
# headers = json.loads(props["TEST"]["HEADERS"])
# headers = json.loads(json.dumps(props["TEST"]["HEADERS"]))
# headers = props["TEST"]["HEADERS"]

# headers = eval(props["TEST"]["HEADERS"])
# headers = json.dumps(props["TEST"]["HEADERS"])
input_header = props["TEST"]["HEADERS"]
print("=====>>> input_header {}".format(type(input_header)))
headers = json.loads(input_header)
print("=====>>> headers {}".format(type(headers)))



def json_compare(json1, json2):
    #Compare all keys
    for key in json1.keys():
        #if key exist in json2:
        if key in json2.keys():
            #If subjson
            if type(json1[key]) == dict:
                json_compare(json1[key], json2[key])
            else:
                if json1[key] != json2[key]:
                    print("These entries are different:")
                    print(json1[key])
                    print(json2[key])
        else:
            print("found new key in json1 %r" % key)
    return True

def temp_test():
    # print(type(pd_input))
    # print(pd_input.shape)
    # print(pd_input.columns)
    # print(pd_input.shape[0])
    # print(pd_input["METHOD"]=="POST")
    # print(pd_input.loc[pd_input['METHOD'] == 'POST', 'ID'])

    # for index, row in pd_input.iterrows():
    #     print(row['ID'], row['METHOD'],row['API_INPUT'])
    print(pd_input.iloc[0,4])
    pass

def invoke_post_call():
    url='http://localhost:8082/user'
    input_json=pd_input.iloc[0,4]
    input_payload = json.loads(input_json)
    # http_output=requests.post(url, data=json.dumps(input_payload), headers=headers)
    # print(http_output)
    print("=======>>>>> {}".format(type(input_payload)))
    print("=======>>>>> {}".format(type(input_json)))


def invoke_get_call():
    url='http://localhost:8082/user/number/9916893441'
    # input_json=pd_input.iloc[0,4]
    # input_payload = json.loads(input_json)
    http_output=requests.get(url, headers=headers)
    # http_output=requests.get(url, headers=json.dumps(headers))
    print(http_output.json())

def validate_json(input_json):
    expected_json = json.loads(pd_input.iloc[0, 5])

    json_compare(input_json,expected_json)

    pass

# temp_test()
# invoke_post_call()
# invoke_get_call()

# validate_json(json.loads(pd_input.iloc[0, 4]))


# logger.info(pd_input.iloc[0])
# input = pd_input.iloc[0]
# def first_test(input):
#     logger.info(pd_input.iloc[0])
#
# first_test(input)
print("DONE !!!")

