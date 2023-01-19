# Maximum Amount of Gold Problem
# Given a set of gold bars of various weights and a backpack that can hold at most W pounds, place as much gold as possible into the backpack.
# Input: A set of n gold bars of integer weights w1, . . . ,wn and a backpack that can hold at most W pounds.
# Output: A subset of gold bars of maximum total weight not exceeding W.

import sys

def optimal_weight(W, w, n):
    values = [[0 for i in range(W + 1)] for j in range(n + 1)]
    for j in range(1, n+1):
        for i in range(1, W + 1):
            values[j][i] = values[j-1][i]
            if w[j-1] <= i:
                val = values[j-1][i-w[j-1]] + w[j-1]
                if val > values[j][i] and val <= i:
                    values[j][i] = val
    return values[n][W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w, n))
