'''
1. Meeting Rooms II (Medium)
Problem Statement

Given an array of meeting time intervals, return the minimum number of conference
rooms required (the maximum number of meetings happening at the same time).

Example
Input:
intervals = [[0,30],[5,10],[15,20]]

Output:
2
'''

def minMeetingRooms(intervals):

    if not intervals:
        return 0

    # sweep over start and end times separately, in chronological order
    starts = sorted(i[0] for i in intervals)
    ends = sorted(i[1] for i in intervals)

    rooms = max_rooms = 0
    s = e = 0
    n = len(intervals)

    while s < n:
        if starts[s] < ends[e]:
            rooms += 1              # a meeting starts before the earliest end
            s += 1
            max_rooms = max(max_rooms, rooms)
        else:
            rooms -= 1              # a meeting freed a room
            e += 1

    return max_rooms


if __name__ == "__main__":
    print(minMeetingRooms([[0, 30], [5, 10], [15, 20]]))  # Expected: 2
    print(minMeetingRooms([[7, 10], [2, 4]]))              # Expected: 1

'''
Pattern
✅ Line Sweep (sort starts and ends, track concurrent count)

Key Observation
Walk the time axis: +1 room at each start, -1 at each end. The peak concurrent
count is the rooms needed. Equivalent to a min-heap of end times.

| Metric | Value      |
| ------ | ---------- |
| Time   | O(n log n) |
| Space  | O(n)       |

Better Possible?
❌ No — sorting is required.
'''
