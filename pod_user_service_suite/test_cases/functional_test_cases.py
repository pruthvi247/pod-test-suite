import os
import sys
import logging


sys.path.insert(0, os.path.abspath(os.path.abspath('')))

from pod_user_service_suite.utils.json_utils import load_properties_from_json
from pod_user_service_suite.utils.csv_utils import csv_pandas


props = load_properties_from_json()
logging.getLogger().setLevel(props["TEST"]["LOGGING_LEVEL"]) # settng log levels = CRITICAL = 50,FATAL = CRITICAL,ERROR = 40,WARNING = 30,WARN = WARNING,INFO = 20,DEBUG = 10,NOTSET = 0
logger = logging.getLogger(__name__)
logger.info("info logs")


pd_input = csv_pandas(props["TEST"]["IP_TEST_DOC_FILEPATH"])


# logger.info(pd_input.iloc[0])
input = pd_input.iloc[0]
def first_test(input):
    logger.info(type(pd_input.iloc[0]))

first_test(input)
print("DONE !!!")