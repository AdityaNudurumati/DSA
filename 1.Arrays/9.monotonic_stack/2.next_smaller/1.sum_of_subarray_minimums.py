'''
1. Sum of Subarray Minimums (Medium)
Problem Statement

Given an array arr, return the sum of min(b) over every contiguous subarray b.
Since the answer can be large, return it modulo 1e9 + 7.

Example
Input:
arr = [3,1,2,4]

Output:
17
Explanation:
mins of all subarrays sum to 17.
'''

MOD = 10**9 + 7

def sumSubarrayMins(arr):

    n = len(arr)
    prev_less = [-1] * n        # index of previous STRICTLY-smaller element
    next_less = [n] * n         # index of next smaller-OR-EQUAL element

    # asymmetric strict/non-strict bounds avoid double-counting equal values
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        prev_less[i] = stack[-1] if stack else -1
        stack.append(i)

    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        next_less[i] = stack[-1] if stack else n
        stack.append(i)

    total = 0
    for i in range(n):
        # arr[i] is the min of (left choices) * (right choices) subarrays
        left = i - prev_less[i]
        right = next_less[i] - i
        total += arr[i] * left * right

    return total % MOD


if __name__ == "__main__":
    print(sumSubarrayMins([3, 1, 2, 4]))           # Expected: 17
    print(sumSubarrayMins([11, 81, 94, 43, 3]))    # Expected: 444

'''
Pattern
✅ Monotonic Stack — contribution via previous/next smaller

Key Observation
Each element is the minimum of (distance to previous smaller) * (distance to next
smaller) subarrays. Sum arr[i] * left * right. Use strict on one side, non-strict on
the other to count each subarray exactly once.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No. (Brute force is O(n²) or worse.)
'''
