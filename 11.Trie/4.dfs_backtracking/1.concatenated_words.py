'''
472. Concatenated Words (Hard)
Problem Statement

Given an array of strings words (without duplicates), return all the
concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at
least two shorter words (not necessarily distinct) in the given array.

Example
Input:
words = ["cat","cats","catsdogcats","dog","dogcatsdog",
         "hippopotamuses","rat","ratcatdogcat"]

Output:
["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation:
"catsdogcats" = "cats" + "dog" + "cats"
"dogcatsdog"  = "dog" + "cats" + "dog"
"ratcatdogcat" = "rat" + "cat" + "dog" + "cat"
'''


class TrieNode:
    def __init__(self):
        self.children = {}     # char -> TrieNode
        self.end = False       # marks a complete word from the list


def findConcatenatedWords(words):
    root = TrieNode()

    # Build a trie of all words. Skip empty strings so they cannot act as a
    # zero-length "shorter word" and falsely split every candidate.
    def insert(word):
        node = root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.end = True

    for w in words:
        if w:
            insert(w)

    # DFS from index `start`: can word[start:] be split into >= `count` words
    # that each exist in the trie? `count` tracks how many pieces consumed so
    # far so we can require at least two total.
    memo = {}

    def dfs(word, start, count):
        if start == len(word):
            return count >= 2          # reached end using >= 2 pieces
        key = (start, count >= 2)
        if key in memo:
            return memo[key]

        node = root
        for i in range(start, len(word)):
            ch = word[i]
            if ch not in node.children:
                break                   # prune: no word continues this path
            node = node.children[ch]
            # If a word ends here, try splitting the remainder from i + 1.
            if node.end and dfs(word, i + 1, count + 1):
                memo[key] = True
                return True
        memo[key] = False
        return False

    result = []
    for w in words:
        if not w:
            continue
        memo.clear()                    # memo is per-word (indices differ)
        if dfs(w, 0, 0):
            result.append(w)
    return result


if __name__ == "__main__":
    words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog",
             "hippopotamuses", "rat", "ratcatdogcat"]
    print(sorted(findConcatenatedWords(words)))
    # Expected: ['catsdogcats', 'dogcatsdog', 'ratcatdogcat']


'''
Pattern
✅ Trie + DFS / Backtracking (with memoization)
Insert every word into a trie, then for each word walk the trie while DFS-ing
over split points. The trie lets us advance character-by-character and prune
instantly the moment a prefix is not a stored word, instead of re-hashing every
substring. Memoizing on the start index turns the exponential split search into
a per-word DP, so each suffix is solved once.

| Metric | Value      |
| ------ | ---------- |
| Time   | O(N * L^2) |
| Space  | O(N * L)   |

N = number of words, L = max word length. Building the trie is O(total chars);
each word's DFS visits O(L) start positions, each scanning up to O(L) chars.

Better Possible?
❌ Not asymptotically.
Every word must be examined and each split candidate checked. A pure hash-set +
DP solution matches this bound; the trie mainly buys early pruning and avoids
substring allocation, so O(N * L^2) is effectively optimal for this problem.
'''
