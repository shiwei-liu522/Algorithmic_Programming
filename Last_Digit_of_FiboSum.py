# Last Digit of the Sum of Fibonacci Numbers Problem
# Compute the last digit of F0 + F1 + · · · + Fn.
# Input: An integer n.
# Output: The last digit of F0 + F1 + · · · + Fn.

n = int(input())

if n<=1:
    print(n)

lesser = (n+2) % 60

if lesser==1:
    print(0)

elif lesser==0:
    print(9)

def fibo(n):
    a,b = 0,1
    for i in range(2,lesser+1):
        c = a+b
        c = c%10
        b, a = c, b
    if c!=0:
        print(c-1)
    else:
        print(9)
fibo(lesser)