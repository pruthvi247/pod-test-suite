import sys
import os
import pytest
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.abspath('')))

import pod_api_test_suite.utils.csv_util as csv
import pod_api_test_suite.utils.pandas_util as pdutil
from pod_api_test_suite.validation import input_validation


input_df = csv.csv_reader_pandas("/Users/pruthvikumar/Documents/workspace/eclipse-work-space/pod-test-suite/pod_user_service_suite/data/parkingspot_service_test_cases.csv")

input_validation.validate_input_csv_format(input_df)





# #  Converting pandas data frame to dict, so that we can convert dict to tuples.
# #  Doing this because pytest parameterize will take iterables as parameters
input_dict = pdutil.pandas_to_dict(input_df)


@pytest.mark.parametrize("value", input_dict.items())
def test_sample(value):
    print(f'input params given from function : {value[0]}')
    print(f'input params given from function : {value[1]["METHOD"]}')
    print(f'input params given from function : {value[1]["TESTCASE"]}')
    print(f'input params given from function : {type(value)}')

