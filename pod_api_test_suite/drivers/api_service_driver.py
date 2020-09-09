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
from pod_api_test_suite.utils.api_arg_parsing import CliArgParse


# input_df = csv.csv_reader_pandas("/Users/pruthvikumar/Documents/workspace/eclipse-work-space/pod-test-suite/pod_user_service_suite/data/booking_service_test_cases.csv")
input_df = csv.csv_reader_pandas("/Users/pruthvikumar/Documents/workspace/eclipse-work-space/pod-test-suite/pod_user_service_suite/data/parkingspot_service_test_cases.csv")

input_validation.validate_input_csv_format(input_df)


# #  Converting pandas data frame to dict, so that we can convert dict to tuples.
# #  Doing this because pytest parameterize will take iterables as parameters
input_dict = pdutil.pandas_to_dict(input_df)

# ## parameters

# ip_args = CliArgParse().get_args()
# URL_PREFIX = "http://"+str(ip_args.end_point_ip)+str(ip_args.port)
# HEADERS = ip_args.headers
# OUTPUT_REPORT_PATH = ip_args.output_report_path


URL_PREFIX = "http://localhost:8082"
HEADERS = {"Content-Type": "application/json"}
OUTPUT_REPORT_PATH ="/Users/pruthvikumar/Desktop/rough/test_report.csv"

final_report_dict = {}



@pytest.mark.parametrize("input_value", input_dict.items())
def test_sample(input_value):

    if(input_value[1]['METHOD']== str(RestMethods.POST.name)):
        print(f'Executing test case : {input_value[0]}')
        ip_url = str(input_value[1][ColumnHeaders.URL.name])
        ip_payload = input_value[1]["API_INPUT"]

        http_output = https.invoke_post_call(ip=URL_PREFIX, url=ip_url,
                                       headers=HEADERS, input_palyload=ip_payload)

        # # compares expected json with http output
        diff_dict = output_validation.json_validation(http_out_json=http_output.json(),
                                    expected_output_json=json.loads(input_value[1]["EXPECTED_OUTPUT"]))

        final_report_dict.update(report_util.prepare_output_dict(diff_dict, testID=input_value[0]))
        print(final_report_dict)



    elif(input_value[1]['METHOD']== str(RestMethods.GET.name)):
        print(f'Executing test case : {input_value[0]}')
        ip_url = str(input_value[1][ColumnHeaders.URL.name])

        http_output = https.invoke_get_call(ip=URL_PREFIX, url=ip_url,
                                             headers=HEADERS)

        # # compares expected json with http output
        diff_dict = output_validation.json_validation(http_out_json=http_output.json(),
                                                      expected_output_json=json.loads(
                                                          input_value[1]["EXPECTED_OUTPUT"]))

        # if diff_dict:
        #     print(f' ???????????????? {diff_dict}')

        final_report_dict.update(report_util.prepare_output_dict(diff_dict, testID=input_value[0]))
        print(final_report_dict)
    elif (input_value[1]['METHOD'] == str(RestMethods.PUT.name)):
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
    elif (input_value[1]['METHOD'] == str(RestMethods.DELETE.name)):
        assert False,f" {input_value[1]['METHOD']} : Method is not implemented in test suite, check {input_value[0]} test case"
    else:

        assert False,f" {input_value[1]['METHOD']} : Method is not implemented in test suite, check {input_value[0]} test case"

    # writing final_report to csv
    report_util.write_to_csv(OUTPUT_REPORT_PATH, final_report_dict)
    report_util.write_to_html(OUTPUT_REPORT_PATH)

webbrowser.open('file://' + os.path.realpath(OUTPUT_REPORT_PATH.replace('.csv', '.html')))





