'''
1. Sliding Window Maximum (Hard)
Problem Statement

Given an integer array nums and a window size k, return a list of the maximum of
each contiguous window of size k as it slides from left to right.

Example
Input:
nums = [1,3,-1,-3,5,3,6,7], k = 3

Output:
[3,3,5,5,6,7]
'''

from collections import deque

def maxSlidingWindow(nums, k):

    dq = deque()        # holds indices; their nums values are decreasing
    result = []

    for i, x in enumerate(nums):

        # drop the front index if it has slid out of the window
        if dq and dq[0] <= i - k:
            dq.popleft()

        # drop smaller values from the back: they can never be the max now
        while dq and nums[dq[-1]] < x:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])   # front is always the window max

    return result


if __name__ == "__main__":
    print(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))  # Expected: [3, 3, 5, 5, 6, 7]
    print(maxSlidingWindow([1], 1))                          # Expected: [1]

'''
Pattern
✅ Monotonic Deque (decreasing) sliding window

Key Observation
A smaller element with a larger element to its right is useless — it can never be
a future maximum. Keeping the deque decreasing means the front is always the max.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  | (each index pushed and popped at most once)
| Space  | O(k)  |

Better Possible?
❌ No. A heap would be O(n log k).
'''
