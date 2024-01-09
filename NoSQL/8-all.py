#!/usr/bin/python3
"""" find all from db mongo """


def list_all(mongo_collection):
    find_all = mongo_collection.find()
    return find_all
