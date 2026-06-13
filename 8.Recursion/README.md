# Recursion

Pattern-based roadmap for **recursion & backtracking**. Each numbered folder is one pattern
with a `notes.txt` (sub-pattern tree, template, problems checklist). When built out, a pattern is
split into sub-folders — same structure as [../1.Arrays](../1.Arrays/) … [../7.Trees](../7.Trees/).

> This section is the foundation for Backtracking, Trees, Divide & Conquer, and DP. The heart of
> it is the **backtracking template** (choose → explore → un-choose, with pruning) — see
> [notes.txt](notes.txt).
>
> Overlap: **Divide & Conquer** (Count Inversions, Reverse Pairs, Majority Element, Quick Select)
> lives in [../1.Arrays/11.advanced/3.divide_conquer](../1.Arrays/11.advanced/3.divide_conquer/) and
> [partition_dutch_flag](../1.Arrays/1.two_pointer_problems/3.partition_dutch_flag/); **Tree
> Recursion** in [../7.Trees](../7.Trees/). Those are **cross-referenced**, not duplicated.

## Patterns

Built **self-contained**. Pattern 5 (Tree Recursion) is fully covered by cross-references to
[../7.Trees](../7.Trees/); pattern 3 builds only a fresh array Merge Sort and cross-refs the rest.

| #  | Pattern | Folder | Status |
|----|---------|--------|--------|
| 1  | Basic Recursion | [1.basic](1.basic/) | 5 problems (factorial, sum-N, reverse, fib, climbing) |
| 2  | Backtracking | [2.backtracking](2.backtracking/) | 13 problems (subsets, perms, combos, grid, partition, CSP) |
| 3  | Divide & Conquer | [3.divide_conquer](3.divide_conquer/) | 1 new (Merge Sort) + cross-refs → Arrays |
| 4  | Recursive DP (Memo) | [4.memoization](4.memoization/) | 5 problems (stairs, robber, coin change, fib, unique paths) |
| 5  | Tree Recursion | [5.tree_recursion](5.tree_recursion/) | cross-ref → Trees |
| 6  | Mathematical Recursion | [6.mathematical](6.mathematical/) | 3 problems (Pow, matrix-exp Fibonacci, Sqrt) |

**Total: 27 problems**, every file runnable and verified.

See [notes.txt](notes.txt) for the full roadmap tree, learning order, and the backtracking template.

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
python "8.Recursion\<folder>\<file>.py"
```

Or open the file in VS Code and press `Ctrl+F5` (Run Without Debugging).
