'''
1. Jump Game III (Medium)
Problem Statement

Given an array of non-negative integers arr and a start index start, you stand
on index start. From any index i you may jump to i + arr[i] or i - arr[i]
(staying inside the array bounds).

Return True if you can reach ANY index whose value is 0, otherwise False.

Input:
arr = [4,2,3,0,3,1,2]
start = 5

Output:
True

Explanation:
5 -> 4 (5-1) -> 1 (4-3) -> 3 (1+2), arr[3] == 0. Reachable.
'''

from collections import deque


def canReach(arr, start):
    # Reachability over an implicit graph: each index i has edges to
    # i+arr[i] and i-arr[i]. We BFS from `start`, marking visited indices
    # so we never loop forever. If any popped index holds value 0 -> True.
    n = len(arr)
    visited = [False] * n
    queue = deque([start])
    visited[start] = True

    while queue:
        i = queue.popleft()
        if arr[i] == 0:        # found a zero -> success
            return True
        for nxt in (i + arr[i], i - arr[i]):
            if 0 <= nxt < n and not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)

    return False               # exhausted reachable set, no zero found


if __name__ == "__main__":
    print(canReach([4, 2, 3, 0, 3, 1, 2], 5))  # Expected: True
    print(canReach([4, 2, 3, 0, 3, 1, 2], 0))  # Expected: True
    print(canReach([3, 0, 2, 1, 2], 2))        # Expected: False


'''
Pattern
✅ Graph Reachability via BFS (Jump Game family)

Greedy/rule & why it's safe:
Unlike Jump Game I/II (single forward direction, where a greedy "track the
farthest reach" works), Jump Game III allows BOTH +arr[i] and -arr[i] moves,
so reachability is no longer a monotone forward sweep — it is plain graph
connectivity. The safe rule is: an index is reachable iff it sits in the same
connected component as `start`. BFS explores that component exactly once.
Marking a node visited the moment it is enqueued is safe because every edge is
bidirectional in effect across the search; revisiting could only re-derive an
already-known-reachable index, never a new one, so skipping visited nodes loses
no answer and guarantees termination. Answer = does the component contain a 0.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No (asymptotically). Each index is enqueued/visited at most once and each has
at most two outgoing edges, so the traversal is O(n) time and O(n) space for the
visited array + queue. We must touch reachable indices at least once, so O(n) is
optimal. (Space can be trimmed to O(1) extra by mutating arr to negative as a
visited marker, but time stays O(n).)
'''
