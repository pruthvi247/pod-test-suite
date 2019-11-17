import configparser
import json
import logging
import sys
import os

# log_levels = CRITICAL = 50,FATAL = CRITICAL,ERROR = 40,WARNING = 30,WARN = WARNING,INFO = 20,DEBUG = 10,NOTSET = 0

logging.getLogger().setLevel(10)
logger = logging.getLogger(__name__)

def load_properties_from_json(filepath) :
    with open(filepath,'r') as f:
        logging.debug("reading json properties file from ::{}".format('pod_user_service_suite/config/user_service_properties.json'))
        confprop = json.load(f)
    return confprop

def compare_json(json1, json2,result=None):
    # json1 is expected output
    # json2 is http output

    if result is None:
        result={}
    #Compare all keys
    for key in json1.keys():
        #if key exist in json2:
        if key in json2.keys():
            #If subjson
            if type(json1[key]) == dict:
                dict_keys = {}
                compare_json(json1[key], json2[key],result)
            elif type(json1[key]) == list:
                if type(json1[key][0]) == dict:
                    compare_json(json1[key][0], json2[key][0], result)

            else:
                if json1[key] != json2[key]:
                    # print("These entries are different:")
                    result[key] = [json1[key],json2[key]]
        else:
            print("found new key in json1 %r" % key)
    return result


def make_dict(filepath) :
    with open(filepath,'r') as f:
        logging.debug("reading json properties file from ::{}".format('pod_user_service_suite/config/user_service_properties.json'))
        confprop = json.load(f)
    return confprop

# def compare_json(json1, json2):
#     dict_keys={}
#
#     #Compare all keys
#     for key in json1.keys():
#         #if key exist in json2:
#         if key in json2.keys():
#             #If subjson
#             if type(json1[key]) == dict:
#                 compare_json(json1[key], json2[key])
#             else:
#                 if json1[key] != json2[key]:
#                     print("These entries are different:")
#                     dict[key] = [json1[key],json2[key]]
#                     print(json1[key])
#                     print(json2[key])
#         else:
#             print("found new key in json1 %r" % key)
#     return dict

if __name__== "__main__":
    print(type(load_properties_from_json()))