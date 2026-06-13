"""
542. 01 Matrix (Medium)

Problem Statement
-----------------
Given an m x n binary matrix `mat`, return a matrix of the same size where each
cell holds the distance to the NEAREST cell containing 0. Distance between two
adjacent cells (up/down/left/right) is 1.

Example
-------
Input:  [[0,0,0],
         [0,1,0],
         [1,1,1]]
Output: [[0,0,0],
         [0,1,0],
         [1,2,1]]
"""

from collections import deque


def update_matrix(mat):
    rows, cols = len(mat), len(mat[0])
    dist = [[-1] * cols for _ in range(rows)]
    q = deque()

    # Multi-source seed: every 0 is a source at distance 0.
    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 0:
                dist[r][c] = 0
                q.append((r, c))

    # Single BFS expanding from all zeros simultaneously.
    while q:
        r, c = q.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))

    return dist


if __name__ == "__main__":
    mat1 = [[0, 0, 0],
            [0, 1, 0],
            [1, 1, 1]]
    print(update_matrix(mat1))  # Expected: [[0, 0, 0], [0, 1, 0], [1, 2, 1]]

    mat2 = [[0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]]
    print(update_matrix(mat2))  # Expected: [[0, 0, 0], [0, 1, 0], [0, 0, 0]]


"""
Pattern
-------
Multi-source BFS. Instead of running a separate BFS from each non-zero cell
(O((mn)^2)), we invert the problem: seed the queue with ALL zeros at distance 0
and expand outward once. The first time BFS reaches a cell it does so along the
shortest path from the nearest source, so the recorded distance is optimal.

| Metric | Value     |
|--------|-----------|
| Time   | O(m * n)  |
| Space  | O(m * n)  |

Better Possible?
No. Every cell must be assigned a value, so O(m*n) time is a lower bound, and
BFS achieves it. A DP two-pass approach matches the same complexity but BFS is
the canonical multi-source formulation.
"""
