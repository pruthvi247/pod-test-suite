# this method is used to read csv using pandas

import pandas as pd
import logging

from pod_user_service_suite.utils.json_utils import load_properties_from_json

props = load_properties_from_json()
logger = logging.getLogger(__name__)

def csv_pandas(filepath):
    logger.debug("Reading input test case csv : {}".format(props["TEST"]["IP_TEST_DOC_FILEPATH"]))
    return pd.read_csv(filepath)
