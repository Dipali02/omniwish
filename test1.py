# Given an array and an integer K, find the maximum for each and every contiguous subarray of size k.

# Algorithm:
# 1)Create a nested loop, the outer loop from starting index to n – k th elements. The inner loop will run for k iterations.
# 2)Create a variable to store the maximum of k elements traversed by the inner loop.
# 3)Find the maximum of k elements traversed by the inner loop.
# 4)Print the maximum element in every iteration of outer loop.

def Max(arr, n, k):
    max = 0

    for i in range(n - k + 1):
        max = arr[i]
        for j in range(1, k):
            if arr[i + j] > max:
                max = arr[i + j]
        print(str(max) + " ", end = "")

if __name__=="__main__":
    arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
    n = len(arr)
    k = 3
    Max(arr, n, k)
