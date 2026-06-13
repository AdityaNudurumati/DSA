"""
773. Sliding Puzzle (Hard)

Problem Statement
-----------------
On a 2x3 board there are 5 tiles labeled 1..5 and one empty square labeled 0.
A move swaps the 0 with an adjacent (up/down/left/right) tile. The board is
solved when it equals [[1,2,3],[4,5,0]]. Return the least number of moves
required to solve the board, or -1 if it is unsolvable.

Example
-------
Input:  [[1,2,3],[4,0,5]]
Output: 1            (swap the 0 and the 5)

Input:  [[1,2,3],[5,4,0]]
Output: -1           (no sequence of moves solves it)

Input:  [[4,1,2],[5,0,3]]
Output: 5
"""

from collections import deque


def sliding_puzzle(board):
    goal = "123450"
    # Flatten the 2x3 board into a 6-char string (row-major) as the state.
    start = "".join(str(v) for row in board for v in row)

    # For each index of the 0 in the flat string, list the indices it can swap with.
    # Layout indices:  0 1 2
    #                  3 4 5
    neighbors = {
        0: (1, 3),
        1: (0, 2, 4),
        2: (1, 5),
        3: (0, 4),
        4: (1, 3, 5),
        5: (2, 4),
    }

    # BFS over board states; each legal swap is an edge of weight 1.
    q = deque([(start, 0)])
    seen = {start}
    while q:
        state, steps = q.popleft()
        if state == goal:
            return steps
        z = state.index("0")
        for nb in neighbors[z]:
            lst = list(state)
            lst[z], lst[nb] = lst[nb], lst[z]
            nxt = "".join(lst)
            if nxt not in seen:
                seen.add(nxt)
                q.append((nxt, steps + 1))
    return -1


if __name__ == "__main__":
    print(sliding_puzzle([[1, 2, 3], [4, 0, 5]]))  # Expected: 1
    print(sliding_puzzle([[1, 2, 3], [5, 4, 0]]))  # Expected: -1
    print(sliding_puzzle([[4, 1, 2], [5, 0, 3]]))  # Expected: 5


"""
Pattern
-------
State Space Search / Puzzle BFS. Each distinct board configuration is a node and
each legal swap of the blank tile with a neighbor is an edge. Because every move
has unit cost, plain BFS from the start state finds the fewest moves to reach the
goal; the first time the goal string is dequeued, its depth is the answer. The
board is encoded as a 6-character string so states hash cheaply into a `seen` set.
There are at most 6! = 720 reachable states, half of which are unsolvable parity
classes, so the search is tiny and bounded.

| Metric | Value                    |
|--------|--------------------------|
| Time   | O((R*C)! * (R*C))        |
| Space  | O((R*C)!)                |

Better Possible?
For this fixed 2x3 board the state space is constant (<= 720 nodes), so BFS is
effectively O(1). For larger n-puzzles, A* with an admissible heuristic
(Manhattan distance) or IDA* explores far fewer states, but plain BFS is the
canonical and simplest correct solution here.
"""
