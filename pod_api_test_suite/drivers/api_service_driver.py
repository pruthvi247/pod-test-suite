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

## This is to read the input cli params that is written to json file
input_param_dict = read_input_json(str(str(os.getcwd()) + "/pod_api_test_suite/properties/")+"ip_cli_params.json")

input_df= csv.csv_reader_pandas(input_param_dict['INPUT_FILE_PATH'])

URL_PREFIX = input_param_dict['URL_PREFIX']
HEADERS = input_param_dict['HEADERS']
OUTPUT_REPORT_PATH = input_param_dict['OUTPUT_REPORT_PATH']

input_dict = pdutil.pandas_to_dict(input_df)
final_report_dict = {}
response_dict={}   # #### This dict is to store http response of all the test cases

input_validation.validate_input_csv_format(input_df)

@pytest.mark.parametrize("input_value", input_dict.items())
def test_sample(input_value):

    if input_value[1]['METHOD'] == str(RestMethods.POST.name):
        print(f'Executing test case : {input_value[0]}')
        ip_url = str(input_value[1][ColumnHeaders.URL.name])

        ip_payload = input_value[1]["API_INPUT"]

        if str(input_value[1]["DEPENDENT"]).lower() != "no":
            print("<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>")
            print(input_value[0])
            ip_payload = prepare_dependent_input_json(dep_json=json.loads(input_value[1]["DEPENDENT"]),input_json=json.loads(input_value[1]["API_INPUT"]),parent_json=response_dict[str(json.loads(input_value[1]["DEPENDENT"])["dependent_test_case_id"])])

        http_output = https.invoke_post_call(ip=URL_PREFIX, url=ip_url,
                                             headers=HEADERS, input_palyload=ip_payload)
        print("TRACE >>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(http_output.json())
        print(type(http_output.json()))

        response_dict[str(input_value[0])] = json.dumps(http_output.json())

        # # compares expected json with http output
        diff_dict = output_validation.json_validation(http_out_json=http_output.json(),
                                                      expected_output_json=json.loads(
                                                          input_value[1]["EXPECTED_OUTPUT"]))

        final_report_dict.update(report_util.prepare_output_dict(diff_dict, testID=input_value[0]))
        print(final_report_dict)

    elif input_value[1]['METHOD'] == str(RestMethods.GET.name):
        print(f'Executing test case : {input_value[0]}')
        ip_url = str(input_value[1][ColumnHeaders.URL.name])

        http_output = https.invoke_get_call(ip=URL_PREFIX, url=ip_url,
                                            headers=HEADERS)

        # # compares expected json with http output
        diff_dict = output_validation.json_validation(http_out_json=http_output.json(),
                                                      expected_output_json=json.loads(
                                                          input_value[1]["EXPECTED_OUTPUT"]))

        final_report_dict.update(report_util.prepare_output_dict(diff_dict, testID=input_value[0]))

    elif input_value[1]['METHOD'] == str(RestMethods.PUT.name):
        print(f'Executing test case : {input_value[0]}')
        ip_url = str(input_value[1][ColumnHeaders.URL.name])
        ip_payload = input_value[1]["API_INPUT"]

        http_output = https.invoke_put_call(ip=URL_PREFIX, url=ip_url,
                                            headers=HEADERS, input_palyload=ip_payload)

        # # compares expected json with http output
        diff_dict = output_validation.json_validation(http_out_json=http_output.json(),
                                                      expected_output_json=json.loads(
                                                          input_value[1]["EXPECTED_OUTPUT"]))

        final_report_dict.update(report_util.prepare_output_dict(diff_dict, testID=input_value[0]))
        print(final_report_dict)

    elif input_value[1]['METHOD'] == str(RestMethods.DELETE.name):
        assert False, f" {input_value[1]['METHOD']} : Method is not implemented in test suite, please contact testing team, check {input_value[0]} test case"
    else:

        assert False, f" {input_value[1]['METHOD']} : Method is not implemented in test suite,please contact testing team, check {input_value[0]} test case"

    # writing final_report to csv
    report_util.write_to_csv(OUTPUT_REPORT_PATH, final_report_dict)
    report_util.write_to_html(OUTPUT_REPORT_PATH)
    # ### writing http output of all test cases to csv, extracting output path form --output_report_path input parameter, appending "_http_resp.csv" to the file path
    http_out_path = OUTPUT_REPORT_PATH.replace('.csv', '_http_resp.csv')
    report_util.write_to_csv(http_out_path, response_dict)



