'''
1. My Calendar I (Medium)
Problem Statement

Implement a MyCalendar class to store events. A new event can be added only if it
does NOT cause a double booking. A double booking happens when two events share
some non-empty time [start, end) (end exclusive). book(start, end) returns True if
the event was added without a double booking, otherwise False (and is not added).

Example
Input:
book(10, 20), book(15, 25), book(20, 30)

Output:
True, False, True
'''

import bisect


class MyCalendar:
    # Keep booked intervals sorted by start in two parallel lists.
    # starts[i], ends[i] describe the i-th interval. bisect on starts locates
    # the insertion point; only the left and right neighbors can overlap a
    # well-ordered, conflict-free set, so we check just those two.

    def __init__(self):
        self.starts = []
        self.ends = []

    def book(self, start, end):
        i = bisect.bisect_right(self.starts, start)  # first interval starting after `start`

        # right neighbor at index i begins at starts[i]; overlap if it starts before `end`
        if i < len(self.starts) and self.starts[i] < end:
            return False
        # left neighbor at index i-1 ends at ends[i-1]; overlap if it ends after `start`
        if i > 0 and self.ends[i - 1] > start:
            return False

        self.starts.insert(i, start)
        self.ends.insert(i, end)
        return True


if __name__ == "__main__":
    cal = MyCalendar()
    print(cal.book(10, 20))  # Expected: True
    print(cal.book(15, 25))  # Expected: False
    print(cal.book(20, 30))  # Expected: True

'''
Pattern
Ordered-Map Intervals (sorted lists + bisect)

Structure & why
A conflict-free calendar stays totally ordered: intervals never overlap, so they
are sorted by start AND by end simultaneously. To test a candidate [start, end)
we bisect for its slot and inspect only the immediate left and right neighbors —
if neither overlaps, nothing else can. We use two parallel lists because
sortedcontainers is unavailable; bisect gives O(log n) search and list.insert is
O(n) for the shift.

| Metric | Value      |
| ------ | ---------- |
| Build  | O(1)       |
| Query  | O(log n)   |
| Update | O(n)       |

Better Possible?
A balanced BST / SortedList gives O(log n) insertion too, but the neighbor-only
overlap check is already optimal for the query itself.
'''
