def fibonacciBFR(n):

    if n <= 1:
        return n

    return fibonacciBFR(n - 1) + fibonacciBFR(n - 2)
    
def fibonacciTD(n, c):
    
    if n in c:
        return c[n]
    
    if n <= 1:
        res = n
        
    else:
        res = fibonacciTD(n - 1, c) + fibonacciTD(n - 2, c)
        
    c[n] = res
    
    return res

def fibonacciBU(n):

    fib = [0]*(n + 1)
    fib[0] = 0
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[-1]
    
def fibonacciNaive(n):
    if n <= 1:
        return n
    nm2 = 0
    nm1 = 1
    ns = nm2 + nm1
    ni = 2
    while ni != n:
        nm2 = nm1
        nm1 = ns
        ns = nm2 + nm1
        ni += 1
    return ns
        
    
print(fibonacciBFR(7))

print(fibonacciTD(100, {}))

print(fibonacciBU(1000))

print(fibonacciNaive(1000))