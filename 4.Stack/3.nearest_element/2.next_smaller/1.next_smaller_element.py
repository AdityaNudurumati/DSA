'''
1. Next Smaller Element (Easy)
Problem Statement

You are given an integer array nums.

For each element, find the next strictly smaller element to its right: the first
value to the right that is smaller than it. If no such element exists, the answer
is -1.

Return an array of the next smaller elements, one per index.

Example
Input:
nums = [4,8,5,2,25]
Output:
[2,5,2,-1,-1]
'''

def nextSmallerElement(nums):
    n = len(nums)
    res = [-1] * n
    stack = []                       # store indices, increasing by value

    for i, x in enumerate(nums):
        # x is the next smaller element for every larger value waiting on the stack.
        while stack and nums[stack[-1]] > x:
            res[stack.pop()] = x
        stack.append(i)

    # Indices left on the stack have no smaller element to their right (stay -1).
    return res


if __name__ == "__main__":
    print(nextSmallerElement([4, 8, 5, 2, 25]))   # Expected: [2, 5, 2, -1, -1]


'''
Pattern
✅ Monotonic Stack (increasing)
Scan left->right with an increasing stack of indices. When a smaller value arrives
it is the answer for all larger indices still waiting, which we pop and fill.
| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |
Better Possible?
❌ No. Each index is pushed and popped once; O(n) is optimal.
'''
