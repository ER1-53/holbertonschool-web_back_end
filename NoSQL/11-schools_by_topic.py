#!/usr/bin/env python3
""" update many topics """


def schools_by_topic(mongo_collection, topic):
    """ find one document"""
    find_one = mongo_collection.find({"topics": topic})
    return find_one
