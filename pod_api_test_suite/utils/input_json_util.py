
from operator import itemgetter
from operator import getitem
from functools import reduce
import json

def nested_set(dic, keys, value, create_missing=True):
    # ## [source: https://stackoverflow.com/questions/13687924/setting-a-value-in-a-nested-python-dictionary-given-a-list-of-indices-and-value,
    # ## reference : https://hackersandslackers.com/extract-data-from-complex-json-python/]
    d = dic
    if type(keys) == list:
        for key in keys[:-1]:
            if key in d:
                d = d[key]
            elif create_missing:
                d = d.setdefault(key, {})
            else:
                return dic
        if keys[-1] in d or create_missing:
            d[keys[-1]] = value
        return dic
    else:
        if keys in d or create_missing:
            d[keys] = value
            return dic


def prepare_dependent_input_json(dep_json,input_json,parent_json):
    #  ###This method is used to prepare json input which is dependent on the output of other test case
    print("Preparing dependent input json")
    # ##myvalues = itemgetter(*dep_json["dependent_test_case_key"])(parent_json) ## this will get values of all the keys in the list,will not work if the list is heirarchy
    *path,key =dep_json["dependent_test_case_key"]
    rr_value = reduce(getitem,path,parent_json)[key]
    *dest_path,dest_key = dep_json["current_test_case_key"]
    reduce(getitem, dest_path, input_json)[dest_key] = rr_value
    print(input_json)
    print(type(input_json))
    print(input_json["station"]["id"])


    return json.dumps(input_json)
    # print(rr)
    # print(*dep_json["dependent_test_case_key"])
    # print(type(parent_json))
    # print(type(dep_json))
    # print(dep_json["dependent_test_case_key"])
    # print(type(dep_json["dependent_test_case_key"]))
    # nested_set(dic=input_json,keys=dep_json["current_test_case_key"],value="")
