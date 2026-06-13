"""
200. Number of Islands (Medium)

Problem Statement:
Given an m x n 2D binary grid which represents a map of '1's (land) and '0's
(water), return the number of islands. An island is surrounded by water and is
formed by connecting adjacent lands horizontally or vertically.

Example:
    Input:  grid = [["1","1","1","1","0"],
                     ["1","1","0","1","0"],
                     ["1","1","0","0","0"],
                     ["0","0","0","0","0"]]
    Output: 1

    Input:  grid = [["1","1","0","0","0"],
                     ["1","1","0","0","0"],
                     ["0","0","1","0","0"],
                     ["0","0","0","1","1"]]
    Output: 3
"""

from collections import deque


def num_islands(grid):
    # Scan cells; on each unvisited land cell, BFS-flood it and count one island.
    if not grid or not grid[0]:
        return 0
    rows, cols = len(grid), len(grid[0])
    seen = set()
    count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in seen:
                count += 1
                q = deque([(r, c)])
                seen.add((r, c))
                while q:
                    cr, cc = q.popleft()
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = cr + dr, cc + dc
                        if (0 <= nr < rows and 0 <= nc < cols
                                and grid[nr][nc] == "1" and (nr, nc) not in seen):
                            seen.add((nr, nc))
                            q.append((nr, nc))
    return count


if __name__ == "__main__":
    grid1 = [["1", "1", "1", "1", "0"],
             ["1", "1", "0", "1", "0"],
             ["1", "1", "0", "0", "0"],
             ["0", "0", "0", "0", "0"]]

    grid2 = [["1", "1", "0", "0", "0"],
             ["1", "1", "0", "0", "0"],
             ["0", "0", "1", "0", "0"],
             ["0", "0", "0", "1", "1"]]

    print(num_islands(grid1))  # Expected: 1
    print(num_islands(grid2))  # Expected: 3

"""
Pattern: Grid BFS (connected-component flood fill).
Technique: iterate every cell; the first time we hit unvisited land, increment
the island count and BFS-flood all reachable land via 4-directional moves,
marking cells in a visited set so they are not recounted.
Why: each connected blob of land is one island; BFS marks the whole component
in one sweep before the outer loop can start a new count.

| Metric | Value         |
|--------|---------------|
| Time   | O(m * n)      |
| Space  | O(m * n)      |

Better Possible?
No on time — every cell is examined once. Space could drop by mutating the grid
in place (sinking land to '0') instead of a visited set, but stays O(m*n) in the
worst case for the BFS queue.
"""
