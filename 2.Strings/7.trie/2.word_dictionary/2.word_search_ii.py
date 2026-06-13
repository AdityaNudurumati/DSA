'''
2. Word Search II (Hard)
Problem Statement

Given an m x n board of characters and a list of words, return all words that can
be formed by sequentially adjacent cells (horizontally or vertically neighbouring).
The same cell may not be used more than once within a single word.

Example
Input:
board = [["o","a","a","n"],
         ["e","t","a","e"],
         ["i","h","k","r"],
         ["i","f","l","v"]]
words = ["oath","pea","eat","rain"]

Output:
["eat","oath"]   (sorted)
'''

def findWords(board, words):

    # Build a trie of all target words. Each leaf stores the full word so that
    # when DFS reaches it we know exactly what to collect.
    root = {}
    for word in words:
        node = root
        for ch in word:
            node = node.setdefault(ch, {})
        node['#'] = word  # store the word itself at the end node

    rows, cols = len(board), len(board[0])
    found = set()

    def dfs(r, c, node):
        ch = board[r][c]
        if ch not in node:
            return                 # no trie branch -> prune this path
        nxt = node[ch]

        if '#' in nxt:
            found.add(nxt['#'])    # complete word lies on this path

        board[r][c] = '*'          # mark visited so we don't reuse the cell
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '*':
                dfs(nr, nc, nxt)
        board[r][c] = ch           # restore for other paths (backtrack)

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, root)

    return sorted(found)


if __name__ == "__main__":
    board = [["o", "a", "a", "n"],
             ["e", "t", "a", "e"],
             ["i", "h", "k", "r"],
             ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]
    print(findWords(board, words))  # Expected: ['eat', 'oath']

'''
Pattern
✅ Trie + DFS / backtracking — the trie lets one grid walk test ALL words at once and
   prunes a path the instant it stops matching any word prefix.

| Metric | Value                                                       |
| ------ | ----------------------------------------------------------- |
| Time   | O(M · N · 4^Lmax) worst, heavily pruned in practice         |
| Space  | O(total chars in words) for the trie                        |

Better Possible?
Running a separate DFS per word costs O(W · M · N · 4^L). Sharing one trie across all
words is the accepted optimal approach for this problem.
'''
