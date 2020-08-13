# omniwish

Given an array and an integer K, find the maximum for each and every contiguous subarray of size k.
Algorithm:
Create a nested loop, the outer loop from starting index to n – k th elements. The inner loop will run for k iterations.
Create a variable to store the maximum of k elements traversed by the inner loop.
Find the maximum of k elements traversed by the inner loop.
Print the maximum element in every iteration of outer loop



Given an array arr[] of size N and a number K, the task is to find the length of the smallest subsequence such that the sum of the subsequence is greater than or equal to number K.
Algorithm:
Traverse input array and insert every array element into priority queue.
Initialize variables that holds the sum of picked element from priority queue and the variable to get the count of picked element from priority queue to 0
Pop the elements out from the priority queue untill the priority queue is not empty
