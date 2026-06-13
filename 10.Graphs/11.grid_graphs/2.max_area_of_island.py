"""
695. Max Area of Island (Medium)

Problem Statement:
You are given an m x n binary matrix grid. An island is a group of 1's (land)
connected 4-directionally (horizontal or vertical). The area of an island is the
number of cells with a value 1 in the island. Return the maximum area of an
island in grid. If there is no island, return 0.

Example:
    Input:  [[0,0,1,0,0,0,0,1,0,0,0,0,0],
             [0,0,0,0,0,0,0,1,1,1,0,0,0],
             [0,1,1,0,1,0,0,0,0,0,0,0,0],
             [0,1,0,0,1,1,0,0,1,0,1,0,0],
             [0,1,0,0,1,1,0,0,1,1,1,0,0],
             [0,0,0,0,0,0,0,0,0,0,1,0,0],
             [0,0,0,0,0,0,0,1,1,1,0,0,0],
             [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    Output: 6

    Input:  [[0,0,0,0],[0,0,0,0]]    Output: 0
"""


def max_area_of_island(grid):
    # DFS flood fill returning the size of the region; track the running maximum.
    if not grid or not grid[0]:
        return 0
    m, n = len(grid), len(grid[0])
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(r, c):
        if not (0 <= r < m and 0 <= c < n) or grid[r][c] != 1:
            return 0
        grid[r][c] = 0                        # mark visited
        area = 1
        for dr, dc in dirs:
            area += dfs(r + dr, c + dc)       # accumulate connected land
        return area

    best = 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1:
                best = max(best, dfs(r, c))
    return best


if __name__ == "__main__":
    g1 = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
          [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
          [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    print(max_area_of_island(g1))            # Expected: 6

    g2 = [[0, 0, 0, 0], [0, 0, 0, 0]]
    print(max_area_of_island(g2))            # Expected: 0

"""
Pattern: Grid Graph / Islands (flood fill that returns region size).
Technique: same connected-component DFS as Number of Islands, but instead of just
counting components the recursion returns the area (1 + sum of neighbor areas),
and we keep the maximum over all islands.
Why: marking each visited cell ensures every land cell contributes to exactly one
island's area; the per-island totals are compared to find the largest.

| Metric | Value     |
|--------|-----------|
| Time   | O(m * n)  |
| Space  | O(m * n)  |   recursion stack worst case

Better Possible?
No — every cell must be examined once. Iterative BFS/DFS or Union-Find with a size
array achieves the same complexity while avoiding deep recursion on large inputs.
"""
