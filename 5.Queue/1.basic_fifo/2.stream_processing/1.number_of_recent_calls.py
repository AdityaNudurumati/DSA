'''
1. Number of Recent Calls (Easy)  [LC933]
Problem Statement

You have a RecentCounter that counts the number of recent requests within a
time window.

Implement ping(t), where t is the time in milliseconds of the current request.
Each call returns the number of requests that happened in the inclusive range
[t - 3000, t]. It is guaranteed that every call to ping uses a strictly larger
value of t than the previous call.

Input (sequence of pings):
ping(1)
ping(100)
ping(3001)
ping(3002)

Output:
1
2
3
3

Explanation:
ping(1)    -> window [-2999, 1]    : {1}                  -> 1
ping(100)  -> window [-2900, 100]  : {1, 100}             -> 2
ping(3001) -> window [1, 3001]     : {1, 100, 3001}       -> 3
ping(3002) -> window [2, 3002]     : {100, 3001, 3002}    -> 3  (1 dropped)
'''

from collections import deque


class RecentCounter:
    def __init__(self):
        self.q = deque()  # stores ping timestamps in increasing order

    def ping(self, t):
        self.q.append(t)
        # drop all timestamps older than the window start (t - 3000)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)


if __name__ == "__main__":
    rc = RecentCounter()
    print(rc.ping(1))     # Expected: 1
    print(rc.ping(100))   # Expected: 2
    print(rc.ping(3001))  # Expected: 3
    print(rc.ping(3002))  # Expected: 3


'''
Pattern
✅ Basic FIFO — Stream Processing (sliding time window)
Pings arrive in increasing order, so the queue stays sorted. Each ping appends
to the rear and evicts stale timestamps from the front; the remaining size is
the count inside the window. Front eviction is the natural FIFO operation.

| Metric          | Value |
| --------------- | ----- |
| Time per ping   | O(1)* |
| Space           | O(w)  |
(* amortized; each timestamp is added and removed at most once. w = pings in window)

Better Possible?
❌ No. Amortized O(1) per ping is optimal: each timestamp is processed a
constant number of times across the whole stream.
'''
