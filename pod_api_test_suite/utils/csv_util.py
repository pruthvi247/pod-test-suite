import pandas as pd
import json
import logging
logger = logging.getLogger(__name__)

def csv_reader_pandas(filepath):
    """This method reads csv using pandas and returns pandas data frame"""

    print("Reading input test case csv : {}".format(filepath))

    # dropna will delete columns where all values are nan
    return pd.read_csv(filepath).dropna(how='all', axis=1)
