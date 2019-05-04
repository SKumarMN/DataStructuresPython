def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n=5
print("Fib of {} is {}".format(n,fibonacci(n)))



def fib_dp(n,lookup):
    if n == 0:
        lookup[n] =0
    elif n == 1:
        lookup[n] =1
    else:
        lookup[n] = fib_dp(n-1,lookup) + fib_dp(n-2,lookup) 
    
    return lookup[n]


lookup = [None] * (n +1)
print(fib_dp(n,lookup))

