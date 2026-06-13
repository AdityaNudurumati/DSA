'''
1. Zigzag Conversion (Medium)
Problem Statement

The string s is written in a zigzag pattern on a given number of rows.
For example, "PAYPALISHIRING" with numRows = 3 looks like:

P   A   H   N
A P L S I I G
Y   I   R

Read the zigzag row by row to produce a new string. Return that string.

Example
Input:
s = "PAYPALISHIRING"
numRows = 3

Output:
"PAHNAPLSIIGYIR"
'''

def convert(s, numRows):
    # one row means the zigzag is just the original string
    if numRows == 1:
        return s

    rows = [[] for _ in range(numRows)]
    cur = 0          # current row index
    going_down = False

    # walk the characters, bouncing between top and bottom rows
    for ch in s:
        rows[cur].append(ch)
        if cur == 0 or cur == numRows - 1:
            going_down = not going_down   # flip direction at the edges
        cur += 1 if going_down else -1

    # concatenate rows top to bottom
    return ''.join(''.join(row) for row in rows)


if __name__ == "__main__":
    print(convert("PAYPALISHIRING", 3))  # Expected: PAHNAPLSIIGYIR
    print(convert("PAYPALISHIRING", 4))  # Expected: PINALSIGYAHRPI


'''
Pattern
✅ Simulation (walk the zigzag, bucket chars per row)
Maintain a current row and a direction that flips at the top/bottom edges;
drop each character into its row, then join the rows.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No — must visit every character; output is O(n).
'''
