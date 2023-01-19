# Money Change Again Problem
# Compute the minimum number of coins needed to change the given value into coins with denominations 1, 3, and 4.
# Input: An integer money.
# Output: The minimum number of coins with denominations 1, 3, and 4 that changes money.

import math
n=int(input())
denominations=[1,3,4]
def money_change(n):
    min_num_coins=[0]
    for m in range(1,n+1):
        min_num_coins.append(math.inf)
        for i in range(len(denominations)):
            if m>=denominations[i]:
                num_coins=min_num_coins[m-denominations[i]]+1
                if num_coins<min_num_coins[m]:
                    min_num_coins[m]=num_coins
    return min_num_coins[n]
print(money_change(n))
