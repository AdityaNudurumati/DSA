'''
1. Previous Greater Element (Easy)
Problem Statement

You are given an integer array nums.

For each element, find the nearest greater element to its LEFT: the closest value
to the left that is strictly greater than it. If no such element exists, the answer
is -1.

Return an array of the previous greater elements, one per index.

Example
Input:
nums = [10,4,2,20,40,12,30]
Output:
[-1,10,4,-1,-1,40,40]
'''

def previousGreaterElement(nums):
    n = len(nums)
    res = [-1] * n
    stack = []                       # store values, decreasing from bottom to top

    for i, x in enumerate(nums):
        # Pop everything not greater than x; they can never be a previous greater.
        while stack and stack[-1] <= x:
            stack.pop()
        # The remaining top (if any) is the nearest greater element on the left.
        if stack:
            res[i] = stack[-1]
        stack.append(x)

    return res


if __name__ == "__main__":
    print(previousGreaterElement([10, 4, 2, 20, 40, 12, 30]))  # Expected: [-1, 10, 4, -1, -1, 40, 40]


'''
Pattern
✅ Monotonic Stack (decreasing)
Scan left->right keeping a stack whose values decrease toward the top. Before
pushing x, pop all values <= x; whatever remains on top is the nearest greater
element to the left.
| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |
Better Possible?
❌ No. Each element is pushed and popped at most once; O(n) is optimal.
'''
