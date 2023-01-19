# Money Change Problem
# Compute the minimum number of coins needed
# to change the given value into coins with denominations 1, 5, and 10.
# Input: An integer money.
# Output: The minimum number of coins with denominations 1, 5,and 10 that changes money.

money = int(input())

count = 0
for i in [10, 5, 1]:
    if money >= i:
        num = money // i
        count += num
        money = money % i
        if money == 0:
            print(count)
