'''
Rat in a Maze (Hard)
Problem Statement

Given an N x N maze where 1 is an open cell and 0 is blocked, a rat starts at
the top-left (0,0) and must reach the bottom-right (N-1,N-1). It may move Down,
Left, Right, Up to adjacent open cells without revisiting a cell.

Return the sorted list of all path strings, where each move is encoded as one
of 'D', 'L', 'R', 'U'.

Example:
Input:
maze = [[1,0,0,0],
        [1,1,0,1],
        [1,1,0,0],
        [0,1,1,1]]

Output:
["DDRDRR", "DRDDRR"]
'''


def find_paths(maze):
    n = len(maze)
    result = []
    visited = [[False] * n for _ in range(n)]
    # ordered so generated paths are lexicographically friendly
    moves = [("D", 1, 0), ("L", 0, -1), ("R", 0, 1), ("U", -1, 0)]

    def backtrack(r, c, path):
        if r == n - 1 and c == n - 1:     # reached destination
            result.append(path)
            return
        visited[r][c] = True              # mark current cell
        for ch, dr, dc in moves:
            nr, nc = r + dr, c + dc
            if (0 <= nr < n and 0 <= nc < n and
                    maze[nr][nc] == 1 and not visited[nr][nc]):
                backtrack(nr, nc, path + ch)
        visited[r][c] = False             # restore on backtrack

    if maze and maze[0][0] == 1:
        backtrack(0, 0, "")
    return sorted(result)


if __name__ == "__main__":
    maze = [[1, 0, 0, 0],
            [1, 1, 0, 1],
            [1, 1, 0, 0],
            [0, 1, 1, 1]]
    print(find_paths(maze))
    # Expected: ['DDRDRR', 'DRDDRR']


'''
Pattern
✅ Grid Backtracking (visited marking + restore)
We DFS from the start, marking cells visited to prevent cycles and unmarking on
the way back so every distinct simple path to the goal is recorded.
| Metric | Value     |
| ------ | --------- |
| Time   | O(4^(N*N)) |
| Space  | O(N*N)    |
Better Possible?
❌ No

Enumerating all paths is inherently exponential; the visited grid prunes cycles
but the path count can still grow exponentially.
'''
