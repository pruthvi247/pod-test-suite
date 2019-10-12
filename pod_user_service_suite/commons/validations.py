from pod_user_service_suite.utils.json_utils import compare_json
import logging

from pod_user_service_suite.utils.json_utils import load_properties_from_json

v_props = load_properties_from_json(filepath='pod_user_service_suite/config/user_service_properties.json')
logging.getLogger().setLevel(v_props["TEST"]["LOGGING_LEVEL"]) # setting log levels = CRITICAL = 50,FATAL = CRITICAL,ERROR = 40,WARNING = 30,WARN = WARNING,INFO = 20,DEBUG = 10,NOTSET = 0
logger = logging.getLogger(__name__)
logger.info("info logs")




def json_validation(http_out_json,expected_output_json):
    logging.debug("validating output and expected output")
    compare_json(json1=expected_output_json,json2=http_out_json)