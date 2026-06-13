'''
2. Game of Life (Medium)
Problem Statement

Given a board of 0s (dead) and 1s (live), compute the next state per Conway's rules,
in-place. All cells update simultaneously based on their 8 neighbors:
- a live cell with < 2 or > 3 live neighbors dies
- a live cell with 2 or 3 live neighbors lives
- a dead cell with exactly 3 live neighbors becomes live

Example
Input:
board = [[0,1,0],
         [0,0,1],
         [1,1,1],
         [0,0,0]]

Output:
[[0,0,0],
 [1,0,1],
 [0,1,1],
 [0,1,0]]
'''

def gameOfLife(board):

    m, n = len(board), len(board[0])

    # 2-bit encoding: bit 0 = current state, bit 1 = next state.
    # reading "& 1" still sees the original state during the pass.
    for i in range(m):
        for j in range(n):

            live = 0
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    if di == 0 and dj == 0:
                        continue
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n:
                        live += board[ni][nj] & 1

            if board[i][j] & 1:                  # currently live
                if live == 2 or live == 3:
                    board[i][j] |= 2             # stays live
            else:                                # currently dead
                if live == 3:
                    board[i][j] |= 2             # becomes live

    # shift each cell to its next state
    for i in range(m):
        for j in range(n):
            board[i][j] >>= 1

    return board


if __name__ == "__main__":
    print(gameOfLife([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]))
    # Expected: [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]

'''
Pattern
✅ In-place Simulation with bit-encoding

Key Observation
Encode (current | next<<1) so all cells can be read in their ORIGINAL state during
the same pass; a final shift reveals the next generation. Avoids copying the board.

| Metric | Value  |
| ------ | ------ |
| Time   | O(m*n) |
| Space  | O(1)   |

Better Possible?
❌ No.
'''
