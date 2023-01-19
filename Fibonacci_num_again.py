# Huge Fibonacci Number Problem
# Compute the n-th Fibonacci number modulo m.
# Input: Integers n and m.
# Output: n-th Fibonacci number modulo m.

import sys

def fib_mod(n, m):
    mod_seq = []
    mod_seq.append(0)
    mod_seq.append(1)
    mod_seq.append(1)
    p = 2
    while not(mod_seq[p-1] == 0 and mod_seq[p] == 1):
        mod_seq.append((mod_seq[p] + mod_seq[p-1]) % m)
        p = p + 1
    l = n % (p-1)
    return (mod_seq[l])


if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    if (m >= 2 and n>= 1 and m <= 100000 and n <= (10**18)):
        print(fib_mod(n, m))