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

if __name__== "__main__":
    print(type(load_properties_from_json()))