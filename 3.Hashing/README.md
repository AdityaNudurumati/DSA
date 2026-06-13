# Hashing

Pattern-based roadmap for the **hashing technique**. Each numbered folder is one pattern
with a `notes.txt` (sub-pattern tree, template, problems checklist). When built out, a
pattern is split into sub-folders — same structure as [../1.Arrays](../1.Arrays/) and
[../2.Strings](../2.Strings/).

> Hashing cuts across data structures, so several patterns here overlap with work already
> done in Arrays/Strings. Those are **cross-referenced, not duplicated** — see each
> folder's `notes.txt` and the [roadmap](notes.txt). The material unique to this section
> is **Index Mapping (#4)**, **Ordered Hashing (#8, LRU/LFU)**, and **Hash Design (#9)**.

## Patterns

Built as a **self-contained** section: every category implements its problems here through
the hashing lens. Problems that also appear under multiple categories are written once and
cross-linked within this section (e.g. Two Sum, Contains Duplicate).

| #  | Pattern | Folder | Status |
|----|---------|--------|--------|
| 1  | Frequency Counting | [1.frequency_counting](1.frequency_counting/) | 6 problems (char ×3, element ×2, top-k ×1) |
| 2  | Lookup / Existence | [2.lookup](2.lookup/) | 3 problems (complement ×1, membership ×2) |
| 3  | Set-Based Hashing | [3.set_based](3.set_based/) | 3 problems (unique ×1, consecutive ×1, dedup ×1) |
| 4  | Index Mapping | [4.index_mapping](4.index_mapping/) | 3 problems (value→idx ×2, last-seen ×1) |
| 5  | Grouping Pattern | [5.grouping](5.grouping/) | 2 problems (by-signature ×2) |
| 6  | Prefix Hashing | [6.prefix_hashing](6.prefix_hashing/) | 4 problems (sum ×1, xor ×1, modulo ×2) |
| 7  | Sliding Window + Hashing | [7.sliding_window](7.sliding_window/) | 4 problems (freq ×2, char-track ×2) |
| 8  | Ordered Hashing | [8.ordered_hashing](8.ordered_hashing/) | 2 problems (LRU ×1, first-unique ×1) |
| 9  | Hash Design | [9.design](9.design/) | 3 problems (HashMap, HashSet, Consistent Hashing) |
| 10 | Rolling Hash | [10.rolling_hash](10.rolling_hash/) | 3 problems (rabin-karp ×1, string-hash ×1, dup-substring ×1) |

**Total: 33 problems**, every file runnable and verified.

See [notes.txt](notes.txt) for the full roadmap tree and cross-references.

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
python "3.Hashing\<folder>\<file>.py"
```

Or open the file in VS Code and press `Ctrl+F5` (Run Without Debugging).
