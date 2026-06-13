'''
3. Corporate Flight Bookings (Medium)   (LeetCode 1109)
Problem Statement

There are n flights labeled 1..n. Each booking is [first, last, seats] meaning
`seats` were reserved on every flight from first to last (1-indexed, inclusive).
Return an array of length n where answer[i] is the total seats reserved on flight
i+1.

Because every booking is a range-add and we only read the result once at the end,
a difference array gives O(bookings + n) with O(1) per range update.

Example
Input:
bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5  -> [10, 55, 45, 25, 25]
bookings = [[1,2,10],[2,2,15]],          n = 2  -> [10, 25]
'''


def corp_flight_bookings(bookings, n):
    # diff has one extra slot so a booking ending at flight n needs no bounds check
    diff = [0] * (n + 1)
    for first, last, seats in bookings:
        diff[first - 1] += seats        # start adding from this flight (0-indexed)
        diff[last] -= seats             # stop adding right after `last`
    # prefix sum of the difference array reconstructs the real per-flight totals
    result = [0] * n
    running = 0
    for i in range(n):
        running += diff[i]
        result[i] = running
    return result


if __name__ == "__main__":
    print(corp_flight_bookings([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5))
    # Expected: [10, 55, 45, 25, 25]
    print(corp_flight_bookings([[1, 2, 10], [2, 2, 15]], 2))
    # Expected: [10, 25]

'''
Pattern
✅ Difference Array (range-add, single final read)

A difference array stores deltas: adding v to [l, r] is just diff[l] += v and
diff[r+1] -= v, an O(1) update. A final prefix sum turns the deltas back into
absolute values. This is the lightweight cousin of lazy propagation: when all
updates precede all queries, you skip the tree entirely.

| Metric        | Value          |
| ------------- | -------------- |
| Range Update  | O(1)           |
| Finalize      | O(n)           |
| Total         | O(bookings + n)|
| Space         | O(n)           |

Better Possible?
❌ No. You must touch every booking and produce every output cell, so
O(bookings + n) is optimal. A lazy segment tree would solve it too but is overkill
here since queries do not interleave with updates.
'''
