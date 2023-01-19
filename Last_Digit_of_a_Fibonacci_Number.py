# DigitLast Digit of Fibonacci Number Problem
# Compute the last digit of the n-th Fibonacci number.
# Input: An integer n.
# Output: The last digit of the n-th Fibonacci number.


n = int(input())

if n <= 1:
    print(n)

def last_digit_fibo(n):
    a, b = 0, 1
    for i in range(n - 1):
        c = a + b
        c = c % 10
        b, a = c, b
    print(c)

last_digit_fibo(n)

