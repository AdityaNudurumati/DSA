'''
1. Insert Interval (Medium)
Problem Statement

Given a list of non-overlapping intervals sorted by start, insert a new interval,
merging if necessary, and return the result still sorted and non-overlapping.

Example
Input:
intervals = [[1,3],[6,9]], newInterval = [2,5]

Output:
[[1,5],[6,9]]
'''

def insert(intervals, newInterval):

    result = []
    i, n = 0, len(intervals)

    # 1) intervals that end before the new one starts -> keep as is
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    # 2) intervals that overlap the new one -> absorb into newInterval
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    result.append(newInterval)

    # 3) the rest -> keep as is
    while i < n:
        result.append(intervals[i])
        i += 1

    return result


if __name__ == "__main__":
    print(insert([[1, 3], [6, 9]], [2, 5]))
    # Expected: [[1, 5], [6, 9]]
    print(insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
    # Expected: [[1, 2], [3, 10], [12, 16]]

'''
Pattern
✅ Three-phase scan (before / overlapping / after)

Key Observation
Because the input is already sorted and non-overlapping, a single linear pass in
three phases inserts and merges without re-sorting.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No.
'''
