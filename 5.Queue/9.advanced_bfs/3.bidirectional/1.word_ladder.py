'''
127. Word Ladder (Hard)
Problem Statement

Given two words beginWord and endWord, and a wordList, return the length of the
shortest transformation sequence from beginWord to endWord such that:
  - only one letter changes between adjacent words, and
  - every intermediate word exists in wordList.

Return 0 if no such sequence exists. The sequence length counts both endpoints.

Input:
begin = "hit", end = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
5

Explanation:
hit -> hot -> dot -> dog -> cog  (5 words)
'''

import string


def ladderLength(beginWord, endWord, wordList):
    words = set(wordList)
    if endWord not in words:
        return 0

    # Bidirectional BFS: maintain two frontiers, always expand the smaller one.
    front = {beginWord}
    back = {endWord}
    visited = {beginWord, endWord}
    length = 1                       # both endpoints counted

    while front and back:
        # always expand the smaller frontier to keep branching minimal
        if len(front) > len(back):
            front, back = back, front

        next_front = set()
        for word in front:
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    if c == word[i]:
                        continue
                    candidate = word[:i] + c + word[i + 1:]
                    if candidate in back:        # frontiers meet
                        return length + 1
                    if candidate in words and candidate not in visited:
                        visited.add(candidate)
                        next_front.add(candidate)
        front = next_front
        length += 1

    return 0


if __name__ == "__main__":
    print(ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # Expected: 5
    print(ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))         # Expected: 0


'''
Pattern
✅ Bidirectional BFS
Words are nodes; an edge joins words that differ by one letter. Plain BFS explores
O(b^d) nodes; searching from both ends and meeting in the middle explores
O(2 * b^(d/2)), a large saving on long ladders. We always expand whichever frontier
is smaller to keep the branching factor low.

| Metric | Value             |
| ------ | ----------------- |
| Time   | O(N * L^2 * 26)   |  N=words, L=word length (build neighbors per char)
| Space  | O(N * L)          |  word set + frontiers + visited

Better Possible?
❌ Bidirectional BFS is already the standard optimization over single-ended BFS.
Pre-building a generic-pattern adjacency map ("h*t") can speed neighbor lookup but
does not change the asymptotic complexity.
'''
