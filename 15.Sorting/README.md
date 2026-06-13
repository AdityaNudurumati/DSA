# Sorting

Pattern-based roadmap for **sorting algorithms and sorting-based techniques**. Each numbered
folder is one pattern with a `notes.txt` (sub-pattern tree, template, problems checklist). When
built out, a pattern is split into sub-folders — same structure as [../1.Arrays](../1.Arrays/) … [../14.BitManipulation](../14.BitManipulation/).

> Comparison sorts have an Ω(n log n) lower bound; counting/radix/bucket beat it by exploiting
> bounded keys. Stability matters for multi-key sorts.
>
> Overlap (cross-referenced): Merge Sort → [../8.Recursion/3.divide_conquer](../8.Recursion/3.divide_conquer/) &
> [../6.LinkedList/8.sorting](../6.LinkedList/8.sorting/); Quick Select → [../1.Arrays/.../partition_dutch_flag](../1.Arrays/1.two_pointer_problems/3.partition_dutch_flag/);
> Inversion Count → [../1.Arrays/11.advanced/3.divide_conquer](../1.Arrays/11.advanced/3.divide_conquer/);
> Topological Order → [../10.Graphs/4.topological_sort](../10.Graphs/4.topological_sort/);
> Largest Number / Sort by Frequency → Arrays / Strings.

## Patterns

Built **self-contained** — algorithms implemented by hand; sort+X applications cross-referenced.

| #  | Pattern | Folder | Status |
|----|---------|--------|--------|
| 1  | Comparison Based | [1.comparison](1.comparison/) | 6 problems (bubble, selection, insertion, merge, quick, heap) |
| 2  | Non-Comparison | [2.non_comparison](2.non_comparison/) | 4 problems (counting, radix, bucket, Maximum Gap) |
| 3  | Sorting-Based Patterns | [3.sort_patterns](3.sort_patterns/) | 1 problem (Coordinate Compression) + cross-refs |
| 4  | Custom Sorting | [4.custom](4.custom/) | 3 problems (Relative Sort, Custom Sort String, multi-key) |
| 5  | Stability Concepts | [5.stability](5.stability/) | 2 problems (stable-vs-unstable, two-pass stable) |
| 6  | Advanced Applications | [6.advanced](6.advanced/) | 1 problem (External Sort / k-way merge) + cross-refs |

**Total: 17 problems**, every file runnable and verified.

See [notes.txt](notes.txt) for the full roadmap tree, the complexity cheat sheet, and cross-references.

## How to add a problem

1. Pick the right pattern folder (and sub-folder once built out).
2. Create `N.problem_name.py` (N = next number in that folder).
3. Follow the file template below.
4. Tick the box in that folder's `notes.txt` checklist.

### Per-problem file template

```python
'''
N. Problem / Algorithm Title (Difficulty)
Problem Statement

<what it does / asks>

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
✅ <which sort / technique and why>

| Metric | Value |
| ------ | ----- |
| Time   | O(?)  |
| Space  | O(?)  |
| Stable | yes/no |

Better Possible?
❌/✅ <reasoning>
'''
```

### How to run any file

```powershell
python "15.Sorting\<folder>\<file>.py"
```

Or open the file in VS Code and press `Ctrl+F5` (Run Without Debugging).
