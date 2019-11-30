from pymongo import MongoClient


mongo_url = ''

def test_pymongo():
    client = MongoClient()
    # client = MongoClient(‘host’, port_number)
    #client = MongoClient(‘localhost’, 27017)
    client = MongoClient('mongodb://localhost:27017/')
    mydatabase = client['test']
    mycollection = mydatabase['booking']
    cursor = mycollection.find({})
    for document in cursor:
        print(document)
def delete_docs_collection():
    client = MongoClient('mongodb://localhost:27017/')
    mydatabase = client['test']
    mycollection = mydatabase['booking']

    mycollection.delete_many({})


test_pymongo()
delete_docs_collection()
