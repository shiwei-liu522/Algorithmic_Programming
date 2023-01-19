#Fibonacci Number
# Fibonacci Number Problem
# Compute the n-th Fibonacci number.
    # Input: An integer n.
    # Output: n-th Fibonacci number.

n = int(input())

if n <= 1:
    print(n)

def fibo(n):
    a, b = 0, 1
    for i in range(n - 1):
        c = a + b
        b, a = c, b
    print(c)

fibo(n)
