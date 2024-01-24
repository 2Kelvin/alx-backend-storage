#!/usr/bin/env python3
'''Learning and using Redis'''
import redis
import uuid
from typing import Union


class Cache:
    '''class Cache'''

    def __init__(self) -> None:
        '''class constructor'''
        self._redis = redis.Redis(
            host='localhost', port=6379, decode_responses=True)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''stores data in Redis db using the randomly generated key'''
        randomKey: str = str(uuid.uuid4())
        self._redis.set(randomKey, data)
        return randomKey
