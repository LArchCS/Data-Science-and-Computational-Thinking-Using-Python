def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a+b

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
    
def fib3(n):
    a=0
    b=1
    while n>0:
        a,b=b,a+b
        n-=1
    return b

def fib4(n):
    if n == 0 or n ==1:
        return 1
    else:
        return fib4(n-2) + fib4(n-1)