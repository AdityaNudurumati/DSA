'''
1. Add and Search Word — Data Structure Design (Medium)
Problem Statement

Design a dictionary that supports adding words and searching them, where the
search string may contain the wildcard '.' that matches ANY single character.

- addWord(word): store a word
- search(word): return True if any stored word matches; '.' matches one char

Example
Input:
addWord("bad"); addWord("dad"); addWord("mad")
search("pad")  -> False
search("bad")  -> True
search(".ad")  -> True
search("b..")  -> True

Output:
False, True, True, True
'''

class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word):
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node['#'] = True  # end-of-word marker

    def search(self, word):

        def dfs(node, i):
            # matched all characters -> success only if this node ends a word
            if i == len(word):
                return '#' in node

            ch = word[i]
            if ch == '.':
                # wildcard: try every child branch
                for key, child in node.items():
                    if key != '#' and dfs(child, i + 1):
                        return True
                return False
            else:
                # normal char: must exist, then continue down it
                if ch not in node:
                    return False
                return dfs(node[ch], i + 1)

        return dfs(self.root, 0)


if __name__ == "__main__":
    wd = WordDictionary()
    for w in ["bad", "dad", "mad"]:
        wd.addWord(w)
    print(wd.search("pad"))   # Expected: False
    print(wd.search("bad"))   # Expected: True
    print(wd.search(".ad"))   # Expected: True
    print(wd.search("b.."))   # Expected: True

'''
Pattern
✅ Trie + DFS backtracking — a literal char follows one edge; a '.' branches into
   every child, exploring all possibilities recursively.

| Metric | Value                                                   |
| ------ | ------------------------------------------------------- |
| Time   | O(L) no wildcard; up to O(26^d · L) with d dots         |
| Space  | O(total chars) trie + O(L) recursion stack              |

Better Possible?
Without wildcards a hash set matches in O(L). The branching DFS over a trie is the
standard optimum once '.' wildcards are allowed.
'''
