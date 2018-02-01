# -*- coding: utf-8 -*-

import numpy
import matplotlib.pyplot as plt

def cooling_diffeq(k, Tenv):
    def f(t, T):
        return -k*(T-Tenv)
        
    return f

def solve(f, f0, eps, h, n):
    x=0
    F=f0    # T=T(t)
    l=[]
    c=0
    Fprev=F+2*eps
    while abs(F-Fprev)>eps:
        dF=f(x, F)*h
        x=x+h
        Fprev=F
        F=F+dF
        
        if c % n == 0:
            l.append(F)
        c+=1
    
    return l
    

def draw(sol):
    plt.plot(sol)


if __name__=="__main__":
    sol = solve(f=cooling_diffeq(k=0.1, Tenv=24),
                f0=100,
                eps=0.01,
                h=0.1,
                n=10
                )
    draw(sol)