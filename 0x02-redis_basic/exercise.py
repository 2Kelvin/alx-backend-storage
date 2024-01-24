#!/usr/bin/env python3
'''Learning and using Redis'''
import redis
import uuid
from typing import Union, Optional, Callable
import sys


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

    def get(self, key: str, fn: Optional[Callable] = None)\
            -> Union[str, bytes, int, float]:
        '''custom get() method'''
        if fn:
            return fn(self._redis.get(key))

        return self._redis.get(key)

    def get_str(self) -> str:
        '''convert redis data to regular string'''
        return self.decode("utf-8")

    def get_int(self) -> int:
        '''convert redis data to regular int'''
        return int.from_bytes(self, sys.byteorder)
