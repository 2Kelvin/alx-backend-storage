#!/usr/bin/env python3
'''Log stats'''
from pymongo import MongoClient


def nginxLogs():
    '''provides nginx log stats stored in mongodb'''
    mongoClient = MongoClient("mongodb://localhost:27017")
    collection = mongoClient.logs.nginx

    allLogs = collection.count_documents({})
    getLogs = collection.count_documents({'method': 'GET'})
    postLogs = collection.count_documents({'method': 'POST'})
    putLogs = collection.count_documents({'method': 'PUT'})
    patchLogs = collection.count_documents({'method': 'PATCH'})
    deleteLogs = collection.count_documents({'method': 'DELETE'})
    pathLogs = collection.count_documents({'method': 'GET', 'path': '/status'})

    print(f'{allLogs} logs')
    print('Methods:')

    print(f'\tmethod GET: {getLogs}')
    print(f'\tmethod POST: {postLogs}')
    print(f'\tmethod PUT: {putLogs}')
    print(f'\tmethod PATCH: {patchLogs}')
    print(f'\tmethod DELETE: {deleteLogs}')

    print(f'{pathLogs} status check')


if __name__ == '__main__':
    nginxLogs()
