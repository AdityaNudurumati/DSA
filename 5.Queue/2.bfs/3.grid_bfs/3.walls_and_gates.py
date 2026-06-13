"""
286. Walls and Gates (Medium)

Problem Statement:
You are given an m x n grid initialized with these three possible values:
  -1  = a wall or an obstacle.
   0  = a gate.
  INF = 2147483647, an empty room (Infinity meaning an empty room).
Fill each empty room with the distance to its nearest gate. If it is impossible
to reach a gate, that value stays as INF. Mutate the grid in place.

Example:
    INF = 2147483647
    Input:  [[INF,-1, 0, INF],
             [INF,INF,INF,-1],
             [INF,-1,INF,-1],
             [ 0, -1,INF,INF]]
    Output: [[ 3, -1, 0, 1],
             [ 2,  2, 1, -1],
             [ 1, -1, 2, -1],
             [ 0, -1, 3, 4]]
"""

from collections import deque

INF = 2147483647


def walls_and_gates(rooms):
    # Multi-source BFS from every gate at once; first arrival = shortest distance.
    if not rooms or not rooms[0]:
        return
    rows, cols = len(rooms), len(rooms[0])
    q = deque()
    for r in range(rows):
        for c in range(cols):
            if rooms[r][c] == 0:
                q.append((r, c))  # seed all gates

    while q:
        cr, cc = q.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = cr + dr, cc + dc
            # only overwrite empty rooms still at INF (skips walls and visited)
            if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == INF:
                rooms[nr][nc] = rooms[cr][cc] + 1
                q.append((nr, nc))


if __name__ == "__main__":
    rooms = [[INF, -1, 0, INF],
             [INF, INF, INF, -1],
             [INF, -1, INF, -1],
             [0, -1, INF, INF]]
    walls_and_gates(rooms)
    print(rooms)
    # Expected: [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]

"""
Pattern: Multi-Source BFS (shortest distance in an unweighted grid).
Technique: enqueue all gates simultaneously, then expand outward; each empty
room is reached first by its nearest gate, so we write distance = parent + 1 and
only ever touch a room while it still equals INF (acting as the visited guard).
Why: launching from all gates at once means the BFS frontier represents equal
distance, guaranteeing the first write to any room is the minimum.

| Metric | Value         |
|--------|---------------|
| Time   | O(m * n)      |
| Space  | O(m * n)      |

Better Possible?
No — multi-source BFS visits each room once. Running a separate BFS per gate
would be far worse, O(gates * m * n).
"""
