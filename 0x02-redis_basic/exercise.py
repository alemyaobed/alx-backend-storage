#!/usr/bin/env python3
'''
Writing strings to redis
'''
import redis
from typing import Union, Callable, Optional
import uuid


class Cache:
    '''
    Create a Cache class. In the __init__ method, store an instance
    of the Redis client as a private variable named _redis
    (using redis.Redis()) and flush the instance using flushdb.

    Create a store method that takes a data argument and returns
    a string. The method should generate a random key (e.g. using uuid),
    store the input data in Redis using the random key and return the key.

    Type-annotate store correctly. Remember that data can be a str, bytes,
    int or float.
    
    Redis only allows to store string, bytes and numbers (and lists thereof).
    Whatever you store as single elements, it will be returned as a byte
    string. Hence if you store "a" as a UTF-8 string, it will be returned as
    b"a" when retrieved from the server.

    In this exercise we will create a get method that take a key string
    argument and an optional Callable argument named fn. This callable will
    be used to convert the data back to the desired format.

    Remember to conserve the original Redis.get behavior if the key does
    not exist.

    Also, implement 2 new methods: get_str and get_int that will automatically
    parametrize Cache.get with the correct conversion function.

    The following code should not raise:
    '''
    def __init__(self) -> None:
        '''The constructor method for the class'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''The store method for the class'''
        random_key = str(uuid.uuid4())
        if isinstance(data, (int, float)):
            data = str(data) 
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str, fn: Optional[Callable] = None) -> Optional[Union[str, bytes, int, float]]:
        '''Retrieve data from Redis and apply an optional conversion function'''
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data
    
    def get_str(self, key: str) -> Optional[str]:
        '''Retrieve a string from Redis'''
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        '''Retrieve an integer from Redis'''
        return self.get(key, lambda d: int(d))
