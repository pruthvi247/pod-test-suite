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

input_df = csv.csv_reader_pandas("/Users/pruthvikumar/Documents/workspace/eclipse-work-space/pod-test-suite/pod_user_service_suite/data/parkingspot_service_test_cases.csv")
# input_df = csv.csv_reader_pandas("/Users/pruthvikumar/Documents/workspace/eclipse-work-space/pod-test-suite/pod_user_service_suite/data/booking_service_test_cases.csv")

input_validation.validate_input_csv_format(input_df)


# #  Converting pandas data frame to dict, so that we can convert dict to tuples.
# #  Doing this because pytest parameterize will take iterables as parameters
input_dict = pdutil.pandas_to_dict(input_df)

# ## parameters
# initial_ip = "http://localhost:8081"
initial_ip = "http://localhost:8082"
HEADERS= {"Content-Type": "application/json"}
output_report_csv = "/Users/pruthvikumar/Desktop/rough/csv_report.csv"
final_report_dict = {}


@pytest.mark.parametrize("input_value", input_dict.items())
def test_sample(input_value):

    if(input_value[1]['METHOD']== str(RestMethods.POST.name)):
        print(f'Executing test case : {input_value[0]}')
        ip_url = str(input_value[1][ColumnHeaders.URL.name])
        ip_payload = input_value[1]["API_INPUT"]

        http_output = https.invoke_post_call(ip=initial_ip, url=ip_url,
                                       headers=HEADERS, input_palyload=ip_payload)

        # # compares expected json with http output
        diff_dict = output_validation.json_validation(http_out_json=http_output.json(),
                                    expected_output_json=json.loads(input_value[1]["EXPECTED_OUTPUT"]))

        final_report_dict.update(report_util.prepare_output_dict(diff_dict, testID=input_value[0]))
        print(final_report_dict)



    elif(input_value[1]['METHOD']== str(RestMethods.GET.name)):
        print(f'Executing test case : {input_value[0]}')
        ip_url = str(input_value[1][ColumnHeaders.URL.name])

        http_output = https.invoke_get_call(ip=initial_ip, url=ip_url,
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
        print("its PUT method")
    elif (input_value[1]['METHOD'] == str(RestMethods.DELETE.name)):
        print("its DELETE method")
    else:

        assert False,f" {input_value[1]['METHOD']} : Method is not implemented in test suite, check {input_value[0]} test case"

    # writing final_report to csv
    report_util.write_to_csv(output_report_csv, final_report_dict)
    report_util.write_to_html(output_report_csv)

webbrowser.open('file://' + os.path.realpath(output_report_csv.replace('.csv', '.html')))





