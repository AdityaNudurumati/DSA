# Strings

Pattern-based roadmap for string problems. Each numbered folder is one pattern with a
`notes.txt` (sub-pattern tree, templates, and a problems checklist). When a pattern is
built out, it's split into sub-folders (one per sub-pattern), each holding one runnable
`.py` per problem — same structure as [../1.Arrays](../1.Arrays/).

## Patterns

| #  | Pattern | Folder | Status |
|----|---------|--------|--------|
| 1  | Two Pointers | [1.two_pointers](1.two_pointers/) | 10 problems (opposite_ends ×4, same_direction ×3, in_place ×3) |
| 2  | Sliding Window | [2.sliding_window](2.sliding_window/) | 7 problems (fixed ×2, variable ×3, frequency ×2) |
| 3  | Hashing / Frequency | [3.hashing](3.hashing/) | 9 problems (char_freq ×5, hashmap ×2, set ×2) |
| 4  | Pattern Matching | [4.pattern_matching](4.pattern_matching/) | 7 problems (kmp ×3, rabin_karp ×2, z ×2) |
| 5  | Palindrome Techniques | [5.palindrome](5.palindrome/) | 3 problems (expand_center ×2, manacher ×1) |
| 6  | String Construction | [6.construction](6.construction/) | 8 problems (builder ×3, simulation ×3, encode_decode ×2) |
| 7  | Trie | [7.trie](7.trie/) | 6 problems (prefix ×3, word_dict ×2, autocomplete ×1) |
| 8  | Stack on Strings | [8.stack](8.stack/) | 7 problems (brackets ×3, remove_dups ×2, decode ×2) |
| 9  | Greedy on Strings | [9.greedy](9.greedy/) | 5 problems (rearrange ×2, lexicographical ×2, partition ×1) |
| 10 | Dynamic Programming | [10.dynamic_programming](10.dynamic_programming/) | 10 problems (lcs ×2, edit ×3, palindromic ×2, subseq ×3) |
| 11 | Rolling Hash / Advanced | [11.rolling_hash](11.rolling_hash/) | 4 problems (double_hash ×2, substring_search ×1, optimization ×1) |

**Total: 76 problems**, every file runnable and verified.

See [notes.txt](notes.txt) for the full roadmap tree and trigger phrases.

## How to add a problem

1. Pick the right pattern folder (and sub-folder once it's built out).
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

def solution(...):
    ...


if __name__ == "__main__":
    # quick sanity check
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
python "2.Strings\<folder>\<file>.py"
```

Or open the file in VS Code and press `Ctrl+F5` (Run Without Debugging).
