#!/usr/bin/env python3
'''Getting insights from data'''
from pymongo import MongoClient


def log_stats():
    '''Implementation of the function for obtaining the insights'''
    client = MongoClient('mongodb://127.0.0.1:27017')
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
    status_check = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check} status check")

    # Top 10 IPs with the highest count
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = list(collection.aggregate(pipeline))
    print("IPs:")
    for ip_info in top_ips:
        ip = ip_info["_id"]
        count = ip_info["count"]
        print(f"\t{ip}: {count}")


if __name__ == "__main__":
    log_stats()
