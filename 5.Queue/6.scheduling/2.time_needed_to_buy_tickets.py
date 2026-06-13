"""
2073. Time Needed to Buy Tickets (Easy)

Problem Statement:
People stand in a line (a queue) to buy tickets. `tickets[i]` is how many tickets
person i still wants. Each second, the person at the front buys ONE ticket. If
they still need more, they go to the back of the line; otherwise they leave.
Return the number of seconds it takes for the person at position `k` to finish
buying all of their tickets.

Example:
    Input:  tickets = [2,3,2], k = 2
    Output: 6
    Input:  tickets = [5,1,1,1], k = 0
    Output: 8
"""

from collections import deque


def time_required_to_buy(tickets, k):
    # Queue of (index, remaining) so we can detect when person k is done.
    q = deque((i, t) for i, t in enumerate(tickets))
    time = 0
    while q:
        i, remaining = q.popleft()
        time += 1               # this person buys one ticket (one second)
        remaining -= 1
        if remaining == 0:
            if i == k:          # target finished -> total time so far is the answer
                return time
        else:
            q.append((i, remaining))  # still wants more -> back of the line
    return time


def time_required_to_buy_math(tickets, k):
    # O(n) one-pass: person before/at k contributes min(t, tickets[k]) seconds,
    # person after k contributes min(t, tickets[k] - 1).
    target = tickets[k]
    total = 0
    for i, t in enumerate(tickets):
        total += min(t, target) if i <= k else min(t, target - 1)
    return total


if __name__ == "__main__":
    print(time_required_to_buy([2, 3, 2], k=2))      # Expected: 6
    print(time_required_to_buy([5, 1, 1, 1], k=0))   # Expected: 8
    print(time_required_to_buy_math([2, 3, 2], k=2))     # Expected: 6
    print(time_required_to_buy_math([5, 1, 1, 1], k=0))  # Expected: 8

"""
Pattern: Scheduling (FIFO with re-insertion).
Technique: simulate the line with a deque, re-queueing anyone who still needs
tickets, and stop the moment person k hits zero. A closed-form O(n) pass also
works: everyone at or before k buys up to tickets[k], everyone after buys up to
tickets[k] - 1 (they stop once the target's last purchase happens).
Why: the queue models the round-robin directly; the math version skips the
simulation by counting each person's bounded contribution.

| Metric | Value (simulation) | Value (math) |
|--------|--------------------|--------------|
| Time   | O(n * max_ticket)  | O(n)         |
| Space  | O(n)               | O(1)         |

Better Possible?
The math one-pass at O(n) time / O(1) extra space is optimal — every person must
be inspected at least once.
"""
