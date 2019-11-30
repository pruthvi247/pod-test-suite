import os
import sys
import logging
import requests
import json
from pymongo import MongoClient


sys.path.insert(0, os.path.abspath(os.path.abspath('')))

from pod_user_service_suite.utils.json_utils import load_properties_from_json
# from pod_user_service_suite.utils import json_utils
from pod_user_service_suite.utils.csv_utils import csv_pandas
from pod_user_service_suite.commons.http_invocations import invoke_post_call
from pod_user_service_suite.commons.http_invocations import invoke_get_call
from pod_user_service_suite.commons.http_invocations import invoke_put_call
from pod_user_service_suite.commons.validations import json_validation
from pod_user_service_suite.utils.csv_utils import write_to_csv

props = load_properties_from_json(filepath='pod_user_service_suite/config/booking_service_properties.json')
logging.getLogger().setLevel(props["TEST"]["LOGGING_LEVEL"]) # setting log levels = CRITICAL = 50,FATAL = CRITICAL,ERROR = 40,WARNING = 30,WARN = WARNING,INFO = 20,DEBUG = 10,NOTSET = 0
logger = logging.getLogger(__name__)
logger.info("info logs")

pd_input = csv_pandas(props["TEST"]["IP_TEST_DOC_FILEPATH"])
headers = json.loads(props["TEST"]["HEADERS"])
final_report ={}

# This is util method, nothing to do with the logic of test case execution,
# this function will prepare a dict for final output
def prepare_output_dict(diff_dict,testID):
    if bool(diff_dict):
        tempvalue = '{"status":"fail","diff":' + "\"" + "{}".format(diff_dict) + "\""
        final_report[str(testID)] = tempvalue

    else:
        final_report[str(testID)] = "{\"status\" : \"pass\"}"


# Test cases execution will start form here
# Iterate over each row of csv and execute the test case one after other

for index, row in pd_input.iterrows():

    logger.info("Executing test : {}".format(row["ID"]))
    if str(row["METHOD"]).lower() == 'POST'.lower():
        print()
        http_output =invoke_post_call(ip=props["TEST"]["USER_SERVICE_HOST_IP"],url=row['URL'],
                         headers=headers,input_palyload=row["API_INPUT"])

        # compares expected json with http output
        diff_dict = json_validation(http_out_json=http_output.json(),expected_output_json=json.loads(row["EXPECTED_OUTPUT"]))
        prepare_output_dict(diff_dict,testID=row['ID'])

    elif row["METHOD"] == 'GET':
        print("its a get method{}".format(row["ID"]))
        http_output = invoke_get_call(ip=props["TEST"]["USER_SERVICE_HOST_IP"], url=row['URL'],headers=headers)
        diff_dict = json_validation(http_out_json=http_output.json(),
                                    expected_output_json=json.loads(row["EXPECTED_OUTPUT"]))
        prepare_output_dict(diff_dict, testID=row['ID'])

    elif row["METHOD"] == 'PUT':
        print("its a PUT method{}".format(row["ID"]))
        http_output = invoke_put_call(ip=props["TEST"]["USER_SERVICE_HOST_IP"], url=row['URL'],headers=headers)
        diff_dict = json_validation(http_out_json=http_output.json(),
                                    expected_output_json=json.loads(row["EXPECTED_OUTPUT"]))
        prepare_output_dict(diff_dict, testID=row['ID'])
    elif row["METHOD"] == 'DELETE':
        print("its a PUT method{}".format(row["ID"]))
    else:
        logger.exception("specified method is not implemented : {}".format(row["METHOD"]))


# writing final_report to csv
write_to_csv(props["TEST"]["OP_FILEPATH"],final_report)

def clean_booking_collection():
    client = MongoClient('mongodb://localhost:27017/')
    mydatabase = client['test']
    mycollection = mydatabase['booking']

    mycollection.delete_many({})

clean_booking_collection()