# Trie

Pattern-based roadmap for the **trie (prefix tree)** and related string structures. Each numbered
folder is one pattern with a `notes.txt` (sub-pattern tree, template, problems checklist). When
built out, a pattern is split into sub-folders — same structure as [../1.Arrays](../1.Arrays/) … [../10.Graphs](../10.Graphs/).

> FAANG focus: **Basic Trie, Prefix Problems, Word Dictionary, Word Search II, Bitwise Trie**.
> Compressed/suffix/Aho-Corasick are advanced / competitive.
>
> Overlap: Implement Trie, LCP, Replace Words, Add & Search Word, Word Search II, Search
> Suggestions all live in [../2.Strings/7.trie](../2.Strings/7.trie/); Maximum XOR of Two Numbers in
> [../1.Arrays/11.advanced/7.trie](../1.Arrays/11.advanced/7.trie/). Those are **cross-referenced**. The new
> material: Trie Delete, Prefix Count, **XOR Queries**, Counting Trie, **Kth Lexicographical**,
> Radix/Compressed Trie, Suffix Trie, and **Aho-Corasick**.

## Patterns

Built **self-contained**. Patterns 1–5 add new variants and cross-reference the existing basics in
`2.Strings/7.trie` and `1.Arrays/11.advanced/7.trie`.

| #  | Pattern | Folder | Status |
|----|---------|--------|--------|
| 1  | Basic Operations | [1.basic](1.basic/) | 1 new (Trie with Delete) + cross-ref |
| 2  | Prefix-Based Problems | [2.prefix](2.prefix/) | 1 new (Count Words With Prefix) + cross-refs |
| 3  | Dictionary / Word Lookup | [3.dictionary](3.dictionary/) | 1 new (Magic Dictionary) + cross-refs |
| 4  | Trie + DFS / Backtracking | [4.dfs_backtracking](4.dfs_backtracking/) | 1 new (Concatenated Words) + cross-ref |
| 5  | Bitwise Trie | [5.bitwise](5.bitwise/) | 2 problems (Max XOR With Element, Min XOR Pair) |
| 6  | Counting Trie | [6.counting](6.counting/) | 2 problems (Count Distinct, Trie II queries) |
| 7  | Lexicographical Trie | [7.lexicographical](7.lexicographical/) | 2 problems (Lexicographical Numbers, Kth Lexicographical) |
| 8  | Compressed Trie | [8.compressed](8.compressed/) | 1 problem (Radix Tree) |
| 9  | Suffix Trie | [9.suffix](9.suffix/) | 2 problems (substring search, longest repeated substring) |
| 10 | Advanced String Structures | [10.advanced](10.advanced/) | 2 problems (Aho-Corasick, Stream of Characters) |

**Total: 15 problems**, every file runnable and verified.

See [notes.txt](notes.txt) for the full roadmap tree, the core node, and cross-references.

## How to add a problem

1. Pick the right pattern folder (and sub-folder once built out).
2. Create `N.problem_name.py` (N = next number in that folder).
3. Follow the file template below.
4. Tick the box in that folder's `notes.txt` checklist.

### Per-problem file template

```python
'''
N. Problem Title (Difficulty)
Problem Statement

<what the problem asks>

Example
Input:  ...
Output: ...
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

def solution(...):
    ...


if __name__ == "__main__":
    print(solution(...))   # Expected: ...

'''
Pattern
✅ <which pattern and why>

| Metric | Value |
| ------ | ----- |
| Time   | O(?)  |
| Space  | O(?)  |

Better Possible?
❌/✅ <reasoning>
'''
```

### How to run any file

```powershell
python "11.Trie\<folder>\<file>.py"
```

Or open the file in VS Code and press `Ctrl+F5` (Run Without Debugging).
