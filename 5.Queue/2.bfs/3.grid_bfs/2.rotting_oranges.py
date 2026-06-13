"""
994. Rotting Oranges (Medium)

Problem Statement:
You are given an m x n grid where each cell can be 0 (empty), 1 (fresh orange),
or 2 (rotten orange). Every minute, any fresh orange that is 4-directionally
adjacent to a rotten orange becomes rotten. Return the minimum number of minutes
that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example:
    Input:  [[2,1,1],[1,1,0],[0,1,1]]  Output: 4
    Input:  [[2,1,1],[0,1,1],[1,0,1]]  Output: -1
    Input:  [[0,2]]                     Output: 0
"""

from collections import deque


def oranges_rotting(grid):
    # Multi-source BFS: seed the queue with ALL rotten oranges at minute 0.
    rows, cols = len(grid), len(grid[0])
    q = deque()
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                q.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1

    if fresh == 0:
        return 0  # nothing to rot

    minutes = 0
    while q and fresh > 0:
        minutes += 1
        for _ in range(len(q)):       # one level = one minute
            cr, cc = q.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  # becomes rotten
                    fresh -= 1
                    q.append((nr, nc))

    return minutes if fresh == 0 else -1


if __name__ == "__main__":
    print(oranges_rotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))  # Expected: 4
    print(oranges_rotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))  # Expected: -1
    print(oranges_rotting([[0, 2]]))                            # Expected: 0

"""
Pattern: Multi-Source BFS (simultaneous spread / level = elapsed time).
Technique: enqueue every initially rotten orange, then expand the frontier one
level per minute, rotting adjacent fresh oranges and decrementing a fresh count.
Why: starting all sources together models simultaneous spreading; the number of
BFS levels equals the minutes needed for the last orange to rot.

| Metric | Value         |
|--------|---------------|
| Time   | O(m * n)      |
| Space  | O(m * n)      |

Better Possible?
No — every cell is processed at most once. The leftover fresh count cleanly
detects the unreachable case (-1) without a second scan.
"""
