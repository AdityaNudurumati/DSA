'''
1. Previous Smaller Element (Easy)
Problem Statement

You are given an integer array nums.

For each element, find the nearest smaller element to its LEFT: the closest value
to the left that is strictly smaller than it. If no such element exists, the answer
is -1.

Return an array of the previous smaller elements, one per index.

Example
Input:
nums = [4,5,2,10,8]
Output:
[-1,4,-1,2,2]
'''

def previousSmallerElement(nums):
    n = len(nums)
    res = [-1] * n
    stack = []                       # store values, increasing from bottom to top

    for i, x in enumerate(nums):
        # Pop everything not smaller than x; they can never be a previous smaller.
        while stack and stack[-1] >= x:
            stack.pop()
        # The remaining top (if any) is the nearest smaller element on the left.
        if stack:
            res[i] = stack[-1]
        stack.append(x)

    return res


if __name__ == "__main__":
    print(previousSmallerElement([4, 5, 2, 10, 8]))   # Expected: [-1, 4, -1, 2, 2]


'''
Pattern
✅ Monotonic Stack (increasing)
Scan left->right keeping a stack whose values increase toward the top. Before
pushing x, pop all values >= x; whatever remains on top is the nearest smaller
element to the left.
| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |
Better Possible?
❌ No. Each element is pushed and popped at most once; O(n) is optimal.
'''
