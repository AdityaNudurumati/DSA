'''
1. Implement a Radix Tree / Compressed Trie (Hard)
Problem Statement

A Radix Tree (compressed trie / Patricia trie) collapses single-child chains so that
each edge holds a STRING label rather than a single character. This shrinks the node
count and speeds lookups. Implement insert / search / startsWith.

The key operation is the EDGE SPLIT: when inserting a word that diverges in the middle
of an existing edge label, that edge is split at the divergence point into a parent
edge (shared prefix) and a child edge (old suffix), then the new word is attached.

Implement a class with:
  - insert(word)      add a word
  - search(word)      True only if the EXACT word was inserted
  - startsWith(prefix) True if any inserted word starts with prefix

Input:
  insert ["team", "tea", "ten"]
  search "tea"        -> True
  search "te"         -> False   (inserted as prefix only, never a full word)
  startsWith "te"     -> True
  search "team"       -> True
  search "ten"        -> True

Output:
  True
  False
  True
  True
  True
'''

class RadixNode:
    def __init__(self, label=""):
        self.label = label          # edge label leading INTO this node (string)
        self.children = {}          # first-char -> RadixNode
        self.end = False            # marks end of a complete inserted word


def _common_prefix_len(a, b):
    # length of the shared leading characters of a and b
    i = 0
    while i < len(a) and i < len(b) and a[i] == b[i]:
        i += 1
    return i


class RadixTree:
    def __init__(self):
        self.root = RadixNode()     # root holds empty label

    def insert(self, word):
        node = self.root
        while word:
            first = word[0]
            if first not in node.children:
                # no edge starts with this char -> hang the whole remainder as one edge
                node.children[first] = RadixNode(word)
                node.children[first].end = True
                return
            child = node.children[first]
            cpl = _common_prefix_len(word, child.label)

            if cpl == len(child.label):
                # full edge label matched -> descend and keep consuming the word
                word = word[cpl:]
                node = child
                if not word:
                    child.end = True
                    return
            else:
                # diverge mid-label -> SPLIT the edge at cpl
                shared = child.label[:cpl]
                # new intermediate node owns the shared prefix
                mid = RadixNode(shared)
                node.children[first] = mid
                # old child keeps the remaining suffix of its label
                child.label = child.label[cpl:]
                mid.children[child.label[0]] = child
                # attach the rest of the new word (if any) under mid
                rest = word[cpl:]
                if rest:
                    leaf = RadixNode(rest)
                    leaf.end = True
                    mid.children[rest[0]] = leaf
                else:
                    mid.end = True   # new word ends exactly at the split point
                return

    def _walk(self, word):
        # walk edges consuming word; return (node, fully_consumed) or (None, False)
        node = self.root
        while word:
            first = word[0]
            if first not in node.children:
                return None, False
            child = node.children[first]
            cpl = _common_prefix_len(word, child.label)
            if cpl < len(child.label):
                # word ended inside this edge label
                if cpl == len(word):
                    return child, False   # landed mid-edge: prefix matches, no full word
                return None, False        # mismatch inside the label
            word = word[cpl:]
            node = child
        return node, True

    def search(self, word):
        node, consumed = self._walk(word)
        return node is not None and consumed and node.end

    def startsWith(self, prefix):
        node, _ = self._walk(prefix)
        return node is not None


if __name__ == "__main__":
    tree = RadixTree()
    for w in ["team", "tea", "ten"]:
        tree.insert(w)

    print(tree.search("tea"))         # Expected: True
    print(tree.search("te"))          # Expected: False
    print(tree.startsWith("te"))      # Expected: True
    print(tree.search("team"))        # Expected: True
    print(tree.search("ten"))         # Expected: True


'''
Pattern
✅ Compressed Trie (Radix Tree)
Collapse single-child chains so each edge stores a whole string. The defining trick is
the edge split: when a new word diverges partway through an edge label, break that edge
into a shared-prefix node plus the old suffix, then attach the new branch. This keeps
node count proportional to branch points (not total characters), saving memory while
preserving O(length) lookups.

| Metric | Value  |
| ------ | ------ |
| Time   | O(L)   |  L = length of the query/insert word (edge compare is linear in L)
| Space  | O(N)   |  N = total chars across distinct branch segments (<= plain trie)

Better Possible?
❌ Not asymptotically. Lookups are already O(L), the minimum needed to read the key.
A radix tree improves the CONSTANT factors and memory over a char-per-node trie by
merging chains; it is itself the space-optimized form of the trie.
'''
