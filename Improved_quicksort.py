# Speeding-up RandomizedQuickSort Problem
# Sort a given sequence of numbers (that may contain duplicates) using a modification of RandomizedQuickSort that works in
# O(nlogn) expected time.
# Input: An integer array with n elements that may contain duplicates.
# Output: Sorted array (generated using a modification of RandomizedQuickSort) that works in O(nlogn) expected time.

import random

def randomized_quick_sort(A, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    A[l], A[k] = A[k], A[l]
    #use partition
    m1, m2 = partition(A, l, r)
    randomized_quick_sort(A, l, m1 - 1)
    randomized_quick_sort(A, m2 + 1, r)


def partition(A, l, r):
    x = A[l]
    j = l
    m1 = l
    m2 = r
    while j <= m2:
        if A[j] < x:
            A[j], A[m1] = A[m1], A[j]
            m1 += 1
            j += 1
        elif A[j] > x:
            A[j], A[m2] = A[m2], A[j]
            m2 -= 1
        else:
            j += 1
    return m1, m2


n = int(input())
A = [int(i) for i in input().split()]

randomized_quick_sort(A, 0, n - 1)
for x in A:
    print(x, end=' ')

