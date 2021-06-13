import pandas as pd
import requests
import json
import pytest


# def inc(x):
#     return x + 1
#
#
# def test_answer():
#     assert inc(4) == 5


# input_pd = pd.read_csv('/Users/pruthvi.kumar/Documents/workspace/eclipse-workspace/pod-test-suite/pod_user_service_suite/data/booking_service_test_cases.csv')

input_palyload = """{"code": "book123","customer": {"userId": "cust101"},"dateOfBooking": "2019-11-14T09:22:25.619Z","owner": {"userId": "owner101"},
"parkingEndDate": "2019-11-14T09:23:25.62Z",
"parkingSpotId": "spot101","parkingStartDate": "2019-11-13T09:21:25.619Z"}"""

headers = json.loads("{\"Content-Type\": \"application/json\"}")
# http_output = requests.post('http://localhost:8081/booking', data=json.dumps(json.loads(input_palyload)), headers=headers)
# print(http_output)
def post_call():
    http_output = requests.post('http://localhost:8081/booking', data=json.dumps(json.loads(input_palyload)),
                                headers=headers)
    return http_output

output=[]

def temp_method(input,expected):
    output.append(expected+1)

    assert eval(input) == expected

ll = [("3+5", 8),("2+4", 6),("6*7", 42),]

@pytest.mark.parametrize("input,expected", ll)


def test_post(input,expected):
    temp_method(input,expected)
    # assert eval(input) == expected
    output.append(55)
    output.append(66)
    http_output = post_call()
    output.append(str(http_output))
    with open('/Users/pruthvi.kumar/Desktop/pytest.txt', 'w') as f:
        for item in output:
            f.write("%s\n" % item)

# def test_get():
#     pass
# def test_post():
#     http_output = post_call()
#     # http_output = requests.post('http://localhost:8081/booking', data=json.dumps(json.loads(input_palyload)),
#     #                             headers=headers)
#     print(http_output)
#     print(http_output.status_code)
#     assert http_output.status_code == 400
#     # print(type(http_output.status_code))


