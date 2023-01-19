# Maximizing the Value of the Loot Problem
# Find the maximal value of items that fit into the backpack.
# Input: The capacity of a backpack W as well as the weights
# (w1, . . . ,wn) and costs (c1, . . . , cn) of n different compounds.
# Output: The maximum total value of fractions of items that fit into the backpack of the given capacity: i.e.,
# the maximum value of c1·f1+· · ·+cn·fn such that w1 · f1 +· · ·+wn · fn ≤W
# and 0 ≤ fi ≤ 1 for all i (fi is the fraction of the i-th item taken to the backpack).

n, W = map(int, input().split())
bag = []

# if W == 0:
#     print(0)
#     quit()
#
# #if the overall capacity of the bag is 0, then the value of the loot is 0, so print(0) and quit()

for i in range(n):
    v, w = map(int, input().split())
    if v == 0:
        continue
    bag.append((v, w))

bag.sort(key = lambda x: x[0]/x[1], reverse = True)

total_value = 0

for v,w in bag:
    if W==0:
        print(total_value)
        quit()
    weight = min(w, W)
    total_value += weight * v / w
    W -= weight

print(total_value)