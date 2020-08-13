# Given an array and an integer K, find the maximum for each and every contiguous subarray of size k.

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
