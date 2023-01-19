# Number of Inversions Problem
# Compute the number of inversions in a sequence of integers.
# Input: A sequence of n integers a1, . . . ,an.
# Output: The number of inversions in the sequence, i.e., the number of indices i < j such that ai > aj .

def merge(left, right):
    global tot_count
    count = 0
    sorted_arr = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
            count += len(left) - i
    sorted_arr += left[i:]
    sorted_arr += right[j:]
    return sorted_arr, count


def mergesort(arr):
    global tot_count
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    sorted_arr, count = merge(left, right)
    tot_count += count
    return sorted_arr

tot_count = 0
n = int(input())
A = [int(i) for i in input().split()]
mergesort(A)
print(tot_count)
