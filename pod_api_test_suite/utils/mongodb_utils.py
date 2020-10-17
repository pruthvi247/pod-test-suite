from pymongo import MongoClient



def clean_mongo_collection(mongo_db_url,db_name,collection_name):
    print("Trying to clean mongo DB data")

    client = MongoClient(str(mongo_db_url))
    mydatabase = client[str(db_name)]
    mycollection = mydatabase[str(collection_name)]

    mycollection.delete_many({})