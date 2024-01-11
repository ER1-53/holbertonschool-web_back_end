#!/usr/bin/env python3
""" insert in doc """


def insert_school(mongo_collection, **kwargs):
    """ insert information to db """
    return mongo_collection.insert(kwargs)
