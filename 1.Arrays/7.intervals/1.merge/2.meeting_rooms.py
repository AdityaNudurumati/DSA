'''
2. Meeting Rooms (Easy)
Problem Statement

Given an array of meeting time intervals, determine whether a person could attend
ALL meetings (i.e. no two meetings overlap).

Example
Input:
intervals = [[0,30],[5,10],[15,20]]

Output:
False
Explanation:
[0,30] overlaps both [5,10] and [15,20].
'''

def canAttendMeetings(intervals):

    intervals.sort(key=lambda x: x[0])      # sort by start

    for i in range(1, len(intervals)):
        # a meeting starts before the previous one ends -> conflict
        if intervals[i][0] < intervals[i - 1][1]:
            return False

    return True


if __name__ == "__main__":
    print(canAttendMeetings([[0, 30], [5, 10], [15, 20]]))  # Expected: False
    print(canAttendMeetings([[7, 10], [2, 4]]))              # Expected: True

'''
Pattern
✅ Sort by start, check adjacent overlap

| Metric | Value      |
| ------ | ---------- |
| Time   | O(n log n) |
| Space  | O(1)       |

Better Possible?
❌ No — sorting is required to compare neighbors.
'''
