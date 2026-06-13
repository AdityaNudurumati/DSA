'''
1. Implement Trie with Delete (Medium)
Problem Statement

Design a trie (prefix tree) that supports four operations:
- insert(word): add a word into the trie
- search(word): return True only if the exact word was inserted before
- startsWith(prefix): return True if any inserted word begins with prefix
- delete(word): remove the word; prune nodes that are no longer part of any word

Example
Input:
insert("apple")
search("apple")    -> True
search("app")      -> False
startsWith("app")  -> True
insert("app")
search("app")      -> True
delete("apple")
search("apple")    -> False
search("app")      -> True
startsWith("app")  -> True

Output:
True, False, True, True, False, True, True
'''


class TrieNode:

    def __init__(self):
        self.children = {}   # char -> TrieNode
        self.end = False     # True if a word ends at this node


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            # create the child node if this edge does not exist yet, then descend
            node = node.children.setdefault(ch, TrieNode())
        node.end = True                       # mark the final node as a complete word

    def _find(self, prefix):
        # walk down following prefix, return the node we land on or None
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def search(self, word):
        node = self._find(word)
        # word exists only if we reached a node AND it was marked as word-end
        return node is not None and node.end

    def startsWith(self, prefix):
        # prefix exists if we can simply walk the whole prefix
        return self._find(prefix) is not None

    def delete(self, word):
        # recursive prune: unmark the end, then drop any node left with no children
        def _prune(node, i):
            if i == len(word):
                node.end = False              # unmark; node may still hold a prefix
            else:
                ch = word[i]
                child = node.children.get(ch)
                if child is None:
                    return False              # word not present, nothing to prune
                if _prune(child, i + 1):
                    del node.children[ch]     # child is now empty -> remove the edge
            # this node is safe to delete if it ends no word and has no children
            return not node.end and not node.children

        _prune(self.root, 0)


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))      # Expected: True
    print(trie.search("app"))        # Expected: False
    print(trie.startsWith("app"))    # Expected: True
    trie.insert("app")
    print(trie.search("app"))        # Expected: True
    trie.delete("apple")
    print(trie.search("apple"))      # Expected: False
    print(trie.search("app"))        # Expected: True
    print(trie.startsWith("app"))    # Expected: True


'''
Pattern
✅ Trie (Prefix Tree) + recursive pruning delete — share common prefixes so each op
   costs the word length, and on delete unwind bottom-up removing only nodes that no
   longer end a word and have no children (so "app" survives after deleting "apple").

| Metric | Value                                  |
| ------ | -------------------------------------- |
| Time   | O(L) per op, L = length of word/prefix |
| Space  | O(total characters inserted)           |

Better Possible?
A hash set answers insert/search/delete in O(L) too, but cannot answer startsWith
without scanning every key. The trie is optimal when prefix queries are needed; the
pruning delete keeps space proportional to the words actually stored.
'''
