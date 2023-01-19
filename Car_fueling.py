# Car Fueling Problem
# Compute the minimum number of gas tank refills to get from one city to another.
# Input: Integers d and m, as well as a sequence of integers stop1 < stop2 < · · · < stopn.
# Output: The minimum number of refills to get from one city to another
# if a car can travel at most m miles on a full tank. The distance between the cities is d miles and there are gas stations at distances
# stop1,stop2, . . . ,stopn along the way.We assume that a car starts with a full tank.


# Input format. The first line contains an integer d. The second line contains an integer m. The third line specifies an integer n. Finally, the last line contains integers stop1,stop2, . . . ,stopn.
# Output format. The minimum number of refills needed. If it is not possible to reach the destination, output −1.
# Constraints. 1 ≤ d ≤ 105. 1 ≤ m ≤ 400. 1 ≤ n ≤ 300. 0 < stop1 < stop2 < · · · < stopn < d.


d,  m, n = int(input()), int(input()), int(input())
stops = list(map(int, input().split()))

def car_fueling(d, m, n, stops):
    stops.insert(0, 0)
    stops.append(d)
    num_refills, current_refill = 0, 0
    while current_refill <= n:
        last_refill = current_refill
        while current_refill <= n and stops[current_refill + 1] - stops[last_refill] <= m:
            current_refill += 1
        if current_refill == last_refill:
            return -1
        if current_refill <= n:
            num_refills += 1
    return num_refills

print(car_fueling(d, m, n, stops))