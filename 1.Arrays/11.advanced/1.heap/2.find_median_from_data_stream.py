'''
2. Find Median from Data Stream (Hard)
Problem Statement

Design a structure that supports adding integers from a stream and returning the
median of all elements so far.
- addNum(num): add an integer
- findMedian(): return the current median

Example
addNum(1); addNum(2); findMedian() -> 1.5
addNum(3);            findMedian() -> 2
'''

import heapq

class MedianFinder:

    def __init__(self):
        self.small = []   # max-heap (store negatives) of the lower half
        self.large = []   # min-heap of the upper half

    def addNum(self, num):
        # push to small, then funnel its max into large to keep order
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # rebalance so small holds the extra element when sizes differ
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2


if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    print(mf.findMedian())   # Expected: 1.5
    mf.addNum(3)
    print(mf.findMedian())   # Expected: 2.0

'''
Pattern
✅ Two Heaps (max-heap lower half, min-heap upper half)

Key Observation
Balance the two halves so their roots straddle the median. addNum funnels through
both heaps then rebalances; the median is a root or the average of the two roots.

| Metric    | Value     |
| --------- | --------- |
| addNum    | O(log n)  |
| findMedian| O(1)      |
| Space     | O(n)      |

Better Possible?
❌ No for a dynamic stream.
'''
