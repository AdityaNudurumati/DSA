'''
3. First Negative in Every Window of Size K (Easy)
Problem Statement

Given an integer array nums and an integer k, for EACH contiguous window of size
k report the FIRST negative number in that window. If a window has no negative
number, report 0.

Example
Input:
nums = [12,-1,-7,8,-15,30,16,28], k = 3

Output:
[-1, -1, -7, -15, -15, 0]
Explanation:
[12,-1,-7]->-1  [-1,-7,8]->-1  [-7,8,-15]->-7
[8,-15,30]->-15 [-15,30,16]->-15 [30,16,28]->0 (none)
'''

from collections import deque

def firstNegativeInWindow(nums, k):

    result = []
    dq = deque()          # indices of negative numbers, in order

    for i in range(len(nums)):

        # drop the front index if it has slid out of the window
        if dq and dq[0] <= i - k:
            dq.popleft()

        # record the current index only if it is negative
        if nums[i] < 0:
            dq.append(i)

        # once the first full window is formed, the front is the answer
        if i >= k - 1:
            result.append(nums[dq[0]] if dq else 0)

    return result


if __name__ == "__main__":
    print(firstNegativeInWindow([12, -1, -7, 8, -15, 30, 16, 28], 3))
    # Expected: [-1, -1, -7, -15, -15, 0]
    print(firstNegativeInWindow([1, 2, 3], 2))          # Expected: [0, 0]
    print(firstNegativeInWindow([-1, -2, -3], 2))        # Expected: [-1, -2]

'''
Pattern
✅ Fixed-Size Sliding Window + Deque (queue of negative indices)

Key Observation
We only need the EARLIEST negative index still inside the window. Keep those
indices in a queue: the front is that first negative. Pop the front when it
leaves the window; append new negative indices at the back. Each index is added
and removed at most once.

| Metric | Value           |
| ------ | --------------- |
| Time   | O(n)            |
| Space  | O(k) (deque)    |

Better Possible?
❌ No. Every element is processed once; output itself is O(n-k+1).
'''
