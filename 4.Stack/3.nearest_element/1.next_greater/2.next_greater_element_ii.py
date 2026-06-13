'''
2. Next Greater Element II (Medium)
Problem Statement

You are given a circular integer array nums (the last element is followed by the
first element again).

For each element, find its next greater element: the first strictly greater value
encountered when scanning forward, wrapping around the end of the array. If no such
element exists, the answer is -1.

Return an array of the next greater elements, one per index.

Example
Input:
nums = [1,2,1]
Output:
[2,-1,2]
'''

def nextGreaterElements(nums):
    n = len(nums)
    res = [-1] * n
    stack = []                       # store indices, decreasing by value

    # Iterate twice over the array to emulate the circular wrap-around.
    for i in range(2 * n):
        idx = i % n
        # Resolve every index whose value is smaller than the current value.
        while stack and nums[stack[-1]] < nums[idx]:
            res[stack.pop()] = nums[idx]
        # Only push real indices during the first pass; the second pass just resolves.
        if i < n:
            stack.append(idx)

    return res


if __name__ == "__main__":
    print(nextGreaterElements([1, 2, 1]))          # Expected: [2, -1, 2]
    print(nextGreaterElements([1, 2, 3, 4, 3]))    # Expected: [2, 3, 4, -1, 4]


'''
Pattern
✅ Monotonic Stack (decreasing) over a doubled scan
A circular array is handled by walking indices i in [0, 2n) and using i % n. The
first pass pushes indices; both passes resolve waiting indices, so wrap-around
greaters are found without physically duplicating the array.
| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |
Better Possible?
❌ No. Each index is pushed and popped at most once; O(n) is optimal.
'''
