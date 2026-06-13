'''
1. Number of Islands (Medium) — Union Find
Problem Statement

Given a 2D grid of '1' (land) and '0' (water), return the number of islands. An
island is land connected 4-directionally.

(Often solved with DFS/BFS; this file shows the Union-Find approach.)

Example
Input:
grid = [["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]]

Output:
3
'''

def numIslands(grid):

    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])
    parent = list(range(m * n))
    count = sum(row.count("1") for row in grid)     # start: every land cell separate

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]           # path compression
            x = parent[x]
        return x

    def union(a, b):
        nonlocal count
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
            count -= 1                               # two islands became one

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                idx = i * n + j
                if i + 1 < m and grid[i + 1][j] == "1":
                    union(idx, (i + 1) * n + j)
                if j + 1 < n and grid[i][j + 1] == "1":
                    union(idx, i * n + (j + 1))

    return count


if __name__ == "__main__":
    print(numIslands([
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]))   # Expected: 3
    print(numIslands([
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]))   # Expected: 1

'''
Pattern
✅ Union-Find (Disjoint Set Union) with path compression

Key Observation
Start with each land cell as its own set; union with right/down land neighbors.
Each successful union merges two islands, so decrement a running island count.

| Metric | Value             |
| ------ | ----------------- |
| Time   | O(m*n * α)        | (α = inverse Ackermann, ~constant)
| Space  | O(m*n)            |

Better Possible?
DFS/BFS flood fill is also O(m*n) and simpler; DSU shines for dynamic connectivity.
'''
