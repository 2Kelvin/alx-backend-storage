#!/usr/bin/env python3
'''Learning and using Redis'''
import redis
import uuid
from typing import Union, Optional, Callable, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    '''count cache method calls'''
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        '''wrapper func'''
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    '''store function i/o history'''
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        '''wrapper'''
        inpArr = f'{method.__qualname__}:inputs'
        outArr = f'{method.__qualname__}:outputs'
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(inpArr, str(args))
        out = method(self, *args, **kwargs)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(outArr, out)
        return out
    return wrapper


def replay(fn: Callable) -> None:
    '''displays the history of calls of a particular function'''
    if fn is None or not hasattr(fn, '__self__'):
        return
    rStore = getattr(fn.__self__, '_redis', None)
    if not isinstance(rStore, redis.Redis):
        return
    functionName = fn.__qualname__
    inpArr = f'{functionName}:inputs'
    outArr = f'{functionName}:outputs'
    functionCount = 0
    if rStore.exists(functionName) != 0:
        functionCount = int(rStore.get(functionName))
    print(f'{functionName} was called {functionCount} times:')
    inp = rStore.lrange(inpArr, 0, -1)
    out = rStore.lrange(outArr, 0, -1)
    for i, o in zip(inp, out):
        print(f'{functionName}(*{i.decode("utf-8")}) -> {o}')
    return None


class Cache:
    '''class Cache'''

    def __init__(self) -> None:
        '''class constructor'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''stores data in Redis db using the randomly generated key'''
        randomKey: str = str(uuid.uuid4())
        self._redis.set(randomKey, data)
        return randomKey

    def get(self, key: str, fn:
            Optional[Callable[[bytes], Union[str, bytes, int, float]]] = None)\
            -> Union[str, bytes, int, float, None]:
        '''custom get() method'''
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            data = fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        '''convert redis data to regular string'''
        return self.get(key, lambda x: x.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        '''convert redis data to regular int'''
        return self.get(key, lambda x: int(x))
