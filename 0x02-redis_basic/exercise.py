#!/usr/bin/env python3
'''
Writing strings to redis
'''
import redis
from typing import Union
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
    '''
    def __init__(self) -> None:
        '''The constructor method for the class'''
        self.__redis = redis.Redis()
        self.__redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''The store method for the class'''
        random_key = str(uuid.uuid4())
        self.__redis.set(random_key, data)
        return random_key
