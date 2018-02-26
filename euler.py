# -*- coding: utf-8 -*-

import numpy
import matplotlib.pyplot as plt
import sqlite3 as sql

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


def test():
    sol = solve(f=cooling_diffeq(k=0.1, Tenv=24),
                F0=100,
                eps=0.01,
                h=0.1,
                n=10
                )
    draw(sol)

#test()

def with_file(filename):
    i = open(filename, "r")
    
    k = float(i.readline().strip())
    Tenv = float(i.readline().strip())
    F0 = float(i.readline().strip())
    eps = float(i.readline().strip())
    h = float(i.readline().strip())
    n = int(i.readline().strip())
    
    i.close()
    
    sol = solve(f=cooling_diffeq(k=k, Tenv=Tenv),
                F0=F0,
                eps=eps,
                h=h,
                n=n
    )

    o=open("output.txt","w")
    
    for point in sol:
        o.write("{}\n".format(point))

    o.close()  # o.flush()

    to_sqldb(sol)
        
    # draw(sol)

def to_sqldb(result):
    conn = sql.connect('example.db')
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS trajectory")
    conn.commit()
    cursor.execute('''
       CREATE TABLE trajectory
         (value float)
    ''')

    for r in result:
        cursor.execute('''
           INSERT INTO trajectory (value)
             VALUES
           (?)''', (r,)
        )
    cursor.close()
    conn.commit()
    conn.close()
    

def consume(temp):
    conn = sql.connect('example.db')
    cursor = conn.cursor()


    cursor.execute("SELECT value FROM trajectory WHERE value < ?", (temp,))

    for row in cursor:
        print(row)

    cursor.execute("SELECT sum(value) FROM trajectory WHERE value<?", (temp,))
    row = cursor.fetchone()

    print("Sum is: ", row[0])

    del cursor
    conn.close()


with_file('input.txt')


consume(100)





