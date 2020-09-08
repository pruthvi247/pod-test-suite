import pandas as pd

from pod_api_test_suite.properties.enum import ColumnHeaders

def pandas_to_dict(pd_df):
    """This method is used to convert pandas dataframe to dictionory so that we can pass dict as a pytest.mark.parametrize to test function
    keys will be test case id, values are dict
    reference : https://stackoverflow.com/questions/26716616/convert-a-pandas-dataframe-to-a-dictionary/38043364
    """
    pd_df.set_index(str(ColumnHeaders.ID.name), drop=True, inplace=True)  # set_index to set ID columns as the dataframe index.

    pd_dict = pd_df.to_dict(orient="index")   # orient=index parameter to have the index as dictionary keys.


    return pd_dict
