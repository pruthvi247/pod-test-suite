import pandas as pd
from json2html import *
import json


report_dict ={}
def prepare_output_dict(diff_dict,testID):
    if bool(diff_dict):
        # tempvalue = '{"status":"fail","diff":' + "\"" + "{}".format(diff_dict) + "\"}"
        tempvalue = '{"status":"fail","diff":' + "{}".format(diff_dict)+"}"
        report_dict[str(testID)] = str(tempvalue)

    else:
        report_dict[str(testID)] = "{\"status\" : \"pass\"}"

    return  report_dict

def write_to_csv(filepath,dict):
    # pd.DataFrame(dict).to_csv(filepath,index=False)
    pdseries = pd.Series(dict).to_frame()
    pd.DataFrame(pdseries).to_csv(filepath,header=['output'])
    return pd.read_csv(filepath)


def write_to_html(filepath):
    """This method reads csv using pandas and converts to html page"""
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
    # print("TRACE >>>>>>>>>>>> closed html")
    return pd.read_csv(filepath)