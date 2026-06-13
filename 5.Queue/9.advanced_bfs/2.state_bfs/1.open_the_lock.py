'''
752. Open the Lock (Medium)
Problem Statement

You have a lock with 4 circular wheels, each labeled 0-9. The lock starts at
"0000". Each move turns one wheel one slot (0->9 wraps, 9->0 wraps).

Given a list of deadends (combinations the lock must never display) and a target,
return the minimum number of turns to reach target from "0000", or -1 if it is
impossible.

Input:
deadends = ["0201","0101","0102","1212","2002"], target = "0202"

Output:
6
'''

from collections import deque


def openLock(deadends, target):
    dead = set(deadends)
    if "0000" in dead:           # can't even start
        return -1
    if target == "0000":
        return 0

    # neighbors: for each of 4 wheels, +1 and -1 (mod 10)
    def neighbors(state):
        for i in range(4):
            d = int(state[i])
            for nd in ((d + 1) % 10, (d - 1) % 10):
                yield state[:i] + str(nd) + state[i + 1:]

    q = deque([("0000", 0)])     # (state, turns)
    visited = {"0000"}

    while q:
        state, turns = q.popleft()
        for nxt in neighbors(state):
            if nxt in visited or nxt in dead:
                continue
            if nxt == target:
                return turns + 1
            visited.add(nxt)
            q.append((nxt, turns + 1))

    return -1


if __name__ == "__main__":
    print(openLock(["0201", "0101", "0102", "1212", "2002"], "0202"))  # Expected: 6
    print(openLock(["0000"], "8888"))                                  # Expected: -1


'''
Pattern
✅ State BFS
Each 4-digit combination is a graph node; an edge connects two states that differ
by one wheel turn. BFS from "0000" gives the minimum number of turns because every
edge has unit cost (shortest path in an unweighted graph). Deadends are simply nodes
we refuse to enqueue.

| Metric | Value                          |
| ------ | ------------------------------ |
| Time   | O(N * A^N * b) = O(10^4 * 8)    |  N=4 wheels, A=10 digits, b=8 neighbors
| Space  | O(10^4)                        |  visited set + queue

Better Possible?
✅ Bidirectional BFS searches from both "0000" and target and meets in the middle,
shrinking the explored frontier. Same big-O bound but far fewer states in practice.
'''
