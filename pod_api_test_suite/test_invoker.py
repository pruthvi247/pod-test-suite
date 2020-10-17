import sys,os
import subprocess
import json
import webbrowser
sys.path.insert(0, os.path.abspath(os.path.abspath('')))

from pod_api_test_suite.utils.api_arg_parsing import CliArgParse
from pod_api_test_suite.utils.mongodb_utils import clean_mongo_collection

#python pod_api_test_suite/test_invoker.py --end_point_ip=192.168.0.177 --output_report_path=/Users/pruthvikumar/Desktop/rough --port=8081
ip_args = CliArgParse().get_args()



URL_PREFIX = "http://"+str(ip_args.end_point_ip)+":"+str(ip_args.port)
HEADERS = ip_args.headers
OUTPUT_REPORT_PATH = ip_args.output_report_path
INPUT_FILE_PATH = ip_args.input_file_path

input_param_dict={}
input_param_dict["URL_PREFIX"] = URL_PREFIX
input_param_dict["HEADERS"] = HEADERS
input_param_dict["OUTPUT_REPORT_PATH"] = OUTPUT_REPORT_PATH
input_param_dict["INPUT_FILE_PATH"] = INPUT_FILE_PATH

def write_params_to_json():
    file_prefix = str(os.getcwd()) + "/pod_api_test_suite/properties/"
    print(file_prefix)
    with open(file_prefix+'ip_cli_params.json', 'w') as fp:
        json.dump(input_param_dict, fp)

write_params_to_json()

# cmd = "/Users/pruthvikumar/Documents/workspace/eclipse-work-space/pod-test-suite/pod_api_test_suite/drivers/api_service_driver.py"
cmd = str(ip_args.driver_path)
subprocess.call(["pytest",cmd, "-sv"])

# ### this open test report in default browser
webbrowser.open('file://' + os.path.realpath(OUTPUT_REPORT_PATH.replace('.csv', '.html')))

mongodb_url = "mongodb://172.20.10.7:27017/"
db_name = 'test'
collection = "parkingSpot"

# ### used to clean up the collection, comment it if not needed
clean_mongo_collection(mongo_db_url=mongodb_url,db_name=db_name,collection_name=collection)