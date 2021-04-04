########### Script to get attachment ids from monogo db and copy  to new folder

from pymongo import MongoClient
import os
import shutil
import sys

# mongodb_url = "mongodb://172.20.10.7:27017/"
mongodb_url = "mongodb://localhost:27017/"
db_name = 'test'
collection = "parkingSpot"
ids_list_full = []


# ### used to clean up the collection, comment it if not needed
# clean_mongo_collection(mongo_db_url=mongodb_url,db_name=db_name,collection_name=collection)

def get_attachment_ids(mongo_db_url, db_name, collection_name):
    print("Getting attachment id's")

    client = MongoClient(str(mongo_db_url))
    mydatabase = client[str(db_name)]
    mycollection = mydatabase[str(collection_name)]

    # result = mycollection.find({"attachmentIds" : "ac3881cb-d0f8-495f-89f4-ae620ac1f08a"})
    result = mycollection.find({})
    # result = mycollection.find({"attachmentIds":""})
    print(type(result))
    print(result.count())
    for cursor in result:
        # print(cursor["attachmentIds"])
        try:
            # print(cursor["attachmentIds"])
            ids_list = cursor["attachmentIds"]
            for id in ids_list:
                ids_list_full.append(id)
        except:
            print(cursor)
    # for doc in mycollection.find():
    #     print(doc)
    # print(list(result))

    # print("Cursor attr:", result.__dict__)
    # for doc in result:
    #     print(doc)


if __name__ == '__main__':
    get_attachment_ids(mongodb_url, db_name, collection)
    print(len(ids_list_full))

    for f in ids_list_full:
        print('find . -name "*' + f + '*" -exec cp {} ../images_backup/ \;')
        os.system('find . -name "*' + f + '*" -exec cp {} ../images_backup/ \;')
        # shutil.move("/Users/pruthvikumar/Documents/workspace/a1m/parkingspot-service/parking_images/*"+f, "/Users/pruthvikumar/Documents/workspace/a1m/parkingspot-service/images_backup")
        # shutil.copy("/Users/pruthvikumar/Documents/workspace/a1m/parkingspot-service/parking_images/*"+f, "/Users/pruthvikumar/Documents/workspace/a1m/parkingspot-service/images_backup")
    print(sys.path)
