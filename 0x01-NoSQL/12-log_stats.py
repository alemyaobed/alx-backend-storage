#!/usr/bin/env python3
'''
Write a Python script that provides some stats about Nginx
logs stored in MongoDB:

Database: logs
Collection: nginx
Display (same as the example):
first line: x logs where x is the number of documents in this collection
second line: Methods:
5 lines with the number of documents with the
method = ["GET", "POST", "PUT", "PATCH", "DELETE"] in this
order (see example below - warning: it’s a tabulation before each line)
one line with the number of documents with:
method=GET
path=/status
You can use this dump as data sample: dump.zip

The output of your script must be exactly the same as the example
'''
from pymongo import MongoClient


client = MongoClient("mongodb://127.0.0.1:27017")
# CORRECT BUT I WAS GOING THE LONG WAY

# db = client.logs
# collection_items = list(db.nginx.find())

# methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
# print("{} logs".format(len(collection_items)))
# print("Methods:")
# for method in methods:
#     items = list(db.nginx.find({"method": method}))
#     print("\t method " + method + f": {len(items)}")

# print(len(list(db.nginx.find(
#     {"$and: {'method': 'GET'}, {'path': '/status'}"})))
#     )
# print(list(db.nginx.find())[0])

db = client.logs
collection = db.nginx

# Total number of documents
total_logs = collection.count_documents({})
print(f"{total_logs} logs")

# Number of documents by method
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
print("Methods:")
for method in methods:
    count = collection.count_documents({"method": method})
    print(f"\tmethod {method}: {count}")

# Number of documents with method=GET and path=/status
status_check = collection.count_documents({"method": "GET", "path": "/status"})
print(f"{status_check} status check")
