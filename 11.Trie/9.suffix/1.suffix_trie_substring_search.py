'''
1. Substring Search via Suffix Trie (Medium)
Problem Statement

Build a SUFFIX TRIE of a string s by inserting every suffix s[i:] into a trie.
Once built, answer queries of the form "is t a substring of s?" in O(len(t)).
Key fact: t is a substring of s  iff  t is a PREFIX of some suffix of s, i.e.
iff t spells out a valid path from the root of the suffix trie.

Example
Input:
s = "banana"
queries = ["ana", "nan", "xyz", "banana", ""]

Output:
[True, True, False, True, True]
Explanation:
"ana", "nan" and the whole "banana" are substrings; "" is trivially present
(empty path); "xyz" never appears.
'''


class TrieNode:
    def __init__(self):
        self.children = {}   # char -> TrieNode


class SuffixTrie:
    def __init__(self, s):
        self.root = TrieNode()
        # insert all suffixes s[i:]; every substring becomes a root path
        for i in range(len(s)):
            self._insert(s[i:])

    def _insert(self, suffix):
        node = self.root
        for ch in suffix:
            node = node.children.setdefault(ch, TrieNode())

    def contains(self, t):
        # substring exists iff t is a path from the root
        node = self.root
        for ch in t:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True


if __name__ == "__main__":
    st = SuffixTrie("banana")
    print(st.contains("ana"))      # Expected: True
    print(st.contains("nan"))      # Expected: True
    print(st.contains("xyz"))      # Expected: False
    print(st.contains("banana"))   # Expected: True
    print(st.contains(""))         # Expected: True

'''
Pattern
Suffix Trie. Insert every suffix s[i:] so that the set of all root-to-node paths
equals the set of all substrings of s. A substring query then degenerates to a
plain prefix walk: follow t character by character; success iff the path exists.
Building costs O(n^2) work/space (n suffixes, up to n chars each), but each query
is only O(len(t)) regardless of n.

| Metric | Value  |
| ------ | ------ |
| Time   | build O(n^2), query O(m) |
| Space  | O(n^2) |

Better Possible?
A suffix automaton or suffix array (with LCP) supports the same substring queries
in O(n) space and O(n) or O(n log n) build, scaling to large strings where the
O(n^2) suffix trie blows up. The trie wins only on conceptual simplicity.
'''
