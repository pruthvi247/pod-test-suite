import sys
import pytest
import pandas as pd
import json
import webbrowser, os

sys.path.insert(0, os.path.abspath(os.path.abspath('')))

import pod_api_test_suite.utils.csv_util as csv
import pod_api_test_suite.utils.pandas_util as pdutil
from pod_api_test_suite.validation import input_validation
from pod_api_test_suite.properties.enum import RestMethods
from pod_api_test_suite.properties.enum import ColumnHeaders
import pod_api_test_suite.api_service.http_service as https
from pod_api_test_suite.validation import output_validation
from pod_api_test_suite.utils import report_util
from pod_api_test_suite.utils.input_param_util import read_input_json
from pod_api_test_suite.utils.input_json_util import prepare_dependent_input_json

"""
TODO : should look at work around for passing arguments through command line
#  ## Below arg parsing works, commented it because pytest is not able to read the args
#  ## eg command : python pod_api_test_suite/drivers/api_service_driver.py \
 --end_point_ip=192.168.0.177 --output_report_path=/Users/pruthvikumar/Desktop/rough --port=8081

# ip_args = CliArgParse().get_args()
# URL_PREFIX = "http://"+str(ip_args.end_point_ip)+str(ip_args.port)
# HEADERS = ip_args.headers
# OUTPUT_REPORT_PATH = ip_args.output_report_path

"""

# ## This is to read the input cli params that is written to json file
#
# input_df = csv.csv_reader_pandas('/Users/pruthvikumar/Documents/workspace/a1m/pod-test-suite/pod_user_service_suite/data/booking_service_test_cases.csv')
#
# input_dict = pdutil.pandas_to_dict(input_df)
# final_report_dict = {}
# response_dict={}   # #### This dict is to store http response of all the test cases
#
# # input_validation.validate_input_csv_format(input_df)
#
# @pytest.mark.parametrize("input_value", input_dict.items())
# def test_sample(input_value):
#     print(type(input_value))
#     print(input_value[0])

############ Start from here
input_file_name = '/Users/pruthvikumar/Documents/workspace/a1m/pod-test-suite/pod_user_service_suite/data/booking_service_test_cases.csv'

# input_validation.validate_input_csv_format(input_df)
def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row
csv_gen = (row for row in open(input_file_name))
csv_gen1 = csv_reader(input_file_name)

@pytest.mark.parametrize("input_value", csv_gen)
@pytest.mark.parametrize("input_value1", csv_gen1)
def test_sample(input_value,input_value1):
    print(type(input_value))
    print(input_value)
    # print(input_value[0])
    # assert True
