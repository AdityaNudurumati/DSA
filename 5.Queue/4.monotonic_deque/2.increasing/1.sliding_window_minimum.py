'''
1. Sliding Window Minimum (Medium)
Problem Statement

Given an integer array nums and a window size k, return a list of the minimum of
each contiguous window of size k as it slides from left to right.

Example
Input:
nums = [1,3,-1,-3,5,3,6,7], k = 3

Output:
[-1,-3,-3,-3,3,3]
'''

from collections import deque

def minSlidingWindow(nums, k):

    dq = deque()        # holds indices; their nums values are increasing
    result = []

    for i, x in enumerate(nums):

        # drop the front index if it has slid out of the window
        if dq and dq[0] <= i - k:
            dq.popleft()

        # drop larger values from the back: they can never be the min now
        while dq and nums[dq[-1]] > x:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])   # front is always the window min

    return result


if __name__ == "__main__":
    print(minSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))  # Expected: [-1, -3, -3, -3, 3, 3]
    print(minSlidingWindow([1], 1))                          # Expected: [1]

'''
Pattern
✅ Monotonic Deque (increasing) sliding window

Key Observation
A larger element with a smaller element to its right is useless — it can never be
a future minimum. Keeping the deque increasing means the front is always the min.
This is the mirror image of Sliding Window Maximum (flip the comparison).

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  | (each index pushed and popped at most once)
| Space  | O(k)  |

Better Possible?
❌ No. A heap would be O(n log k).
'''
