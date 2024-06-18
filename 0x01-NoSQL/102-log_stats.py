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

    def get_top_ips(mongo_collection):
        pipeline = [
            {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
            {"$limit": 10}
        ]
        top_ips = {
            ip["_id"]: ip["count"] for ip in mongo_collection.
            aggregate(pipeline)}
        return top_ips

    # Top 10 IPs
    top_ips = get_top_ips(collection)
    print("IPs:")
    for ip, count in top_ips.items():
        print(f"    {ip}: {count}")


if __name__ == "__main__":
    log_stats()
