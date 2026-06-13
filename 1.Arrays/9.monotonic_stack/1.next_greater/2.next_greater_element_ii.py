'''
2. Next Greater Element II (Medium)
Problem Statement

Given a CIRCULAR integer array nums, return the next greater element for each
position. The next greater of x is the first greater value when scanning to the
right, wrapping around. If none exists, use -1.

Example
Input:
nums = [1,2,1]

Output:
[2,-1,2]
'''

def nextGreaterElements(nums):

    n = len(nums)
    result = [-1] * n
    stack = []                      # indices, values decreasing

    # iterate twice to simulate the circular wrap
    for i in range(2 * n):
        x = nums[i % n]
        while stack and nums[stack[-1]] < x:
            result[stack.pop()] = x
        if i < n:                   # only push real indices on the first pass
            stack.append(i)

    return result


if __name__ == "__main__":
    print(nextGreaterElements([1, 2, 1]))         # Expected: [2, -1, 2]
    print(nextGreaterElements([1, 2, 3, 4, 3]))   # Expected: [2, 3, 4, -1, 4]

'''
Pattern
✅ Monotonic Stack over a doubled (circular) index range

Key Observation
Walking indices 0..2n-1 with i % n revisits the front, resolving wrap-around next
greaters. Push only during the first pass so each index gets one answer.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No.
'''
