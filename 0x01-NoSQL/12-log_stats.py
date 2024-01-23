#!/usr/bin/env python3
'''Log stats'''
import pymongo
from pymongo import MongoClient


def nginxLogs(mongo_collection):
    '''provides nginx log stats stored in mongodb'''
    print(f'{mongo_collection.estimated_document_count()} logs')

    print('Methods:')

    httpMethods = ['GET', 'POST', 'DELETE', 'PATCH', 'PUT']

    for httpMethod in httpMethods:
        methodCount = mongo_collection.count_documents({"method": httpMethod})
        print(f'\tmethod {httpMethod}: {methodCount}')

    getCount = mongo_collection.count_documents({"method": "GET", "path": "/status"})
    print(f'{getCount} status check')


if __name__ == '__main__':
    mongo_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    nginxLogs(mongo_collection)
