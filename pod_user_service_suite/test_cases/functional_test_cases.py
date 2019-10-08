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
headers = {'Content-Type': 'application/json'}

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
    http_output=requests.post(url, data=json.dumps(input_payload), headers=headers)
    print(http_output)


# temp_test()
invoke_post_call()



# logger.info(pd_input.iloc[0])
# input = pd_input.iloc[0]
# def first_test(input):
#     logger.info(pd_input.iloc[0])
#
# first_test(input)
print("DONE !!!")