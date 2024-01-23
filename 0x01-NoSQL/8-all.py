#!/usr/bin/env python3
'''List all documents in the mongodb collection'''


def list_all(mongo_collection):
    '''listing all documents in the passed collection'''
    return [eachDocument for eachDocument in mongo_collection.find()]
