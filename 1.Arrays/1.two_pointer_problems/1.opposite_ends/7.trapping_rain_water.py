'''
7. Trapping Rain Water (Hard)
Problem Statement

Given an array height where each element is the height of a vertical bar of width 1,
compute how much water can be trapped after raining.

Example
Input:
height = [0,1,0,2,1,0,1,3,2,1,2,1]

Output:
6

Explanation:
Water sits in the dips between taller bars.
'''

def trap(height):

    if not height:
        return 0

    left = 0
    right = len(height) - 1

    left_max = height[left]
    right_max = height[right]

    water = 0

    while left < right:

        # The smaller side bounds the water level, so process it.
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            water += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water += right_max - height[right]

    return water


if __name__ == "__main__":
    print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # Expected: 6
    print(trap([4, 2, 0, 3, 2, 5]))                     # Expected: 9

'''
Pattern
✅ Opposite-Ends Two Pointers

Key Observation
Water above a bar = min(maxLeft, maxRight) - height[i].
Move the pointer on the SMALLER side, because that side limits the level —
its trapped water is already fully determined.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No. (Prefix-max arrays also give O(n) but use O(n) space.)
'''
