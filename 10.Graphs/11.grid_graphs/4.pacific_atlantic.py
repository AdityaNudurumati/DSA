"""
417. Pacific Atlantic Water Flow (Medium)

Problem Statement:
There is an m x n rectangular island that borders both the Pacific Ocean (top and
left edges) and the Atlantic Ocean (bottom and right edges). Given an m x n matrix
heights of cell heights, water can flow from a cell to a 4-directionally adjacent
cell with height less than or equal to the current cell's height. Return a list of
coordinates [r, c] such that rain water can flow from that cell to BOTH oceans.

Example:
    Input:  heights = [[1,2,2,3,5],
                       [3,2,3,4,4],
                       [2,4,5,3,1],
                       [6,7,1,4,5],
                       [5,1,1,2,4]]
    Output: (sorted) [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]   (7 cells)
"""


def pacific_atlantic(heights):
    # Reverse flow: from each ocean's border cells, climb to neighbors with height
    # >= current (water could have flowed down to us). Cells reachable from both
    # oceans can drain to both.
    if not heights or not heights[0]:
        return []
    m, n = len(heights), len(heights[0])
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    pacific, atlantic = set(), set()

    def dfs(r, c, visited):
        visited.add((r, c))
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if (0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited
                    and heights[nr][nc] >= heights[r][c]):
                dfs(nr, nc, visited)          # climb uphill (reverse of flow)

    for r in range(m):
        dfs(r, 0, pacific)                    # left edge -> Pacific
        dfs(r, n - 1, atlantic)               # right edge -> Atlantic
    for c in range(n):
        dfs(0, c, pacific)                    # top edge -> Pacific
        dfs(m - 1, c, atlantic)               # bottom edge -> Atlantic

    return sorted([r, c] for (r, c) in pacific & atlantic)


if __name__ == "__main__":
    heights = [[1, 2, 2, 3, 5],
               [3, 2, 3, 4, 4],
               [2, 4, 5, 3, 1],
               [6, 7, 1, 4, 5],
               [5, 1, 1, 2, 4]]
    res = pacific_atlantic(heights)
    print(res)        # Expected: [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
    print(len(res))   # Expected: 7

"""
Pattern: Grid Graph / Multi-source reverse DFS (reachability from two sources).
Technique: instead of simulating downhill flow from every cell, start from the
ocean borders and traverse "uphill" (to neighbors with height >= current). A cell
in the Pacific-reachable set can drain to the Pacific; the intersection of the two
reachable sets are the cells draining to both oceans.
Why: reversing the inequality turns "can this cell reach an ocean?" into "is this
cell reachable from an ocean?", letting two flood fills replace per-cell searches.

| Metric | Value     |
|--------|-----------|
| Time   | O(m * n)  |
| Space  | O(m * n)  |   two visited sets + recursion stack

Better Possible?
No — each cell is visited O(1) times per ocean, so O(m*n) is optimal; a naive
per-cell DFS to the oceans would be O((m*n)^2).
"""
