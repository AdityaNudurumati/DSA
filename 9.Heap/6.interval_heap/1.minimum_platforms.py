'''
1. Minimum Number of Platforms (Medium)
Problem Statement

Given arrival and departure times of trains at a railway station, find the
minimum number of platforms required so that no train has to wait. A platform
holds one train from its arrival until its departure (inclusive overlap means
two platforms are needed).

Example
Input:
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

Output:
3
'''

import heapq


def minPlatforms(arr, dep):
    # build intervals and sort by arrival time
    trains = sorted(zip(arr, dep), key=lambda t: t[0])

    busy = []          # min-heap of departure times of trains currently parked
    platforms = 0      # peak heap size = answer

    for a, d in trains:
        # free every platform whose train left before this train arrives.
        # overlap is inclusive: a train arriving exactly when another departs
        # still needs its own platform, so only pop when departure < arrival.
        while busy and busy[0] < a:
            heapq.heappop(busy)
        heapq.heappush(busy, d)          # occupy a platform for this train
        platforms = max(platforms, len(busy))

    return platforms


if __name__ == "__main__":
    print(minPlatforms([900, 940, 950, 1100, 1500, 1800],
                       [910, 1200, 1120, 1130, 1900, 2000]))   # Expected: 3
    print(minPlatforms([900, 1100, 1235],
                       [1000, 1200, 1240]))                     # Expected: 1


'''
Pattern
✅ Interval + Heap (min-heap of departure times)

Technique & Why
Sort trains by arrival, then sweep. A min-heap keeps the departure times of all
trains currently occupying a platform; its root is the earliest-freeing one.
Before parking a new train we evict every platform that has already freed up
(departure < arrival). The peak heap size over the whole sweep is the minimum
number of platforms needed — equivalent to the maximum concurrent overlap.

| Metric | Value      |
| ------ | ---------- |
| Time   | O(n log n) |
| Space  | O(n)       |

Better Possible?
❌ Not asymptotically — sorting dominates at O(n log n). The classic two-pointer
sweep over separately sorted arrival/departure arrays achieves the same bound
with O(1) extra space, but the heap version generalizes cleanly to resource
scheduling where you must know which specific platform freed up.
'''
