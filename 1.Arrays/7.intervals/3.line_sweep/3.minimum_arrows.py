'''
3. Minimum Number of Arrows to Burst Balloons (Medium)
Problem Statement

Each balloon spans [start, end] on the x-axis. An arrow shot at x bursts every
balloon whose span contains x. Return the minimum number of arrows to burst all.

Example
Input:
points = [[10,16],[2,8],[1,6],[7,12]]

Output:
2
'''

def findMinArrowShots(points):

    if not points:
        return 0

    points.sort(key=lambda x: x[1])     # sort by END
    arrows = 1
    arrow_x = points[0][1]              # shoot at the first balloon's end

    for s, e in points[1:]:
        if s > arrow_x:                # current arrow misses -> need a new one
            arrows += 1
            arrow_x = e

    return arrows


if __name__ == "__main__":
    print(findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))   # Expected: 2
    print(findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]))      # Expected: 4
    print(findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]))      # Expected: 2

'''
Pattern
✅ Greedy Interval Scheduling (sort by end, shoot at earliest end)

Key Observation
Shooting at the earliest end bursts every balloon overlapping that point. Only when
a balloon starts after the current arrow's x do we need another arrow. Mirror image
of Non-overlapping Intervals.

| Metric | Value      |
| ------ | ---------- |
| Time   | O(n log n) |
| Space  | O(1)       |

Better Possible?
❌ No — sorting is required.
'''
