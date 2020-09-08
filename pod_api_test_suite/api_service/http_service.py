import json
import requests
import logging


def invoke_post_call(ip,url,input_palyload,headers):
    final_url = str(ip)+str(url)
    http_output = requests.post(final_url, data=json.dumps(json.loads(input_palyload)), headers=headers)
    # print(http_output.status_code)
    # print(http_output.json())
    return http_output


def invoke_get_call(ip,url,headers):
    final_url = str(ip)+str(url)
    http_output = requests.get(final_url, headers=headers)
    return http_output


def invoke_put_call(ip,url,headers):
    final_url = str(ip)+str(url)
    http_output = requests.put(final_url, headers=headers)
    return http_output