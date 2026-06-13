'''
1. Count Distinct Strings (Easy)
Problem Statement

Insert a stream of strings into a trie and report how many DISTINCT strings have
been inserted. Re-inserting a string that already exists must NOT increase the count;
only the first time a string appears does it add 1 to the distinct total.

Example
Input:
insert ["abc", "abc", "abcd", "ab"]

Output:
distinct count = 3
'''

class TrieNode:
    def __init__(self):
        self.children = {}     # char -> TrieNode
        self.end_count = 0     # how many times a word ENDS exactly here


class DistinctCounter:
    def __init__(self):
        self.root = TrieNode()
        self.distinct = 0      # number of unique words seen so far

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())  # descend / create
        # only the FIRST time this exact word ends here is it a new distinct string
        if node.end_count == 0:
            self.distinct += 1
        node.end_count += 1
        return self.distinct


if __name__ == "__main__":
    counter = DistinctCounter()
    for w in ["abc", "abc", "abcd", "ab"]:
        counter.insert(w)
    print(counter.distinct)   # Expected: 3

'''
Pattern
✅ Counting Trie — keep an end_count per node. A word is "new" exactly when the node
   it ends on has end_count == 0 at insert time, so distinctness is decided in O(L)
   without storing or hashing whole words.

| Metric | Value                                       |
| ------ | ------------------------------------------- |
| Time   | O(L) per insert, L = length of the word     |
| Space  | O(total characters inserted)                |

Better Possible?
A hash set of strings also gives O(L) average insert and is simpler for plain
distinct-counting. The trie wins only when prefix/frequency queries are also needed
on the same structure, since it shares prefixes instead of storing full keys.
'''
