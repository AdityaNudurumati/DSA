'''
2. Stream of Characters (Hard)  [LC1032]
Problem Statement

Design a data structure that accepts a stream of characters and checks, after
each new character, whether some word from a given list is a SUFFIX of the
characters queried so far.

Implement query(c): append character c to the stream and return True if any
word equals a suffix of the current stream, otherwise False.

The trick: store the words REVERSED in a trie. Then for each query, walk the
stream backwards (most recent char first) through the trie; if we ever land on
a word-end node, a word is a suffix of the stream.

Input:
words = ["cd", "f", "kl"]
queries = 'a','b','c','d','e','f'

Output:
[False, False, False, True, False, True]

Explanation:
After 'd' the stream ends with "cd" -> True. After 'f' the stream ends with
"f" -> True. All other queries have no word as a suffix.
'''


# Trie node holding reversed words.
class TrieNode:
    def __init__(self):
        self.children = {}     # char -> TrieNode
        self.is_word = False   # marks end of a (reversed) word


class StreamChecker:
    def __init__(self, words):
        self.root = TrieNode()
        self.stream = []                       # characters seen so far
        self.max_len = max(len(w) for w in words)  # cap backward walk
        # Insert each word reversed.
        for w in words:
            node = self.root
            for ch in reversed(w):
                node = node.children.setdefault(ch, TrieNode())
            node.is_word = True

    def query(self, c):
        self.stream.append(c)
        node = self.root
        # Walk the stream backwards, at most max_len characters.
        for i in range(len(self.stream) - 1, max(-1, len(self.stream) - self.max_len - 1), -1):
            ch = self.stream[i]
            if ch not in node.children:
                return False
            node = node.children[ch]
            if node.is_word:
                return True
        return False


if __name__ == "__main__":
    words = ["cd", "f", "kl"]
    sc = StreamChecker(words)
    results = [sc.query(c) for c in ['a', 'b', 'c', 'd', 'e', 'f']]
    print(results)  # Expected: [False, False, False, True, False, True]


'''
Pattern
✅ Reversed-word Trie (suffix matching on a growing stream)
A suffix of the stream is a prefix when both are read right-to-left. By storing
words reversed in a trie and walking the stream backwards on each query, suffix
matching becomes ordinary prefix descent. Bounding the walk by the longest word
length keeps each query cheap regardless of how long the stream grows.

| Metric | Value      |
| ------ | ---------- |
| Time   | O(L) /query|
| Space  | O(m + S)   |

L = length of longest word, m = total length of all words, S = stream length.

Better Possible?
❌ Not asymptotically
Each query must inspect up to L trailing characters to confirm a suffix, so
O(L) per query is optimal. (Stream storage can be trimmed to the last L chars
to bound memory, but the per-query cost is unchanged.) An Aho-Corasick
automaton over reversed words could also drop the per-query loop to amortized
O(1) transitions, but the worst-case work to confirm a match is still O(L).
'''
