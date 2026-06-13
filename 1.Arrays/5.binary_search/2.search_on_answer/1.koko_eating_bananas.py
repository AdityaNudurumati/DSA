'''
1. Koko Eating Bananas (Medium)
Problem Statement

Koko has piles of bananas (piles[i] in pile i) and h hours before the guards return.
Each hour she picks a pile and eats up to `speed` bananas; if a pile has fewer, she
finishes it and waits out the hour. Return the minimum integer speed to finish all
piles within h hours.

Example
Input:
piles = [3,6,7,11], h = 8

Output:
4
'''

import math

def minEatingSpeed(piles, h):

    def hours_needed(speed):
        return sum(math.ceil(p / speed) for p in piles)

    # search on answer: speed in [1, max pile]; feasibility is monotonic
    lo, hi = 1, max(piles)

    while lo < hi:
        mid = (lo + hi) // 2
        if hours_needed(mid) <= h:
            hi = mid            # mid works, try slower
        else:
            lo = mid + 1        # too slow

    return lo


if __name__ == "__main__":
    print(minEatingSpeed([3, 6, 7, 11], 8))         # Expected: 4
    print(minEatingSpeed([30, 11, 23, 4, 20], 5))   # Expected: 30
    print(minEatingSpeed([30, 11, 23, 4, 20], 6))   # Expected: 23

'''
Pattern
✅ Binary Search on the Answer (minimize a monotonic feasible value)

Key Observation
"Can finish at speed s?" is monotonic: if s works, every faster speed works too.
Binary search the smallest s for which the feasibility check passes.

| Metric | Value                |
| ------ | -------------------- |
| Time   | O(n log(max pile))   |
| Space  | O(1)                 |

Better Possible?
❌ No meaningfully better bound.
'''
