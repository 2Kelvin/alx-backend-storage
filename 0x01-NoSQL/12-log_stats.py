#!/usr/bin/env python3
'''Log stats'''
from pymongo import MongoClient


def nginxLogs(collection):
    '''provides nginx log stats stored in mongodb'''
    print(f'{collection.estimated_document_count()} logs')

    print('Methods:')

    httpMethods = ['GET', 'POST', 'DELETE', 'PATCH', 'PUT']

    for httpMethod in httpMethods:
        methodCount = collection.count_documents({"method": httpMethod})
        print(f'\tmethod {httpMethod}: {methodCount}')

    getCount = collection.count_documents({"method": "GET", "path": "/status"})
    print(f'{getCount} status check')


if __name__ == '__main__':
    collection = MongoClient("mongodb://localhost:27017").logs.nginx
    nginxLogs(collection)
