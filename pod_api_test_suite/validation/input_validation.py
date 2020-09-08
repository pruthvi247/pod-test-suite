
import pandas as pd
import json
import math

from pod_api_test_suite.properties.enum import ColumnHeaders


def validate_input_csv_format(pd_df):
    """This method is used to validate input csv format"""
    _validate_input_column_list(pd_df.columns)
    _validate_json(pd_df)


def is_json(myjson):
    """This methods returns true is the string is valid json, otherwise returns false"""
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True


def _validate_json(pd_df):
    for index, row in pd_df.iterrows():
        # # Below assertions will validate if the input and expected output columns are in json format

        # # this check we are doing because for get calls input json will be empty, as it is pandas df , we are checking for nan value
        if not pd.isna(row[str(ColumnHeaders.API_INPUT.name)]):
            # print(f">>>>>>>>>>>>>><<<<<<<<<<<<< iput col {row['ID']}")
            assert is_json(row[str(
                ColumnHeaders.API_INPUT.name)]), f"Input of  test id : {row[str(ColumnHeaders.ID.name)]} is not in json format "
        assert is_json(row[str(
            ColumnHeaders.EXPECTED_OUTPUT.name)]), f"Expected output of  test id : {row[str(ColumnHeaders.ID.name)]} is not in json format "


def _validate_input_column_list(input_col):
    """This method validate if all expected columns are present"""

    # print(list(input_col))
    # print(len(list(input_col)))
    assert len(list(input_col)) == len(ColumnHeaders), "Either columns are missing or there are empty columns in the " \
                                                       "input csv "
