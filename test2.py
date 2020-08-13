# Given an array arr[] of size N and a number K, the task is to find the length
# of the smallest subsequence such that the sum of the subsequence is greater
# than or equal to number K.

def lengthOfSmallestSubsequence(K, v):
    pq = []

    for i in v:
        pq.append(i)
    pq.sort()

    sum = 0
    count = 0

    while (len(pq) > 0 and sum < K):
        sum = sum + pq[-1]
        del pq[-1]
        count = count + 1

    if (sum < K):
        return -1
    return count

v = [2, 3, 1, 5,6, 3, 7, 9,14, 10, 2, 5]
K = 35

print(lengthOfSmallestSubsequence(K, v))
