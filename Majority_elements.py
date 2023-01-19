# Majority Element Problem
# Check whether a given sequence of numbers contains an element that appears more than half of the times.
# Input: A sequence of n integers.
# Output: 1, if there is an element that is repeated more than n/2 times, and 0 otherwise.

n = int(input())
seq = list(map(int, input().split()))


def divide(seq, l, r):
    if l+1==r:
        return seq[l]
    elif l+2==r:
        return seq[l]
    m = (l+r)//2
    left = divide(seq, l, m)
    right = divide(seq, m, r)

    c1, c2 = 0, 0
    for i in seq[l:r]:
        if i == left:
            c1+=1
        elif i == right:
            c2+=1
    if c1>(r-l)//2 and left != -1:
        return left
    elif c2>(r-l)//2 and right != -1:
        return right
    else:
        return -1

print(int(divide(seq, 0, n) != -1))