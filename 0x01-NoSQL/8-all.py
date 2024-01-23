#!/usr/bin/env python3
'''List all documents in the mongodb collection'''
from pymongo import MongoClient


def list_all(mongo_collection):
    '''listing all documents in the passed collection'''
    client = MongoClient('localhost', 27017)
    database = client.mongo_collection
