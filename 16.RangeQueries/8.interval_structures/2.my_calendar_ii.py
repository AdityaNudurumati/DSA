'''
2. My Calendar II (Medium)
Problem Statement

Implement a MyCalendarTwo class. A new event [start, end) (end exclusive) can be
added only if it does NOT cause a TRIPLE booking — a moment in time covered by
three events at once. book(start, end) returns True if it can be added without a
triple booking (and adds it), otherwise False (and does not add it). Double
bookings are allowed.

Example
Input:
book(10,20), book(50,60), book(10,40), book(5,15), book(5,10), book(25,55)

Output:
True, True, True, False, True, True
'''


class MyCalendarTwo:
    # Track all booked intervals plus the set of double-booked (overlap) intervals.
    # A new event is rejected iff it overlaps any existing double-booking (that
    # would make a triple). Otherwise, record the new overlaps it forms with
    # singles into `overlaps`, then store the event itself.

    def __init__(self):
        self.bookings = []   # all accepted intervals
        self.overlaps = []   # regions currently covered twice

    def book(self, start, end):
        # reject if this event would extend any double-booked region into a triple
        for s, e in self.overlaps:
            if start < e and s < end:          # half-open overlap
                return False

        # accumulate new double-bookings created against existing single bookings
        for s, e in self.bookings:
            if start < e and s < end:
                self.overlaps.append((max(start, s), min(end, e)))

        self.bookings.append((start, end))
        return True


if __name__ == "__main__":
    cal = MyCalendarTwo()
    print(cal.book(10, 20))  # Expected: True
    print(cal.book(50, 60))  # Expected: True
    print(cal.book(10, 40))  # Expected: True
    print(cal.book(5, 15))   # Expected: False
    print(cal.book(5, 10))   # Expected: True
    print(cal.book(25, 55))  # Expected: True

'''
Pattern
Overlap-tracking Intervals (two interval lists)

Structure & why
Triple booking means a point lies in three intervals — equivalently, a new
interval intersects an already double-booked region. We maintain `bookings` (all
events) and `overlaps` (every pairwise intersection seen so far). Booking checks
against `overlaps` for a would-be triple; if clear, it merges its intersections
with each single booking into `overlaps`. The half-open overlap test is
`start < e and s < end`.

| Metric | Value |
| ------ | ----- |
| Build  | O(1)  |
| Query  | O(n)  |
| Update | O(n)  |

Better Possible?
Yes — a balanced BST / segment tree over a delta map gives O(log n) per booking
(see My Calendar III). The list approach is O(n) per booking but far simpler.
'''
