'''
2. Longest Repeated Substring via Suffix Trie (Hard)
Problem Statement

Given a string s, find the LONGEST substring that occurs at least twice in s
(occurrences may overlap). If none exists, return "".

Build a suffix trie of s (insert every suffix s[i:]). A substring repeats iff
its path passes through a node that is shared by >= 2 distinct suffixes — such
a node is an INTERNAL node having more than one child OR a node that itself ends
one suffix while continuing into another. The deepest such node spells the
answer. We find it with a DFS that returns the longest string built only from
"branching" prefixes (nodes from which >= 2 suffixes diverge).

Example
Input:
s = "banana"

Output:
"ana"
Explanation:
"ana" occurs at index 1 and index 3 — the longest repeat.
'''


class TrieNode:
    def __init__(self):
        self.children = {}   # char -> TrieNode
        self.count = 0       # how many inserted suffixes pass through this node


class SuffixTrie:
    def __init__(self, s):
        self.root = TrieNode()
        for i in range(len(s)):
            self._insert(s[i:])

    def _insert(self, suffix):
        node = self.root
        for ch in suffix:
            node = node.children.setdefault(ch, TrieNode())
            node.count += 1   # one more suffix uses this edge/node

    def longest_repeated(self):
        # DFS: keep descending only through nodes shared by >= 2 suffixes.
        # Such a node corresponds to a substring that appeared at least twice.
        best = ""

        def dfs(node, path):
            nonlocal best
            for ch, child in node.children.items():
                if child.count >= 2:          # this prefix repeats
                    new_path = path + ch
                    if len(new_path) > len(best):
                        best = new_path
                    dfs(child, new_path)

        dfs(self.root, "")
        return best


if __name__ == "__main__":
    print(SuffixTrie("banana").longest_repeated())   # Expected: ana
    print(SuffixTrie("abcd").longest_repeated())      # Expected:
    print(SuffixTrie("aaaa").longest_repeated())      # Expected: aaa

'''
Pattern
Suffix Trie + DFS for the deepest repeated node. Tagging each node with a count
of suffixes passing through it turns "repeated substring" into "node.count >= 2".
The deepest path made entirely of such nodes is the longest repeated substring.
Building is O(n^2); the DFS visits each node once, also O(n^2) in the worst case.

| Metric | Value  |
| ------ | ------ |
| Time   | O(n^2) |
| Space  | O(n^2) |

Better Possible?
Yes — a suffix automaton finds the longest repeated substring in O(n), and a
suffix array + LCP array does it in O(n log n) with O(n) space (the max LCP value
is exactly the answer length). Binary search + rolling hash is the common
interview alternative. The suffix trie is the most intuitive but least scalable.
'''
