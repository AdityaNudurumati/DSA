'''
1368. Minimum Cost to Make at Least One Valid Path in a Grid (Hard)
Problem Statement

Given an m x n grid where each cell has a sign pointing to its next cell:
  1 = right, 2 = left, 3 = down, 4 = up.
Starting at (0,0) you follow signs for free. You may change the sign of any cell,
each change costing 1. Return the minimum total cost so there exists a valid path
from (0,0) to (m-1,n-1).

Input:
grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]

Output:
3
'''

from collections import deque


def minCost(grid):
    m, n = len(grid), len(grid[0])
    # direction of each sign: index 1..4 -> (dr, dc)
    moves = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}

    INF = float("inf")
    dist = [[INF] * n for _ in range(m)]
    dist[0][0] = 0

    # 0-1 BFS: following the existing sign costs 0 (appendleft),
    # changing the sign costs 1 (append).
    dq = deque([(0, 0)])

    while dq:
        r, c = dq.popleft()
        d = dist[r][c]
        for sign, (dr, dc) in moves.items():
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n:
                w = 0 if grid[r][c] == sign else 1   # free if cell already points here
                if d + w < dist[nr][nc]:
                    dist[nr][nc] = d + w
                    if w == 0:
                        dq.appendleft((nr, nc))
                    else:
                        dq.append((nr, nc))

    return dist[m - 1][n - 1]


if __name__ == "__main__":
    print(minCost([[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]))  # Expected: 3
    print(minCost([[1, 1, 3], [3, 2, 2], [1, 1, 4]]))                          # Expected: 0
    print(minCost([[1, 2], [4, 3]]))                                           # Expected: 1


'''
Pattern
✅ 0-1 BFS (deque)
The grid is a weighted graph where moving in the cell's existing arrow direction is a
0-cost edge and moving in any other direction is a 1-cost edge (one sign change).
With only weights 0 and 1, a double-ended queue replaces a heap: push 0-edges to the
FRONT and 1-edges to the BACK so the deque stays sorted by distance, giving Dijkstra
behavior in linear time.

| Metric | Value      |
| ------ | ---------- |
| Time   | O(m * n)   |  each cell relaxed O(1) times, 4 edges each
| Space  | O(m * n)   |  dist grid + deque

Better Possible?
❌ For 0/1 weights, 0-1 BFS is optimal at O(V+E). A general Dijkstra with a heap would
add an unnecessary O(log V) factor.
'''
