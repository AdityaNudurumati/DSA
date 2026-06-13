'''
3. My Calendar III (Hard)
Problem Statement

Implement a MyCalendarThree class. book(start, end) adds the event [start, end)
(end exclusive) and returns the current maximum k-booking — the largest number of
events that overlap at any single point in time across ALL bookings so far.

Example
Input:
book(10,20), book(50,60), book(10,40), book(5,15), book(5,10), book(25,55)

Output:
1, 1, 2, 3, 3, 3
'''

import bisect


class MyCalendarThree:
    # Sweep-line via a delta map: +1 at start, -1 at end. The max prefix sum over
    # the sorted boundary points is the peak concurrency. We keep `delta` as
    # parallel sorted lists (points + their net change) using bisect, since
    # sortedcontainers is unavailable.

    def __init__(self):
        self.points = []   # sorted distinct boundary times
        self.diffs = []     # net delta at each boundary time

    def _add(self, x, val):
        i = bisect.bisect_left(self.points, x)
        if i < len(self.points) and self.points[i] == x:
            self.diffs[i] += val
        else:
            self.points.insert(i, x)
            self.diffs.insert(i, val)

    def book(self, start, end):
        self._add(start, 1)   # event begins -> one more concurrent
        self._add(end, -1)     # event ends   -> one fewer concurrent

        running = best = 0
        for d in self.diffs:           # prefix-sum sweep over sorted boundaries
            running += d
            if running > best:
                best = running
        return best


if __name__ == "__main__":
    cal = MyCalendarThree()
    print(cal.book(10, 20))  # Expected: 1
    print(cal.book(50, 60))  # Expected: 1
    print(cal.book(10, 40))  # Expected: 2
    print(cal.book(5, 15))   # Expected: 3
    print(cal.book(5, 10))   # Expected: 3
    print(cal.book(25, 55))  # Expected: 3

'''
Pattern
Sweep Line over a delta/difference map

Structure & why
Concurrency at any instant is a prefix sum of boundary deltas: +1 where an event
starts, -1 where it ends (end exclusive, so the -1 lands exactly at `end`). The
answer is the maximum prefix sum over all boundaries in time order. We store the
delta map as two sorted parallel lists keyed by time and merge equal boundaries,
then re-sweep after each booking.

| Metric | Value    |
| ------ | -------- |
| Build  | O(1)     |
| Query  | O(n)     |
| Update | O(n)     |

(n = number of distinct boundary points; insert is O(n) for the list shift,
sweep is O(n).)

Better Possible?
Yes — a dynamic/lazy segment tree over compressed coordinates gives O(log n) per
booking by maintaining the running max incrementally instead of re-sweeping.
'''
