'''
2. Trapping Rain Water (Hard) — Monotonic Stack variant
Problem Statement

Given an array height of bar heights (width 1 each), compute how much water is
trapped after raining.

(A two-pointer O(1)-space solution lives in
 ../../1.two_pointer_problems/1.opposite_ends/7.trapping_rain_water.py.
 This file shows the stack approach, which fills water layer by layer.)

Example
Input:
height = [0,1,0,2,1,0,1,3,2,1,2,1]

Output:
6
'''

def trap(height):

    stack = []      # indices with decreasing heights
    water = 0

    for i, h in enumerate(height):

        # current bar can close basins formed by shorter bars below it
        while stack and height[stack[-1]] < h:
            bottom = stack.pop()
            if not stack:
                break                    # no left wall -> water spills out
            left = stack[-1]
            width = i - left - 1
            bounded = min(height[left], h) - height[bottom]
            water += width * bounded

        stack.append(i)

    return water


if __name__ == "__main__":
    print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))   # Expected: 6
    print(trap([4, 2, 0, 3, 2, 5]))                       # Expected: 9

'''
Pattern
✅ Monotonic (decreasing) Stack — fill water in horizontal layers

Key Observation
Each time a taller bar appears, it forms a left+right wall around the popped bottom.
Water added = width * (min(left, right) wall height - bottom height).

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
The two-pointer version achieves the same O(n) time in O(1) space (see cross-ref).
'''
