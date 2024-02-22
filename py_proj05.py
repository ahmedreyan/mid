#FUNCTION TO CREATE FIBONACCI SERIES
def fibonacci(n):
    a, b= 0,1
    fib_series=[]
    for i in range(n):
        fib_series.append(a)
        a,b = b, a+b
    return fib_series
n=5
fib = fibonacci(n)
print(fib)    