import os
import sys
import logging
import requests
import json


sys.path.insert(0, os.path.abspath(os.path.abspath('')))

from pod_user_service_suite.utils.json_utils import load_properties_from_json
# from pod_user_service_suite.utils import json_utils
from pod_user_service_suite.utils.csv_utils import csv_pandas
from pod_user_service_suite.commons.http_invocations import invoke_post_call
from pod_user_service_suite.commons.validations import json_validation

props = load_properties_from_json(filepath='pod_user_service_suite/config/user_service_properties.json')
logging.getLogger().setLevel(props["TEST"]["LOGGING_LEVEL"]) # setting log levels = CRITICAL = 50,FATAL = CRITICAL,ERROR = 40,WARNING = 30,WARN = WARNING,INFO = 20,DEBUG = 10,NOTSET = 0
logger = logging.getLogger(__name__)
logger.info("info logs")

pd_input = csv_pandas(props["TEST"]["IP_TEST_DOC_FILEPATH"])
headers = json.loads(props["TEST"]["HEADERS"])

for index, row in pd_input.iterrows():
    logger.info("Executing test : {}".format(row["ID"]))
    # print (row["ID"], row["API_INPUT"])
    if row["METHOD"] == 'POST':
        print("its a post method{}".format(row["ID"]))
        http_output =invoke_post_call(ip=props["TEST"]["USER_SERVICE_HOST_IP"],url=row['URL'],
                         headers=headers,input_palyload=row["API_INPUT"])
        diff_keys = json_validation(http_out_json=http_output.json(),expected_output_json=json.loads(row["EXPECTED_OUTPUT"]))
        for k in diff_keys.keys():
            print("keys and values are {} :{}".format(k,diff_keys[k]))
        # json_validation(http_out_json=row["API_INPUT"],expected_output_json=row["EXPECTED_OUTPUT"])



    elif row["METHOD"] == 'GET':
        print("its a get method{}".format(row["ID"]))
    elif row["METHOD"] == 'PUT':
        print("its a PUT method{}".format(row["ID"]))
    elif row["METHOD"] == 'DELETE':
        print("its a PUT method{}".format(row["ID"]))
