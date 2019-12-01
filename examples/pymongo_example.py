from pymongo import MongoClient
from dicttoxml import dicttoxml
import pandas as pd
import json
from json2html import *

# mongo_url = ''
#
# def test_pymongo():
#     client = MongoClient()
#     # client = MongoClient(‘host’, port_number)
#     #client = MongoClient(‘localhost’, 27017)
#     client = MongoClient('mongodb://localhost:27017/')
#     mydatabase = client['test']
#     mycollection = mydatabase['booking']
#     cursor = mycollection.find({})
#     for document in cursor:
#         print(document)
# def delete_docs_collection():
#     client = MongoClient('mongodb://localhost:27017/')
#     mydatabase = client['test']
#     mycollection = mydatabase['booking']
#
#     mycollection.delete_many({})
#
#
# test_pymongo()
# delete_docs_collection()
def func(row):
    xml = ['<item>']
    for field in row.index:
        xml.append('  <field name="{0}">{1}</field>'.format(field, row[field]))
    xml.append('</item>')
    return '\n'.join(xml)

filepath = "/Users/pruthvi.kumar/Documents/workspace/eclipse-workspace/pod-test-suite/pod_user_service_suite/data/booking_service_test_report.csv"
df = pd.read_csv(filepath)

newdict={}
for items in df.itertuples():
    # print(items[1])
    # print(items[2])
    newdict[items[1]]= items[2]
    print("===")


# print(newdict.keys())
# print(newdict.values())

# xml = dicttoxml(newdict)
# print(xml)


r = json.dumps(newdict)
# print(r)

outhtml = json2html.convert(json = r)
print(outhtml)