"""
1162. As Far from Land as Possible (Medium)

Problem Statement
-----------------
Given an n x n grid of 0s (water) and 1s (land), find a water cell whose distance
to the nearest land cell is MAXIMIZED, and return that maximum distance. Distance
used is Manhattan distance via 4-directional steps. If no land or no water exists,
return -1.

Example
-------
Input:  [[1,0,1],
         [0,0,0],
         [1,0,1]]
Output: 2   (the center cell (1,1) is distance 2 from the nearest land)

Input:  [[1,0,0],
         [0,0,0],
         [0,0,0]]
Output: 4   (the far corner (2,2) is distance 4 from the only land at (0,0))
"""

from collections import deque


def max_distance(grid):
    n = len(grid)
    q = deque()
    visited = [[False] * n for _ in range(n)]

    # Multi-source seed: every land cell is a source at distance 0.
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                q.append((r, c))
                visited[r][c] = True

    # All water or all land -> no valid answer.
    if len(q) == 0 or len(q) == n * n:
        return -1

    dist = -1
    # BFS level by level; the last level reached is the farthest water cell.
    while q:
        for _ in range(len(q)):
            r, c = q.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr, nc))
        dist += 1

    return dist


if __name__ == "__main__":
    grid1 = [[1, 0, 1],
             [0, 0, 0],
             [1, 0, 1]]
    print(max_distance(grid1))  # Expected: 2

    grid2 = [[1, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    print(max_distance(grid2))  # Expected: 4


"""
Pattern
-------
Multi-source BFS. Seed the queue with every land cell at distance 0 and flood
all water simultaneously. Because all sources expand in lockstep, each water cell
is first visited at its distance to the NEAREST land. The number of full BFS
levels processed equals the largest such nearest-distance, which is the answer.
Level counting (process the whole frontier per round) lets us read off the depth
without storing per-cell distances.

| Metric | Value     |
|--------|-----------|
| Time   | O(n^2)    |
| Space  | O(n^2)    |

Better Possible?
No. Each of the n*n cells is enqueued and dequeued at most once, so O(n^2) is
optimal for a grid that must be fully examined.
"""
