#!/usr/bin/python3
"""
insert in doc
"""


def insert_school(mongo_collection, **kwargs):
    """ insert information to db """
    insert_doc = mongo_collection.insert_one({**kwargs})
    return insert_doc
