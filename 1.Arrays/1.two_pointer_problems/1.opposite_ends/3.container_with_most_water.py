'''
3. Container With Most Water (Medium)
Problem Statement

You are given an array height.

Each element represents the height of a vertical line.

Find two lines that together with the x-axis form a container that can hold the maximum amount of water.

Return the maximum water area.

Example
Input:
height = [1,8,6,2,5,4,8,3,7]

Output:
49
Explanation:
Choose heights 8 and 7

Width = 7
Height = min(8,7) = 7

Area = 7 * 7 = 49
'''

def maxArea(height):

    left = 0
    right = len(height) - 1

    answer = 0

    while left < right:

        area = (right - left) * min(height[left], height[right])

        answer = max(answer, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return answer


if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(maxArea(height))  # Expected: 49

'''
Pattern
✅ Greedy Two Pointers

Key Observation
Area:
width * min(height1,height2)
Move smaller height.
Moving larger height never helps.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No

Optimal solution.
'''