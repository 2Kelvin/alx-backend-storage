#!/usr/bin/env python3
'''Insert a mongoDb document'''


def insert_school(mongo_collection, **kwargs):
    '''inserts a new document'''
    newDocument = mongo_collection.insert_one(kwargs)
    return newDocument.inserted_id