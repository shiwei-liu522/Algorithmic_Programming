# Least Common Multiple Problem
# Compute the least common multiple of two positive
# integers.
# Input: Two positive integers a and b.
# Output: The least common multiple of a and b.

a, b = map(int, input().split())

def gcd(a, b):
    if b == 0:
        return a
    c = a % b
    return gcd(b, c)

if a > b:
    greatest = gcd(a, b)
else:
    greatest = gcd(b, a)

print(a * b //greatest) #// is floor division