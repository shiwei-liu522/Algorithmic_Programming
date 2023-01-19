# Maximum Product of Two Sequences Problem
# Find the maximum dot product of two sequences of numbers.
# Input: Two sequences of n positive integers: price1, . . . ,pricen and clicks1, . . . , clicksn.
# Output: The maximum value of price1 · c1 + · · · + pricen· cn,where c1, . . . ,
# cn is a permutation of clicks1, . . . , clicksn.

num = int(input())
prices = list(map(int, input().split()))
clicks = list(map(int, input().split()))
clicks = sorted(clicks, reverse=True)
prices = sorted(prices, reverse=True)
print(sum([price * click for price, click in zip(prices, clicks)]))
