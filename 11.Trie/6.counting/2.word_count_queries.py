'''
2. Implement Trie II — Word Count Queries (Medium) (LC 1804)
Problem Statement

Design a trie that supports counting, allowing a word to be inserted multiple times:
- insert(word): add one occurrence of word
- countWordsEqualTo(word): how many times exactly this word was inserted (minus erases)
- countWordsStartingWith(prefix): how many inserted words have this prefix
- erase(word): remove one previously-inserted occurrence of word

Example
Input:
insert("apple"); insert("apple")
countWordsEqualTo("apple")        -> 2
countWordsStartingWith("app")     -> 2
erase("apple")
countWordsEqualTo("apple")        -> 1
countWordsStartingWith("app")     -> 1

Output:
2, 2, 1, 1
'''

class TrieNode:
    def __init__(self):
        self.children = {}     # char -> TrieNode
        self.count = 0         # words PASSING THROUGH this node (prefix count)
        self.end_count = 0     # words ENDING exactly at this node


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
            node.count += 1          # one more word passes through here
        node.end_count += 1          # one more word ends here

    def _walk(self, word):
        # follow word from root, return landing node or None if any char missing
        node = self.root
        for ch in word:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def countWordsEqualTo(self, word):
        node = self._walk(word)
        return node.end_count if node else 0

    def countWordsStartingWith(self, prefix):
        node = self._walk(prefix)
        return node.count if node else 0

    def erase(self, word):
        # assume word was inserted; decrement counters along the path
        if self.countWordsEqualTo(word) == 0:
            return
        node = self.root
        for ch in word:
            child = node.children[ch]
            child.count -= 1
            # prune dead branches to keep prefix counts honest
            if child.count == 0:
                del node.children[ch]
                return
            node = child
        node.end_count -= 1


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    trie.insert("apple")
    print(trie.countWordsEqualTo("apple"))       # Expected: 2
    print(trie.countWordsStartingWith("app"))    # Expected: 2
    trie.erase("apple")
    print(trie.countWordsEqualTo("apple"))       # Expected: 1
    print(trie.countWordsStartingWith("app"))    # Expected: 1

'''
Pattern
✅ Counting Trie — store two counters per node: count (words passing through, for
   prefix queries) and end_count (words ending here, for exact-match queries). Every
   op walks one path, updating or reading counters in O(L). erase mirrors insert by
   decrementing, pruning a subtree the moment its passing-through count hits 0.

| Metric | Value                                              |
| ------ | -------------------------------------------------- |
| Time   | O(L) per operation, L = length of word/prefix      |
| Space  | O(total characters inserted)                       |

Better Possible?
A pair of hash maps (full-word counts + every-prefix counts) answers all four ops in
O(L) too, but countWordsStartingWith would need to enumerate prefixes on insert,
blowing up space to O(sum of word lengths) of distinct prefix keys. The trie shares
prefixes, giving the same time with tighter, structurally-shared storage.
'''
