# Range Query Data Structures

Pattern-based roadmap for **range queries**. Each numbered folder is one pattern with a `notes.txt`
(sub-pattern tree, template, problems checklist). When built out, a pattern is split into sub-folders
— same structure as [../1.Arrays](../1.Arrays/) … [../15.Sorting](../15.Sorting/).

> **Choosing the structure:** static + sum → prefix sum; many range updates / one query → difference
> array; point update + sum → Fenwick; range query + point update → segment tree; range update +
> range query → segment tree + lazy; static idempotent (min/max/gcd) O(1) → sparse table; offline →
> Mo's. FAANG focus: Prefix Sum, Difference Array, Fenwick, Segment Tree, basic Lazy Propagation.
>
> Overlap (cross-referenced): Prefix Sum/XOR/Diff/2D → [../1.Arrays/3.prefix_based](../1.Arrays/3.prefix_based/);
> Fenwick & Segment Tree basics → [../7.Trees/13.advanced_structures](../7.Trees/13.advanced_structures/);
> Intervals → [../1.Arrays/7.intervals](../1.Arrays/7.intervals/).

## Patterns

Built **self-contained** (structures implemented by hand). Pattern 1 (Prefix Based) is fully
cross-referenced to Arrays.

| #  | Pattern | Folder | Status |
|----|---------|--------|--------|
| 1  | Prefix Based | [1.prefix_based](1.prefix_based/) | cross-ref → Arrays/prefix_based |
| 2  | Fenwick Tree (BIT) | [2.fenwick_tree](2.fenwick_tree/) | 2 problems (core BIT, range-update-range-query) |
| 3  | Segment Tree | [3.segment_tree](3.segment_tree/) | 2 problems (range sum, range max) |
| 4  | Lazy Propagation | [4.lazy_propagation](4.lazy_propagation/) | 3 problems (range add, range assign, flight bookings) |
| 5  | Sparse Table | [5.sparse_table](5.sparse_table/) | 2 problems (RMQ, range GCD) |
| 6  | Mo's Algorithm | [6.mos_algorithm](6.mos_algorithm/) | 1 problem (distinct in range) |
| 7  | Advanced Segment Trees | [7.advanced_segment_trees](7.advanced_segment_trees/) | 2 problems (merge sort tree, persistent) |
| 8  | Interval Structures | [8.interval_structures](8.interval_structures/) | 3 problems (My Calendar I/II/III) |
| 9  | Multidimensional | [9.multidimensional](9.multidimensional/) | 1 problem (2D Fenwick) |

**Total: 16 problems**, every file runnable and verified.

See [notes.txt](notes.txt) for the full roadmap tree, the "choose the structure" guide, and cross-references.

## How to add a problem

1. Pick the right pattern folder (and sub-folder once built out).
2. Create `N.problem_name.py` (N = next number in that folder).
3. Follow the file template below.
4. Tick the box in that folder's `notes.txt` checklist.

### Per-problem file template

```python
'''
N. Problem / Structure Title (Difficulty)
Problem Statement

<what it does / asks>

Example
Input:  ...
Output: ...
'''

class Structure:
    ...


if __name__ == "__main__":
    print(...)   # Expected: ...

'''
Pattern
✅ <which structure and why>

| Metric | Value |
| ------ | ----- |
| Build  | O(?)  |
| Query  | O(?)  |
| Update | O(?)  |

Better Possible?
❌/✅ <reasoning>
'''
```

### How to run any file

```powershell
python "16.RangeQueries\<folder>\<file>.py"
```

Or open the file in VS Code and press `Ctrl+F5` (Run Without Debugging).
