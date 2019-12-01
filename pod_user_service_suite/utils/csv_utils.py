# this method is used to read csv using pandas

import pandas as pd
import logging
from json2html import *
import json

from pod_user_service_suite.utils.json_utils import load_properties_from_json

# filepath='pod_user_service_suite/config/user_service_properties.json'
# props = load_properties_from_json(filepath)
logger = logging.getLogger(__name__)

def csv_pandas(filepath):
    logger.debug("Reading input test case csv : {}".format(filepath))
    return pd.read_csv(filepath)

def write_to_csv(filepath,dict):
    logger.debug("writing status output to csv : {}".format(filepath))
    # pd.DataFrame(dict).to_csv(filepath,index=False)
    pdseries = pd.Series(dict).to_frame()
    pd.DataFrame(pdseries).to_csv(filepath,header=['output'])
    return pd.read_csv(filepath)
def write_to_html(filepath):
    logger.debug("writing status output to html : {}".format(filepath))
    df = pd.read_csv(filepath)
    newdict = {}
    for items in df.itertuples():
        newdict[items[1]] = items[2]
    r = json.dumps(newdict)
    outhtml = json2html.convert(json=r)
    filename = filepath.replace('.csv', '.html')
    f = open(filename, 'w')
    f.write(outhtml)
    f.close()
    return pd.read_csv(filepath)
