'''
1. Aho-Corasick Multi-Pattern Matching (Hard)
Problem Statement

Given a list of patterns and a text, find every pattern that occurs as a
substring of the text. All patterns must be located in a SINGLE pass over
the text (not one search per pattern).

Build a trie of the patterns, add failure links (longest proper suffix of the
current node that is also a trie prefix) and output links, then scan the text
once following goto/failure edges and emit matches.

Input:
patterns = ["he", "she", "his", "hers"]
text = "ushers"

Output:
["he", "hers", "she"]

Explanation:
Scanning "ushers": "she" (index 1-3), "he" (index 2-3), "hers" (index 2-5).
'''

from collections import deque


# Trie node for the Aho-Corasick automaton.
class TrieNode:
    def __init__(self):
        self.children = {}      # char -> TrieNode (goto edges)
        self.fail = None        # failure link
        self.output = []        # patterns that END at this node
        self.out_link = None    # next node up the suffix chain that has output


def aho_corasick(patterns, text):
    root = TrieNode()

    # 1. Build the trie of patterns.
    for p in patterns:
        node = root
        for ch in p:
            node = node.children.setdefault(ch, TrieNode())
        node.output.append(p)

    # 2. BFS to build failure links and output links.
    root.fail = root
    q = deque()
    for child in root.children.values():
        child.fail = root          # depth-1 nodes fail to root
        q.append(child)

    while q:
        cur = q.popleft()
        for ch, nxt in cur.children.items():
            # Walk failure links until we find a node with edge ch (or hit root).
            f = cur.fail
            while f is not root and ch not in f.children:
                f = f.fail
            nxt.fail = f.children[ch] if (ch in f.children and f.children[ch] is not nxt) else root
            # Output link: nearest ancestor-by-suffix that itself outputs.
            nxt.out_link = nxt.fail if nxt.fail.output else nxt.fail.out_link
            q.append(nxt)

    # 3. Scan the text once.
    found = set()
    node = root
    for ch in text:
        # Follow failure links until ch is a valid goto edge (or we are at root).
        while node is not root and ch not in node.children:
            node = node.fail
        node = node.children.get(ch, root)
        # Collect outputs at this node and along the output-link chain.
        tmp = node
        while tmp is not None:
            for pat in tmp.output:
                found.add(pat)
            tmp = tmp.out_link

    return found


if __name__ == "__main__":
    patterns = ["he", "she", "his", "hers"]
    text = "ushers"
    print(sorted(aho_corasick(patterns, text)))  # Expected: ['he', 'hers', 'she']

    patterns2 = ["a", "ab", "bab", "bc", "bca", "c", "caa"]
    text2 = "abccab"
    print(sorted(aho_corasick(patterns2, text2)))  # Expected: ['a', 'ab', 'bc', 'c']


'''
Pattern
✅ Aho-Corasick (trie + BFS failure links, single text scan)
A plain trie only matches prefixes from the root; failure links turn the trie
into a finite automaton so that on a mismatch we jump to the longest proper
suffix already in the trie instead of restarting. Output links let us emit all
patterns ending at the current position without re-walking the failure chain.
This finds every occurrence of every pattern in one linear pass.

| Metric | Value           |
| ------ | --------------- |
| Time   | O(m + n + z)    |
| Space  | O(m)            |

m = total length of all patterns, n = length of text, z = number of matches.

Better Possible?
❌ No
Building the automaton is O(m) and we must read all n text characters, so
O(m + n + z) is optimal for multi-pattern matching. Running a separate search
per pattern would be O(n * k), strictly worse for many patterns.
'''
