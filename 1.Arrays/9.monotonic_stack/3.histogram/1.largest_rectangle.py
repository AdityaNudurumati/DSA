'''
1. Largest Rectangle in Histogram (Hard)
Problem Statement

Given an array heights representing bar heights of a histogram (each width 1),
return the area of the largest rectangle that fits inside.

Example
Input:
heights = [2,1,5,6,2,3]

Output:
10
Explanation:
Bars [5,6] form a 2-wide, 5-tall rectangle = 10.
'''

def largestRectangleArea(heights):

    stack = []                  # indices with increasing heights
    max_area = 0
    heights = heights + [0]     # sentinel 0 flushes the stack at the end

    for i, h in enumerate(heights):
        # current bar ends every taller bar's rectangle
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            # width spans from the previous shorter bar to i
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    return max_area


if __name__ == "__main__":
    print(largestRectangleArea([2, 1, 5, 6, 2, 3]))   # Expected: 10
    print(largestRectangleArea([2, 4]))                # Expected: 4

'''
Pattern
✅ Monotonic (increasing) Stack — width via previous-smaller

Key Observation
A bar's rectangle extends until a shorter bar appears on either side. When the stack
pops a bar, the popped height's width is bounded by the new top and the current i.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No.
'''
