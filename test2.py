# Given an array arr[] of size N and a number K, the task is to find the length
# of the smallest subsequence such that the sum of the subsequence is greater
# than or equal to number K.

# Algorithm:
# 1)Traverse input array and insert every array element into priority queue.
# 2)Initialize variables that holds the sum of picked element from priority queue and the variable to get the count of picked element from priority queue to 0.
# 3)Pop the elements out from the priority queue untill the priority queue is not empty.

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
