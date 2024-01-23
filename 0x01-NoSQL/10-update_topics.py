#!/usr/bin/env python3
'''Update mongodb documents'''


def update_topics(mongo_collection, name, topics):
    '''changes document topic baased on the name'''
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
