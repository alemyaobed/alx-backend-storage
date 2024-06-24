#!/usr/bin/env python3
'''
Writing strings to redis
'''
import functools
import redis
from typing import Union, Callable, Optional
import uuid


def count_calls(method: Callable) -> Callable:
    '''Decorator to count the number of calls to a method'''
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        # Increment the call count in Redis
        key = f"{method.__qualname__}"
        self._redis.incr(key)
        # Call the original method
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    '''
    Task 0:
    Create a Cache class. In the __init__ method, store an instance
    of the Redis client as a private variable named _redis
    (using redis.Redis()) and flush the instance using flushdb.

    Create a store method that takes a data argument and returns
    a string. The method should generate a random key (e.g. using uuid),
    store the input data in Redis using the random key and return the key.

    Type-annotate store correctly. Remember that data can be a str, bytes,
    int or float.

    Task 1:
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

    Task 2:
    Familiarize yourself with the INCR command and its python equivalent.

    In this task, we will implement a system to count how many times methods
    of the Cache class are called.

    Above Cache define a count_calls decorator that takes a single method
    Callable argument and returns a Callable.

    As a key, use the qualified name of method using the __qualname__
    dunder method.

    Create and return function that increments the count for that key every
    time the method is called and returns the value returned by the original
    method.

    Remember that the first argument of the wrapped function will be self which
    is the instance itself, which lets you access the Redis instance.

    Protip: when defining a decorator it is useful to use functool.wraps to
    conserve the original function’s name, docstring, etc. Make sure you use it
    as described here.

    Decorate Cache.store with count_calls.
    '''
    def __init__(self) -> None:
        '''The constructor method for the class'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''The store method for the class'''
        random_key = str(uuid.uuid4())
        if isinstance(data, (int, float)):
            data = str(data)
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str, fn: Optional[Callable] = None) -> Optional[
            Union[str, bytes, int, float]]:
        '''
        Retrieve data from Redis and apply an optional conversion
        function
        '''
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
