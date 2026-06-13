'''
2. Non-overlapping Intervals (Medium)
Problem Statement

Given an array of intervals, return the minimum number of intervals you must remove
so that the rest are non-overlapping.

Example
Input:
intervals = [[1,2],[2,3],[3,4],[1,3]]

Output:
1
Explanation:
Remove [1,3] and the rest are non-overlapping.
'''

def eraseOverlapIntervals(intervals):

    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[1])      # greedy: sort by END
    count = 0
    prev_end = intervals[0][1]

    for i in range(1, len(intervals)):
        if intervals[i][0] < prev_end:
            count += 1                       # overlaps -> remove this one
        else:
            prev_end = intervals[i][1]       # keep it; advance the boundary

    return count


if __name__ == "__main__":
    print(eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))  # Expected: 1
    print(eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))           # Expected: 2
    print(eraseOverlapIntervals([[1, 2], [2, 3]]))                   # Expected: 0

'''
Pattern
✅ Greedy Interval Scheduling (sort by end, keep earliest finisher)

Key Observation
Keeping the interval that ends earliest leaves the most room for the rest. Any
interval that starts before the last kept end must be removed.

| Metric | Value      |
| ------ | ---------- |
| Time   | O(n log n) |
| Space  | O(1)       |

Better Possible?
❌ No — sorting is required.
'''
