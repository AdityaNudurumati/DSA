'''
2. Word Search II (Hard)
Problem Statement

Given an m x n board of characters and a list of words, return all words that can be
formed by sequentially adjacent cells (horizontally/vertically), using each cell at
most once per word.

Example
Input:
board = [["o","a","a","n"],
         ["e","t","a","e"],
         ["i","h","k","r"],
         ["i","f","l","v"]]
words = ["oath","pea","eat","rain"]

Output:
["eat","oath"]
'''

def findWords(board, words):

    # build a trie of the words; mark word ends by storing the full word
    trie = {}
    for word in words:
        node = trie
        for ch in word:
            node = node.setdefault(ch, {})
        node["#"] = word

    m, n = len(board), len(board[0])
    found = set()

    def dfs(i, j, node):
        ch = board[i][j]
        if ch not in node:
            return
        nxt = node[ch]
        if "#" in nxt:
            found.add(nxt["#"])

        board[i][j] = "*"                       # mark visited
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != "*":
                dfs(ni, nj, nxt)
        board[i][j] = ch                        # restore

    for i in range(m):
        for j in range(n):
            dfs(i, j, trie)

    return sorted(found)


if __name__ == "__main__":
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    print(findWords(board, ["oath", "pea", "eat", "rain"]))
    # Expected: ['eat', 'oath']

'''
Pattern
✅ Trie + DFS backtracking on the grid

Key Observation
A trie lets one DFS test all words at once and prune dead branches early (stop as
soon as the current path isn't a trie prefix), far better than searching each word.

| Metric | Value                  |
| ------ | ---------------------- |
| Time   | O(m*n*4^L) worst       | (L = max word length, pruned in practice)
| Space  | O(total word length)   |

Better Possible?
The trie pruning is the standard optimal approach for many words.
'''
