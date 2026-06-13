'''
2290. Minimum Obstacles to Reach Corner (Hard)
Problem Statement

You are given a 0-indexed 2D integer array grid of size m x n. Each cell has one
of two values:
  - 0 represents an empty cell,
  - 1 represents an obstacle that may be removed.

You can move up, down, left, or right from and to an empty cell.

Return the minimum number of obstacles to remove so you can move from the top-left
corner (0, 0) to the bottom-right corner (m - 1, n - 1).

Example 1:
Input:  grid = [[0,1,1],[1,1,0],[1,1,0]]
Output: 2
Explanation: The path going down then right removes the 2 obstacles at (0,1)
and (0,2) (or an equivalent 2-obstacle path). 2 is the minimum.

Example 2:
Input:  grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
Output: 0
Explanation: There is a path from corner to corner crossing only empty cells.
'''

from collections import deque


def minimumObstacles(grid):
    # Model each cell as a node. Moving into a cell costs grid[r][c]:
    #   stepping onto an empty cell  (0) -> weight-0 edge -> appendleft
    #   stepping onto an obstacle    (1) -> weight-1 edge -> append
    # With only 0/1 edge weights, a deque-based 0-1 BFS finds shortest
    # distances in O(V + E) without Dijkstra's heap.
    m, n = len(grid), len(grid[0])
    INF = float("inf")
    dist = [[INF] * n for _ in range(m)]
    dist[0][0] = grid[0][0]            # may start on an obstacle

    dq = deque([(0, 0)])               # holds cells, distances live in dist[][]
    while dq:
        r, c = dq.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n:
                nd = dist[r][c] + grid[nr][nc]   # cost = value of cell entered
                if nd < dist[nr][nc]:
                    dist[nr][nc] = nd
                    # weight-0 move -> front, weight-1 move -> back
                    if grid[nr][nc] == 0:
                        dq.appendleft((nr, nc))
                    else:
                        dq.append((nr, nc))

    return dist[m - 1][n - 1]


if __name__ == "__main__":
    grid1 = [[0, 1, 1], [1, 1, 0], [1, 1, 0]]
    print(minimumObstacles(grid1))  # Expected: 2

    grid2 = [[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]]
    print(minimumObstacles(grid2))  # Expected: 0


'''
Pattern
✅ 0-1 BFS with a deque
Edge weights are only 0 (enter empty cell) or 1 (remove obstacle). A double-ended
queue replaces Dijkstra's heap: relax weight-0 edges to the front and weight-1
edges to the back so the deque always pops cells in non-decreasing distance order.
Each cell is finalized once, giving linear time.

| Metric | Value      |
| ------ | ---------- |
| Time   | O(m * n)   |
| Space  | O(m * n)   |

Better Possible?
❌ No
Every cell must be examined at least once, so O(m * n) is optimal. Plain Dijkstra
would work but adds a log factor; 0-1 BFS exploits the binary weights to avoid it.
'''
