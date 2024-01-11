#!/usr/bin/env python3
""" update many topics """
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('localhost', 27017)
    collection = client.logs.nginx

    counts = collection.count_documents({})

    print("{} logs".format(counts))

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    specific_query = {"method": "GET", "path": "/status"}
    specific_count = collection.count_documents(specific_query)
    print("{} status check".format(specific_count))
