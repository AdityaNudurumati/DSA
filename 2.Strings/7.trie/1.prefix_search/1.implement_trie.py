'''
1. Implement Trie (Prefix Tree) (Medium)
Problem Statement

Design a trie that supports three operations:
- insert(word): add a word into the trie
- search(word): return True only if the exact word was inserted before
- startsWith(prefix): return True if any inserted word begins with prefix

Example
Input:
insert("apple")
search("apple")    -> True
search("app")      -> False
startsWith("app")  -> True
insert("app")
search("app")      -> True

Output:
True, False, True, True
'''

class Trie:

    def __init__(self):
        # each node is a dict of child-char -> child-node; '#' marks end of a word
        self.root = {}

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})  # create child if missing, then descend
        node['#'] = True                    # mark the final node as a complete word

    def _find(self, prefix):
        # walk down following prefix, return the node we land on or None
        node = self.root
        for ch in prefix:
            if ch not in node:
                return None
            node = node[ch]
        return node

    def search(self, word):
        node = self._find(word)
        # word exists only if we reached a node AND it was marked as word-end
        return node is not None and '#' in node

    def startsWith(self, prefix):
        # prefix exists if we can simply walk the whole prefix
        return self._find(prefix) is not None


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))      # Expected: True
    print(trie.search("app"))        # Expected: False
    print(trie.startsWith("app"))    # Expected: True
    trie.insert("app")
    print(trie.search("app"))        # Expected: True

'''
Pattern
✅ Trie (Prefix Tree) — share common prefixes so lookups depend on word length, not
   on how many words are stored.

| Metric | Value                                  |
| ------ | -------------------------------------- |
| Time   | O(L) per op, L = length of word/prefix |
| Space  | O(total characters inserted)           |

Better Possible?
For exact membership a hash set gives O(L) too, but it cannot answer startsWith
without scanning every key. The trie is optimal when prefix queries are needed.
'''
