'''
51. N-Queens (Hard)
Problem Statement

The n-queens puzzle is the problem of placing n queens on an n x n chessboard
so that no two queens attack each other (no shared row, column, or diagonal).

Return the number of distinct solutions to the n-queens puzzle. (We also print
one valid board for n = 4.)

Example:
Input:
n = 4

Output:
2
'''


def totalNQueens(n):
    cols = set()
    diag = set()        # r - c constant along a "\" diagonal
    anti = set()        # r + c constant along a "/" diagonal
    count = 0

    def backtrack(row):
        nonlocal count
        if row == n:                      # placed a queen in every row
            count += 1
            return
        for c in range(n):
            if c in cols or (row - c) in diag or (row + c) in anti:
                continue                  # square attacked -> prune
            cols.add(c); diag.add(row - c); anti.add(row + c)
            backtrack(row + 1)
            cols.remove(c); diag.remove(row - c); anti.remove(row + c)

    backtrack(0)
    return count


def one_solution(n):
    # build a single valid board as a list of "..Q." strings
    cols, diag, anti = set(), set(), set()
    placement = []

    def backtrack(row):
        if row == n:
            return True
        for c in range(n):
            if c in cols or (row - c) in diag or (row + c) in anti:
                continue
            cols.add(c); diag.add(row - c); anti.add(row + c)
            placement.append(c)
            if backtrack(row + 1):
                return True
            cols.remove(c); diag.remove(row - c); anti.remove(row + c)
            placement.pop()
        return False

    backtrack(0)
    return ["".join("Q" if col == c else "." for col in range(n))
            for c in placement]


if __name__ == "__main__":
    print(totalNQueens(4))  # Expected: 2
    print(totalNQueens(1))  # Expected: 1
    # one valid board for n = 4
    for row in one_solution(4):
        print(row)
    # Expected:
    # .Q..
    # ...Q
    # Q...
    # ..Q.


'''
Pattern
✅ Constraint Satisfaction Backtracking
Place one queen per row; three sets (column, "\" diagonal r-c, "/" diagonal r+c)
give O(1) attack checks so conflicting squares are pruned immediately.
| Metric | Value  |
| ------ | ------ |
| Time   | O(n!)  |
| Space  | O(n)   |
Better Possible?
❌ No

Row-by-row placement with diagonal pruning is the standard optimal approach;
the search space is inherently factorial.
'''
