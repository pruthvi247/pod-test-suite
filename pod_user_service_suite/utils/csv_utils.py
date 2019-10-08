# this method is used to read csv using pandas

import pandas as pd
import logging

from pod_user_service_suite.utils.json_utils import load_properties_from_json

# filepath='pod_user_service_suite/config/user_service_properties.json'
# props = load_properties_from_json(filepath)
logger = logging.getLogger(__name__)

def csv_pandas(filepath):
    logger.debug("Reading input test case csv : {}".format(filepath))
    return pd.read_csv(filepath)
