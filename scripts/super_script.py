import argparse
import json
import os
import sys
import subprocess
import webbrowser, os


parser = argparse.ArgumentParser(description='Super script to invoke test cases')
parser.add_argument("--ip",default="localhost")
parser.add_argument("--port",default="8080")
parser.add_argument("--ipFile")
parser.add_argument("--opFile")
parser.add_argument("--service",required=True)
parser.add_argument("--basePath",required=True)


args = parser.parse_args()
project_home_folder = args.basePath
if args.service.lower() == 'booking':

    #default properties set to the path present in repo, user can change it by passing it through command line
    property_json_filepath= str(project_home_folder)+"pod_user_service_suite/config/booking_service_properties.json"

    if args.ipFile is None:
        input_filepath = project_home_folder+"pod_user_service_suite/data/booking_service_test_cases.csv"
    else:
        input_filepath= args.ipFile

    if args.opFile is None:
        output_filepath = project_home_folder + "/pod_user_service_suite/data/booking_service_test_report.csv"
    else:
        output_filepath=args.opFile

    def updateJsonFile():
        jsonFile = open(property_json_filepath, "r") # Open the JSON file for reading
        properites_json = json.load(jsonFile) # Read the JSON into the buffer
        # print(data)
        jsonFile.close() # Close the JSON file

        ## Working with buffered content
        properites_json["TEST"]["IP_TEST_DOC_FILEPATH"] = input_filepath
        properites_json["TEST"]["USER_SERVICE_HOST_IP"] = "http://"+args.ip+":"+args.port
        properites_json["TEST"]["OP_FILEPATH"]=output_filepath
        # print(properites_json)

        ## Save our changes to JSON file
        jsonFile = open(property_json_filepath, "w+")
        jsonFile.write(json.dumps(properites_json))
        jsonFile.close()
    updateJsonFile()
    cmd = args.basePath+"pod_user_service_suite/test_cases/booking_service_test_cases.py"
    subprocess.call(["python3",cmd])
    webbrowser.open('file://' + os.path.realpath(output_filepath.replace('.csv', '.html')))

if args.service.lower() == 'userservice':

    #default properties set to the path present in repo, user can change it by passing it through command line
    property_json_filepath= str(project_home_folder)+"pod_user_service_suite/config/user_service_properties.json"

    if args.ipFile is None:
        input_filepath = project_home_folder+"pod_user_service_suite/data/user_service_test_cases.csv"
    else:
        input_filepath= args.ipFile

    if args.opFile is None:
        output_filepath = project_home_folder + "/pod_user_service_suite/data/user_service_test_report.csv"
    else:
        output_filepath=args.opFile

    def updateJsonFile():
        jsonFile = open(property_json_filepath, "r") # Open the JSON file for reading
        properites_json = json.load(jsonFile) # Read the JSON into the buffer
        # print(data)
        jsonFile.close() # Close the JSON file

        ## Working with buffered content
        properites_json["TEST"]["IP_TEST_DOC_FILEPATH"] = input_filepath
        properites_json["TEST"]["USER_SERVICE_HOST_IP"] = "http://"+args.ip+":"+args.port
        properites_json["TEST"]["OP_FILEPATH"]=output_filepath
        # print(properites_json)

        ## Save our changes to JSON file
        jsonFile = open(property_json_filepath, "w+")
        jsonFile.write(json.dumps(properites_json))
        jsonFile.close()
    updateJsonFile()
    cmd = args.basePath+"pod_user_service_suite/test_cases/user_service_test_cases.py"
    subprocess.call(["python3",cmd])
    webbrowser.open('file://' + os.path.realpath(output_filepath.replace('.csv', '.html')))
if args.service.lower() == 'parkingspot':

    #default properties set to the path present in repo, user can change it by passing it through command line
    property_json_filepath= str(project_home_folder)+"pod_user_service_suite/config/parkingspot_service_properties.json"

    if args.ipFile is None:
        input_filepath = project_home_folder+"pod_user_service_suite/data/parkingspot_service_test_cases.csv"
    else:
        input_filepath= args.ipFile

    if args.opFile is None:
        output_filepath = project_home_folder + "/pod_user_service_suite/data/parkingspot_service_test_report.csv"
    else:
        output_filepath=args.opFile

    def updateJsonFile():
        jsonFile = open(property_json_filepath, "r") # Open the JSON file for reading
        properites_json = json.load(jsonFile) # Read the JSON into the buffer
        # print(data)
        jsonFile.close() # Close the JSON file

        ## Working with buffered content
        properites_json["TEST"]["IP_TEST_DOC_FILEPATH"] = input_filepath
        properites_json["TEST"]["USER_SERVICE_HOST_IP"] = "http://"+args.ip+":"+args.port
        properites_json["TEST"]["OP_FILEPATH"]=output_filepath
        # print(properites_json)

        ## Save our changes to JSON file
        jsonFile = open(property_json_filepath, "w+")
        jsonFile.write(json.dumps(properites_json))
        jsonFile.close()
    updateJsonFile()
    cmd = args.basePath+"pod_user_service_suite/test_cases/parkingspot_service_test_cases.py"
    subprocess.call(["python3",cmd])
    webbrowser.open('file://' + os.path.realpath(output_filepath.replace('.csv', '.html')))

