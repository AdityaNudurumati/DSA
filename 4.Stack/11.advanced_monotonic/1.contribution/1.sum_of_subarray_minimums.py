'''
1. Sum of Subarray Minimums (Medium)
Problem Statement

Given an array arr of integers, find the sum of min(b) for every (contiguous)
subarray b of arr. Since the answer may be large, return it modulo 1e9 + 7.

Example
Input:
arr = [3,1,2,4]

Output:
17

Explanation:
Subarrays and their minimums:
[3]->3, [1]->1, [2]->2, [4]->4, [3,1]->1, [1,2]->1, [2,4]->2,
[3,1,2]->1, [1,2,4]->1, [3,1,2,4]->1. Sum = 17.
'''

MOD = 10**9 + 7


def sumSubarrayMins(arr):

    n = len(arr)

    # For each i, count subarrays where arr[i] is the minimum:
    #   left  = #elements to the left  (incl. i) where arr[i] is strictly the min
    #   right = #elements to the right where arr[i] stays the min
    # Use STRICT '>' on the left and NON-STRICT '>=' on the right to break ties
    # consistently (avoids double counting equal values).

    prev_smaller = [-1] * n   # index of previous element strictly smaller
    next_smaller = [n] * n    # index of next element smaller-or-equal

    stack = []
    for i in range(n):
        # pop while stack top is >= current -> current is the new smaller boundary
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        prev_smaller[i] = stack[-1] if stack else -1
        stack.append(i)

    stack = []
    for i in range(n - 1, -1, -1):
        # pop while stack top is strictly > current
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        next_smaller[i] = stack[-1] if stack else n
        stack.append(i)

    total = 0
    for i in range(n):
        left = i - prev_smaller[i]
        right = next_smaller[i] - i
        total += arr[i] * left * right
        total %= MOD

    return total


if __name__ == "__main__":
    print(sumSubarrayMins([3, 1, 2, 4]))          # Expected: 17
    print(sumSubarrayMins([11, 81, 94, 43, 3]))   # Expected: 444

'''
Pattern
✅ Advanced Monotonic Stack — Contribution Technique

Key Observation
Instead of enumerating subarrays, count how many subarrays each element is the
minimum of: (i - prev_smaller) * (next_smaller - i). Multiply by the value and
sum. Strict/non-strict comparisons on opposite sides handle duplicates exactly
once.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No. Every element must be visited; O(n) time is optimal.
'''
