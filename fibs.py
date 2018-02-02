# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 14:50:08 2018

@author: User25
"""

db={1:1, 2:1}


def fib1(n):
    assert n>=1, "must be positive"
    if n<=2:
        return 1
    else:
        return fib1(n-1)+fib1(n-2)

def fib3(n):
    assert n>=1, "must be positive"
    try:
        return db[n]
    except KeyError:
        r = fib3(n-1)+fib3(n-2)
        db[n]=r
        return r


def fib2(n):
    assert n>=1, "must be positive"
    a,b=1,1
    while n>1:
        a,b=b,a+b
        n-=1
    return a

m=fib3(100)
print(m)