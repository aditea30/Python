#sum of given number ex(5+4+3+2+1)
def recurs(n):
    if(n==1):
        return 1
    else:
        return n+recurs(n-1)
print(recurs(4))

#factorail (ex 5=5x4x3x2x1)
def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)
print(fact(3))

#fib(using recursion base condition)
def fib(n):
    if n<=1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(5))

#fibonaci in series
def fibb(n):
    a=0
    b=1
    
    for i in range(n):
        print(a)
        a,b=b,b+a
print(fibb(5))

