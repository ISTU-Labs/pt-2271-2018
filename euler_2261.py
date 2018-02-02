# -*- coding: utf-8 -*-

# Снизу вверх.
# Сверху вниз.

# Diffur1

import matplotlib.pyplot as plt
import numpy as np


# y'=f(x,y).

def expeuler(f, F0, h, eps, n, x0=0):
    x=x0
    F=F0
    # F(x0)=F(x)=F0=F
    Fp=None
    
    l=[]
    c=0
    
    while True:
        
        if c % n == 0:
            l.append(F)
        
        deltaF = f(x, F)
        
        x=x+h
        F=F+deltaF
        # F(x)=F
        c+=1

        
        if Fp is not None:
            if abs(Fp-F)<eps:
                break
        Fp=F
    
    return np.array(l), x-h
    

def show(func, tmax):
    x=np.linspace(0, tmax, len(func))
    # 
    # print(x,func)
    plt.xkcd()
    plt.plot(x, func)
    plt.plot(x, func*np.sin(x))
    plt.plot(x, -func)
    plt.title("COOLING KETTLE ... ")
    plt.show()

def kettlecooling(k, Tenv):
    
    def f(t, T):
        return -k*(T-Tenv)
    
    return f

if __name__=="__main__":
    k=0.01
    Tenv=24
    f=kettlecooling(k, Tenv)
    result,tmax = expeuler(f=f, 
                      eps=0.01,
                      F0=100.0,
                      h=0.1,
                      n=1
                      ) # result is a function
    show(result,tmax)


