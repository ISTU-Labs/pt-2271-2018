# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 12:10:46 2018

@author: User25
"""
import matplotlib.pyplot as plt


def euler(f,F0,x0,eps,h,m):
    x=x0 # x is the current domain element.
    F=F0 # F id the current value of the sulusion function
    # F=F(x)=F0    
    LF=[]
    LX=[]
    c=0
    while True:
        if c % m == 0: 
            LF.append(F)
            LX.append(x)
        dFdx = f(x, F)
        deltaF = dFdx*h
        
        if abs(deltaF)<eps:
            break
        
        x+=h
        F+=deltaF
        c+=1
        # F=F(x)
    
    return LX,LF

def show(Trajectory):
    LX,LF=Trajectory
    plt.plot(LX,LF)
    plt.show()
    
def kettle(k, Te):
    def f(t, T):
        return -k*(T-Te)
        
    return f

def solve(T0,Te,t0,k, eps,h):
    # print("The solution has been found!")
    Res=euler(kettle(k,Te),
            T0,
            t0,
            eps,
            h,
            m=50)
    show(Res)    


def main():
    solve(T0=100,
          Te=24,  # Tenv
          t0=0,
          k=0.01,
          eps=0.01,
          h=0.1
          )
          
main()