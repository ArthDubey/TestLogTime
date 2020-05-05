import random
import time
def matmul(m1,m2):
    a=((m1[0][0]*m2[0][0])+(m1[0][1]*m2[1][0]))%1000007
    b=((m1[0][0]*m2[0][1])+(m1[0][1]*m2[1][1]))%1000007
    c=((m1[1][0]*m2[0][0])+(m1[1][1]*m2[1][0]))%1000007
    d=((m1[1][0]*m2[0][1])+(m1[1][1]*m2[1][1]))%1000007
    return [[a,b],[c,d]]

mymat=[[1,1],[1,0]]
def fib(n):
    if n==1:
        return mymat
    if n==0:
        return [[1,0],[0,1]]
    x=fib(n//2)
    if n%2==0:
        return matmul(x,x)
    else:
        y=matmul(x,x)
        return matmul(y,mymat)
def myfib(n):
    z=fib(n)
    return z[0][1]


def realfib(n):
    n0=0
    n1=1
    n2=1
    for i in range(1,n+1):
        n2,n1,n0=(n2+n1)%1000007,n2,n1
    return n0


tests=int(input("Please enter the upper limit of tests: "))
i=1
while i<=tests:
    rx=time.time()
    realfib(i)
    ry=time.time()
    logx=time.time()
    myfib(i)
    logy=time.time()
    print("Fibonacci of:",i,"\tTime taken by O(n):",ry-rx,"seconds.","\tTime taken by O(Logn):",logy-logx,"seconds.")
    i*=10
