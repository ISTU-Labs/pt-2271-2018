
# Divide and Conquer. (Раззделяй и властвуй).

# Quick Sort.

# L=[1,8, 2 ,6,3,0,5,7,8] - > [0,1,2,3,....]
# 1. L1=[1,0] L2=[8,6,3,5,7,8]
# 2. L1->Sorted L1
# 3. L2->Sorted L2
# 4. Sorted L = Sorted L1 + 2 + Sorted L2


def qs(L):
    """Returns sorted L."""

    if (len(L) == 0):
        return []

    X = L.pop()

    L1, L2 = divide(L, X)
    SL1 = qs(L1)
    SL2 = qs(L2)
    return SL1 + [X] + SL2


def divide(I, X):
    L = []
    G = []
    for e in I:
        if e <= X:
            L.append(e)
        else:
            G.append(e)

    return L, G

# Dynamic programming

#


fibc = {}


def fib(N):
    if N == 1:
        return 1
    if N == 2:
        return 1
    if N in fibc:
        return fibc[N]

    M = fib(N-1)+fib(N-2)

    fibc[N] = M

    return M


def fibimp(N):
    a, b = 1, 1
    while N > 1:
        a, b = b, a+b
        N -= 1
    return a


def tst(N):
    f = fib(N)
    g = fibimp(N)
    return f == g, f, g


# Search with backtrack

def p(L):
    if len(L) == 0:
        yield []
        return
    for i in range(len(L)):
        LL = L[:]
        N = LL.pop(i)
        for pp in p(LL):
            yield [N]+pp
