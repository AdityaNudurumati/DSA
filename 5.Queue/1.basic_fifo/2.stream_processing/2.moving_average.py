'''
2. Moving Average from Data Stream (Easy)  [LC346]
Problem Statement

Given a stream of integers and a window size, calculate the moving average of
all integers in the sliding window.

Implement MovingAverage(size) and next(val), which adds val to the stream and
returns the average of the last `size` values (or fewer, if the stream has not
yet produced `size` values).

Input:
MovingAverage(size = 3)
next(1)
next(10)
next(3)
next(5)

Output:
1.0
5.5
4.6667
6.0

Explanation:
next(1)  -> [1]            -> 1 / 1            = 1.0
next(10) -> [1, 10]        -> 11 / 2           = 5.5
next(3)  -> [1, 10, 3]     -> 14 / 3           = 4.6667
next(5)  -> [10, 3, 5]     -> 18 / 3 = 6.0     (1 slid out of the window)
'''

from collections import deque


class MovingAverage:
    def __init__(self, size):
        self.size = size
        self.q = deque()        # holds the last `size` values
        self.window_sum = 0     # running sum, kept in sync with the deque

    def next(self, val):
        self.q.append(val)
        self.window_sum += val
        if len(self.q) > self.size:
            # window full: evict the oldest value (FIFO) and adjust the sum
            self.window_sum -= self.q.popleft()
        return self.window_sum / len(self.q)


if __name__ == "__main__":
    m = MovingAverage(3)
    print(m.next(1))               # Expected: 1.0
    print(m.next(10))              # Expected: 5.5
    print(round(m.next(3), 4))     # Expected: 4.6667
    print(m.next(5))               # Expected: 6.0


'''
Pattern
✅ Basic FIFO — Stream Processing (fixed-size sliding window)
A deque holds the most recent `size` values. We keep a running sum so each
next() is O(1): add the new value, and once the window overflows, popleft the
oldest value (FIFO) and subtract it. Average = running sum / current count.

| Metric         | Value    |
| -------------- | -------- |
| Time per next  | O(1)     |
| Space          | O(size)  |

Better Possible?
❌ No. The running sum avoids re-summing the window, giving O(1) per query,
which is optimal. Space O(size) is required to know which value leaves next.
'''
