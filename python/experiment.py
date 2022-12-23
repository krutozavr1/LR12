#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import timeit
from functools import lru_cache

def factorial(n):
    product = 1
    while n > 1:
        product *= n
        n -= 1
    return product


def fib(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a


@lru_cache()
def recursive_fib(n):
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = recursive_fib(n - 1)
        return (a + b, a)


@lru_cache()
def recursive_fact(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == '__main__':
    start_time = timeit.default_timer()
    factorial(10)
    print(timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    recursive_fact(10)
    print(timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    fib(10)
    print(timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    recursive_fib(10)
    print(timeit.default_timer() - start_time)