# -*- coding: utf-8 -*-

import numpy
import matplotlib.pyplot as plt

def cooling_diffeq(k, Tenv):
    def f(t, T):
        return -k*(T-Tenv)

    return f

def solve(f, F0, eps, h, n):
    x=0
    F=F0    # T=T(t)
    l=[]
    c=0
    while True:

        if c % n == 0:
            l.append(F)

        dFdt=f(x, F)

        deltaF=dFdt*h

        if abs(deltaF) < eps:
            break

        x=x+h
        F=F+deltaF
        c+=1

    return l


def draw(sol):
    plt.plot(sol)
    plt.show()


if __name__=="__main__":
    sol = solve(f=cooling_diffeq(k=0.1, Tenv=24),
                F0=100,
                eps=0.01,
                h=0.1,
                n=10
                )
    draw(sol)
