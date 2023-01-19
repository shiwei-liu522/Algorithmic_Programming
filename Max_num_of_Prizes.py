# Distinct Summands Problem
# Represent a positive integer as the sum of the maximum number of pairwise distinct positive integers.
# Input: A positive integer n.
# Output: The maximum k such that n can be represented as the sum a1 + · · · + ak of k distinct positive integers.

n = int(input())
summands = []
for i in range(1, n + 1):
    if n - i > i:
        summands.append(i)
        n -= i
    else:
        summands.append(n)
        break
print(len(summands))
print(' '.join(map(str, summands)))


