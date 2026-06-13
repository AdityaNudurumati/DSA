"""
676. Implement Magic Dictionary (Medium)

Problem Statement
-----------------
Design a data structure that is initialized with a list of distinct words.
Afterwards, implement a search method that, given a candidate word, returns
True if and only if you can change EXACTLY ONE character of the candidate to a
DIFFERENT character so that the result is a word currently in the dictionary.

Implement the MagicDictionary class:
    - buildDict(words): builds the dictionary from the given list of words.
    - search(word): returns True iff exactly one character changed yields a
      dictionary word.

Example
-------
Input:
    buildDict(["hello", "leetcode"])
    search("hello")      # 'hello' is in dict, but needs 0 changes -> False
    search("hhllo")      # change 'h'->'e' at index 1 gives "hello" -> True
    search("hell")       # length 4 not in dict -> False
    search("leetcoded")  # length 9 not in dict -> False
Output:
    [False, True, False, False]
"""

from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)  # char -> TrieNode
        self.end = False                        # marks a complete word


class MagicDictionary:
    def __init__(self):
        self.root = TrieNode()

    def buildDict(self, words):
        # Insert every dictionary word into the trie.
        for w in words:
            node = self.root
            for ch in w:
                node = node.children[ch]
            node.end = True

    def search(self, word):
        # DFS allowing exactly one mismatch along the path.
        def dfs(node, i, changed):
            if i == len(word):
                # Valid only if we consumed exactly one change and word ends here.
                return changed and node.end
            ch = word[i]
            for c, nxt in node.children.items():
                if c == ch:
                    # Same char: spend no change.
                    if dfs(nxt, i + 1, changed):
                        return True
                elif not changed:
                    # Different char: spend our single allowed change.
                    if dfs(nxt, i + 1, True):
                        return True
            return False

        return dfs(self.root, 0, False)


if __name__ == "__main__":
    md = MagicDictionary()
    md.buildDict(["hello", "leetcode"])
    print(md.search("hello"))      # Expected: False
    print(md.search("hhllo"))      # Expected: True
    print(md.search("hell"))       # Expected: False
    print(md.search("leetcoded"))  # Expected: False


"""
Pattern
-------
Trie + DFS with a single "edit budget".
We build a trie of the dictionary words, then walk the candidate word down the
trie. At each node we may either match the current character (no change spent)
or, if we have not yet spent our one allowed change, descend into a DIFFERENT
child (spend the change). A search succeeds only if we reach a word-end node
having spent EXACTLY one change. This neatly encodes the "exactly one substitution"
rule without generating all character-swap variants of the query.

| Metric                 | Value                                        |
|------------------------|----------------------------------------------|
| Time (buildDict)       | O(sum of word lengths)                        |
| Time (search)          | O(26 * L)  (branch at most one mismatch node) |
| Space                  | O(total chars in dictionary)                  |

Here L is the length of the searched word. The DFS only ever forks at a single
position (the one mismatch), so the branching stays bounded by the alphabet.

Better Possible?
----------------
For this exact-one-substitution rule the trie traversal is essentially optimal:
each search is O(26 * L). A simpler alternative groups words by length and
compares character-by-character (also O(26 * L) per word but O(n) per search
across n words). The trie shares common prefixes, so it scales better when many
words overlap; you cannot beat needing to read all L characters of the query.
"""
