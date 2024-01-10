#!/usr/bin/env python3
"""" find all from db mongo """


def list_all(mongo_collection):
    """ method find"""
    find_all = mongo_collection.find()
    return find_all
