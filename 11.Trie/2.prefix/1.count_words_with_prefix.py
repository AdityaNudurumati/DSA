'''
1. Count Words With Given Prefix (Medium)
Problem Statement

Design a trie that, after inserting a set of words, can report how many inserted
words start with a given prefix.
- insert(word): add a word into the trie
- countPrefix(prefix): return the number of inserted words that begin with prefix

Maintain a pass-through count on every node: while inserting, increment the count of
each node visited. The count of the node reached by walking a prefix is exactly how
many words pass through it, i.e. how many words have that prefix.

Example
Input:
insert ["apple", "app", "apricot", "banana"]
countPrefix("ap")   -> 3
countPrefix("app")  -> 2
countPrefix("b")    -> 1
countPrefix("c")    -> 0

Output:
3, 2, 1, 0
'''


class TrieNode:
    def __init__(self):
        self.children = {}   # char -> TrieNode
        self.count = 0       # how many inserted words pass through this node


class PrefixCounter:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            # create child if missing, then descend
            node = node.children.setdefault(ch, TrieNode())
            node.count += 1     # one more word passes through this node

    def countPrefix(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return 0        # no word has this prefix
            node = node.children[ch]
        return node.count       # words passing through == words with this prefix


if __name__ == "__main__":
    pc = PrefixCounter()
    for w in ["apple", "app", "apricot", "banana"]:
        pc.insert(w)
    print(pc.countPrefix("ap"))     # Expected: 3
    print(pc.countPrefix("app"))    # Expected: 2
    print(pc.countPrefix("b"))      # Expected: 1
    print(pc.countPrefix("c"))      # Expected: 0

'''
Pattern
✅ Prefix-Based Trie with pass-through counts — store a counter on each node and bump
   it on every insert step, so a prefix query is a single O(P) walk that ends on the
   node whose count already holds the answer (no subtree traversal needed).

| Metric | Value                                       |
| ------ | ------------------------------------------- |
| Time   | O(L) insert, O(P) query (L=word, P=prefix)  |
| Space  | O(total characters inserted)                |

Better Possible?
Without the per-node count you would have to DFS the prefix's subtree per query
(O(subtree)) or scan all words (O(N*L)). The pass-through count makes each query
optimal at O(P), independent of how many words match.
'''
