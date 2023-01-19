# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

#Maximum product of two numbers in an array
# #Naive Algorithm
# def max_pairwise_product_naive(arr):
#     max_product = 0
#     for first in range(len(arr)):
#         for second in range(first + 1, len(arr)):
#             max_product = max(max_product, arr[first]*arr[second])
#     return max_product

#Fast Algorithm
def max_pairwise_product_fast(arr):
    first = max(arr)
    arr.remove(first)
    sec = max(arr)
    return first * sec

# #Stress test
# from random import randint
# def max_pairwise_product_StressTest(N,M):
#     while True:
#         n = randint(2,N)
#         A = [None]*n
#         for i in range(n):
#             A[i] = randint(0,M)
#         print(A)
#         result1 = max_pairwise_product_naive(A)
#         result2 = max_pairwise_product_fast(A)
#         if result1==result2:
#             print('OK')
#         else:
#             print('Wrong answer:',result1,result2)
#             return
# max_pairwise_product_StressTest(5,100)

if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(arr))