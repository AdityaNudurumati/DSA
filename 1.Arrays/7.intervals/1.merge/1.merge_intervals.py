'''
1. Merge Intervals (Medium)
Problem Statement

Given an array of intervals where intervals[i] = [start, end], merge all overlapping
intervals and return the non-overlapping intervals that cover all the input.

Example
Input:
intervals = [[1,3],[2,6],[8,10],[15,18]]

Output:
[[1,6],[8,10],[15,18]]
'''

def merge(intervals):

    intervals.sort(key=lambda x: x[0])      # sort by start
    merged = []

    for s, e in intervals:
        # overlaps the last kept interval -> extend it
        if merged and s <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], e)
        else:
            merged.append([s, e])

    return merged


if __name__ == "__main__":
    print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))  # Expected: [[1,6],[8,10],[15,18]]
    print(merge([[1, 4], [4, 5]]))                       # Expected: [[1,5]]

'''
Pattern
✅ Sort by start, then sweep + merge

Key Observation
After sorting by start, an interval overlaps the previous merged one iff its start
<= that interval's end. Merge by extending the end.

| Metric | Value      |
| ------ | ---------- |
| Time   | O(n log n) | (sort dominates)
| Space  | O(n)       |

Better Possible?
❌ No — sorting is required.
'''
