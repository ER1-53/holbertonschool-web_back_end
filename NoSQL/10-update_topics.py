#!/usr/bin/env python3
"""
update many topics
"""


def update_topics(mongo_collection, name, topics):
    """ update document """
    query = {"name": name}
    new_values = {"$set": {"topics": topics}}
    update_doc = mongo_collection.update_many(query, new_values)
    return update_doc
