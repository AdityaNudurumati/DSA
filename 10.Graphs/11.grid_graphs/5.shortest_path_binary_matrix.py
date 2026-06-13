"""
1091. Shortest Path in Binary Matrix (Medium)

Problem Statement:
Given an n x n binary matrix grid, return the length of the shortest clear path
from the top-left cell (0,0) to the bottom-right cell (n-1,n-1). A clear path
visits only cells with value 0, moves 8-directionally between adjacent cells, and
its length is the number of visited cells. If there is no clear path, return -1.

Example:
    Input:  [[0,1],[1,0]]                     Output: 2
    Input:  [[0,0,0],[1,1,0],[1,1,0]]         Output: 4
    Input:  [[1,0,0]]                          Output: -1
"""

from collections import deque


def shortest_path_binary_matrix(grid):
    # 8-directional BFS: BFS explores cells in increasing path length, so the
    # first time we pop the target the distance is minimal.
    n = len(grid)
    if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
        return -1                             # blocked start or end
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
            (0, 1), (1, -1), (1, 0), (1, 1)]

    q = deque([(0, 0, 1)])                     # (row, col, path length so far)
    grid[0][0] = 1                             # mark visited
    while q:
        r, c, d = q.popleft()
        if r == n - 1 and c == n - 1:
            return d                           # reached target with min length
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                grid[nr][nc] = 1               # mark before enqueue (no dupes)
                q.append((nr, nc, d + 1))
    return -1


if __name__ == "__main__":
    print(shortest_path_binary_matrix([[0, 1], [1, 0]]))                  # Expected: 2
    print(shortest_path_binary_matrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]))  # Expected: 4
    print(shortest_path_binary_matrix([[1, 0, 0]]))                       # Expected: -1

"""
Pattern: Grid Graph / Shortest Path (8-directional BFS on an unweighted grid).
Technique: model open cells as graph nodes connected to their 8 neighbors and run
BFS from the start, carrying the path length. Because every edge has unit cost,
BFS dequeues cells in nondecreasing distance, so the target's first dequeue is the
shortest path length.
Why: marking each cell visited at enqueue time prevents revisits and keeps the
frontier expanding level by level (one level = +1 path length).

| Metric | Value      |
|--------|------------|
| Time   | O(n^2)     |
| Space  | O(n^2)     |   queue + visited marking (in place)

Better Possible?
For exact shortest path on a unit-weight grid, BFS is optimal at O(n^2). A* with a
Chebyshev-distance heuristic can prune the search in practice but has the same
worst-case complexity.
"""
