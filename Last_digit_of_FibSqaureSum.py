# Last Digit of the Sum of Squares of Fibonacci Numbers Problem
# Compute the last digit of the sum of squares of the first n Fibonacci numbers.


n = int(input())
lesser_n = n% 60
lesser_nplus = (n + 1) % 60


def fibo(n):
    a, b = 0, 1
    for _ in range(2, n + 1):
        c = a + b
        c = c % 10
        b, a = c, b
    return c


if lesser_n <= 1:
    a = lesser_n
else:
    a = fibo(lesser_n)
if lesser_nplus <= 1:
    b = lesser_nplus
else:
    b = fibo(lesser_nplus)

print((a * b) % 10)