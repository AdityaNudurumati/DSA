'''
3. Flood Fill (Easy) [LC733]
Problem Statement

You are given an image represented by an m x n grid of integers, and a starting
pixel (sr, sc) plus a new color `color`.

Perform a flood fill: starting from the pixel (sr, sc), change the color of that
pixel and of any 4-directionally connected pixel that shares the SAME original
color as the start pixel, to `color`.

Return the modified image.

Example:
Input:  image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
'''


def floodFill(image, sr, sc, color):
    rows, cols = len(image), len(image[0])
    start_color = image[sr][sc]

    # nothing to do if the target color already matches (avoid infinite recursion)
    if start_color == color:
        return image

    def dfs(r, c):
        # bounds check + only fill pixels of the original connected color
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if image[r][c] != start_color:
            return
        image[r][c] = color
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    dfs(sr, sc)
    return image


if __name__ == "__main__":
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    result = floodFill(image, 1, 1, 2)
    print(result)  # Expected: [[2, 2, 2], [2, 2, 0], [2, 0, 1]]


'''
Pattern
✅ Connected Components / Flood Fill (grid DFS)
Treat the grid as a graph where same-colored adjacent pixels are neighbors. A
single DFS from the start recolors the whole connected region; the `!= start_color`
guard plus the early start==color return prevent revisiting and infinite loops.

| Metric | Value    |
| ------ | -------- |
| Time   | O(m * n) |
| Space  | O(m * n) |

Each pixel is visited at most once; space is the recursion stack, worst case the
entire grid (one solid region).

Better Possible?
❌ Asymptotically optimal: in the worst case every pixel belongs to the region
and must be recolored. BFS with an explicit queue gives the same bounds while
avoiding deep recursion on large grids.
'''
