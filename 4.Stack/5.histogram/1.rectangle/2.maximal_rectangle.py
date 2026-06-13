'''
2. Maximal Rectangle (Hard)
Problem Statement

Given a 2D binary matrix filled with '0's and '1's, find the largest rectangle
containing only '1's and return its area.

Example
Input:
matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]

Output:
6
Explanation:
The 2x3 block of '1's in the bottom-right region has area 6.
'''

def largestRectangleArea(heights):
    # Largest Rectangle in Histogram (LC84) reused per row
    stack = []
    max_area = 0
    heights = heights + [0]                 # sentinel flushes the stack
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    return max_area


def maximalRectangle(matrix):

    if not matrix or not matrix[0]:
        return 0

    cols = len(matrix[0])
    heights = [0] * cols                    # running histogram of consecutive 1s
    best = 0

    for row in matrix:
        for j in range(cols):
            # extend the column's bar if cell is '1', else reset to 0
            heights[j] = heights[j] + 1 if row[j] == "1" else 0
        # the tallest rectangle anchored at this row = LC84 on the histogram
        best = max(best, largestRectangleArea(heights))

    return best


if __name__ == "__main__":
    m = [["1", "0", "1", "0", "0"],
         ["1", "0", "1", "1", "1"],
         ["1", "1", "1", "1", "1"],
         ["1", "0", "0", "1", "0"]]
    print(maximalRectangle(m))        # Expected: 6
    print(maximalRectangle([["0"]]))  # Expected: 0

'''
Pattern
✅ Histogram per row — build each row into a histogram and run Largest Rectangle

Key Observation
For each row, heights[j] is the count of consecutive '1's ending at that row in
column j. The best rectangle whose bottom edge is on this row equals the largest
rectangle in that histogram (LC84). Sweeping all rows covers every rectangle.

| Metric | Value     |
| ------ | --------- |
| Time   | O(rows*cols) |
| Space  | O(cols)   |

Better Possible?
❌ No. Every cell is visited once and each histogram is O(cols); O(rows*cols) is optimal.
'''
