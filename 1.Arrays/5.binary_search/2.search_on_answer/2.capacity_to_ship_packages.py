'''
2. Capacity To Ship Packages Within D Days (Medium)
Problem Statement

Packages on a conveyor must ship within `days` days, in the given order. Each day
you load consecutive packages without exceeding the ship's capacity. Return the
minimum capacity that allows shipping everything within `days`.

Example
Input:
weights = [1,2,3,4,5,6,7,8,9,10], days = 5

Output:
15
'''

def shipWithinDays(weights, days):

    def days_needed(cap):
        d, current = 1, 0
        for w in weights:
            if current + w > cap:
                d += 1
                current = 0
            current += w
        return d

    # capacity must be at least the heaviest package, at most the whole sum
    lo, hi = max(weights), sum(weights)

    while lo < hi:
        mid = (lo + hi) // 2
        if days_needed(mid) <= days:
            hi = mid
        else:
            lo = mid + 1

    return lo


if __name__ == "__main__":
    print(shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))  # Expected: 15
    print(shipWithinDays([3, 2, 2, 4, 1, 4], 3))                # Expected: 6
    print(shipWithinDays([1, 2, 3, 1, 1], 4))                   # Expected: 3

'''
Pattern
✅ Binary Search on the Answer (minimize capacity, monotonic feasibility)

Key Observation
Bigger capacity -> fewer (or equal) days, so feasibility is monotonic. Search the
smallest capacity in [max weight, total weight] that ships within `days`.

| Metric | Value                |
| ------ | -------------------- |
| Time   | O(n log(sum))        |
| Space  | O(1)                 |

Better Possible?
❌ No meaningfully better bound.
'''
