#!/usr/bin/env python3
'''Where can I learn Python?'''


def schools_by_topic(mongo_collection, topic):
    '''find data using a query'''
    return mongo_collection.find({ 'topics': topic })
