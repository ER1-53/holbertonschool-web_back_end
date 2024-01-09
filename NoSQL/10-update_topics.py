#!/usr/bin/python3
""" update many topics """


def update_topics(mongo_collection, name, topics):
    query = {"name":name}
    new_values = {"$set": {"topics": topics}}
    update_doc = mongo_collection.update_one(query, new_values)
    return update_doc
