import json

def compare_json(json1, json2,result=None):
    # json1 is expected output
    # json2 is http output
    # print(">>>>>>>>>>>>> validating json ouput")

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
                    if key in result:
                        temp_lst = []
                        temp_lst.append(result[key])
                        temp_lst.append(json1[key])
                        temp_lst.append(json2[key])
                        result[key]= temp_lst

                    else:
                        result[key] = [json1[key],json2[key]]
        else:
            print("found new key in json1 %r" % key)
    return result



def json_validation(http_out_json,expected_output_json):
    result_keys = compare_json(json1=expected_output_json,json2=http_out_json)
    return result_keys