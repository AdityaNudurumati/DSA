'''
1. Trapping Rain Water via Monotonic Stack (Hard)
Problem Statement

Given an array height where each element is the height of a vertical bar of
width 1, compute how much water can be trapped after raining. Solve it using a
monotonic (decreasing) stack.

Example
Input:
height = [0,1,0,2,1,0,1,3,2,1,2,1]

Output:
6

Explanation:
Water fills the dips between taller bars layer by layer.
'''


def trap(height):

    # Maintain a stack of bar indices with DECREASING heights.
    # When the current bar is taller than the bar on top of the stack, that
    # popped bar is a "valley bottom" bounded on both sides -> trap a horizontal
    # layer of water spanning from the new left boundary to the current bar.

    stack = []      # indices, heights non-increasing
    water = 0

    for i, h in enumerate(height):

        # current bar can hold water on top of shorter bars below it
        while stack and height[stack[-1]] < h:
            bottom = stack.pop()        # the valley floor we fill above

            if not stack:
                break                   # no left wall -> water spills out

            left = stack[-1]            # left boundary index
            width = i - left - 1        # bars strictly between the walls
            bounded_h = min(height[left], h) - height[bottom]
            water += width * bounded_h

        stack.append(i)

    return water


if __name__ == "__main__":
    print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # Expected: 6
    print(trap([4, 2, 0, 3, 2, 5]))                     # Expected: 9

'''
Pattern
✅ Advanced Monotonic Stack — Rain Water Variant

Key Observation
A decreasing stack holds potential left walls. When a taller bar arrives it
closes the valleys above shorter bars: pop each valley floor and add the
horizontal water layer it bounds, using min(leftWall, rightWall) - floor as the
height. Each index is pushed and popped once.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
✅ Yes on space — two-pointer scan does the same in O(1) space; the stack version
is O(n) space but computes water layer-by-layer, useful for some variants.
'''
