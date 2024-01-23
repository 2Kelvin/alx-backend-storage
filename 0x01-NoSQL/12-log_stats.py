#!/usr/bin/env python3
'''Log stats'''
from pymongo import MongoClient


def nginxLogs(collection):
    '''provides nginx log stats stored in mongodb'''
    print(f'{collection.count_documents()} logs')
    print('Methods:')

    httpMethods = ['GET', 'POST', 'PUT', 'PATCH' 'DELETE']

    for httpMethod in httpMethods:
        methodCount = len(list(collection.find({"method": httpMethod})))
        print(f'\tmethod {httpMethod}: {methodCount}')

    getCount = len(list(collection.find({"method": "GET", "path": "/status"})))
    print(f'{getCount} status check')


if __name__ == '__main__':
    mongoClient = MongoClient("mongodb://127.0.0.1:27017")
    nginxLogs(mongoClient.logs.nginx)
