#!/usr/bin/python3
""" update many topics """
from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')
db = client['logs']
collection = db['nginx']

count = collection.count_documents({})
print(f"{count} logs")
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
print("Methods:")
for method in methods:
    count = collection.count_documents({"method": method})
    print(f"\tmethod {method}: {count} logs")

specific_query = {"method": "GET", "path": "/status"}
specific_count = collection.count_documents(specific_query)
print(f"{specific_count} status check")

if __name__ == "__main__":
    pass
