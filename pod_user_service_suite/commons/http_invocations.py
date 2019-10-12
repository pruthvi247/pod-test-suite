import json
import requests
import logging

from pod_user_service_suite.utils.json_utils import load_properties_from_json

v_props = load_properties_from_json(filepath='pod_user_service_suite/config/user_service_properties.json')
logging.getLogger().setLevel(v_props["TEST"]["LOGGING_LEVEL"]) # setting log levels = CRITICAL = 50,FATAL = CRITICAL,ERROR = 40,WARNING = 30,WARN = WARNING,INFO = 20,DEBUG = 10,NOTSET = 0
logger = logging.getLogger(__name__)
logger.info("info logs")



def invoke_post_call(ip,url,input_palyload,headers):
    print("inside invoke_post_call")
    # print(ip)
    # print(url)
    # print(input_palyload)
    # print(headers)
    final_url = str(ip)+str(url)
    http_output=requests.post(final_url, data=json.dumps(json.loads(input_palyload)), headers=headers)
    print(http_output.status_code)
    print(http_output.json())


    return http_output
    # print(http_output)
    # print("=======>>>>> {}".format(type(input_payload)))
    # print("=======>>>>> {}".format(type(input_json)))