"""
200. Number of Islands (Medium)

Problem Statement:
Given an m x n 2D binary grid which represents a map of '1's (land) and '0's
(water), return the number of islands. An island is surrounded by water and is
formed by connecting adjacent lands horizontally or vertically. You may assume
all four edges of the grid are surrounded by water.

Example:
    Input:  [["1","1","0","0","0"],
             ["1","1","0","0","0"],
             ["0","0","1","0","0"],
             ["0","0","0","1","1"]]
    Output: 3

    Input:  [["1","1","1","1","0"],
             ["1","1","0","1","0"],
             ["1","1","0","0","0"],
             ["0","0","0","0","0"]]
    Output: 1
"""


def num_islands(grid):
    # Flood-fill DFS: each unvisited land cell starts a new island, then we sink
    # the whole connected landmass so it is not counted again.
    if not grid or not grid[0]:
        return 0
    m, n = len(grid), len(grid[0])
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(r, c):
        if not (0 <= r < m and 0 <= c < n) or grid[r][c] != '1':
            return
        grid[r][c] = '0'                      # mark visited (sink the land)
        for dr, dc in dirs:
            dfs(r + dr, c + dc)

    count = 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == '1':
                count += 1                    # found a new island
                dfs(r, c)                     # sink it entirely
    return count


if __name__ == "__main__":
    g1 = [["1", "1", "0", "0", "0"],
          ["1", "1", "0", "0", "0"],
          ["0", "0", "1", "0", "0"],
          ["0", "0", "0", "1", "1"]]
    print(num_islands(g1))  # Expected: 3

    g2 = [["1", "1", "1", "1", "0"],
          ["1", "1", "0", "1", "0"],
          ["1", "1", "0", "0", "0"],
          ["0", "0", "0", "0", "0"]]
    print(num_islands(g2))  # Expected: 1

"""
Pattern: Grid Graph / Islands (connected-components flood fill via DFS).
Technique: treat each cell as a node with 4-directional neighbors; scan the grid,
and whenever an unvisited '1' is met, increment the island count and DFS-sink the
entire connected region so its cells are never recounted.
Why: each distinct connected landmass is counted exactly once because the first
cell reached triggers the count and the DFS marks every reachable land cell.

| Metric | Value     |
|--------|-----------|
| Time   | O(m * n)  |
| Space  | O(m * n)  |   recursion stack worst case (one big island)

Better Possible?
Time is optimal (must inspect every cell). Union-Find gives the same O(m*n) with
near-constant amortized merges; iterative BFS avoids deep recursion for huge grids.
"""
