# Greatest Common Divisor Problem
# Compute the greatest common divisor of two positive integers.
# Input: Two positive integers a and b.
# Output: The greatest common divisor of a and b.

a, b = map(int, input().split())

def gcd(a, b):
    while b:
        a, b = b, a % b
    print(a)

gcd(a, b)