# Arrays

Pattern-based roadmap for array problems. Each numbered folder is one pattern, holding
one `.py` file per problem plus a `notes.txt` with the pattern's sub-types, templates,
and a problems checklist.

## Patterns

The **core 10** cover ~80–90% of array interviews; **#11 Advanced** is the remaining high-signal layer.

| #  | Pattern | Folder | Status |
|----|---------|--------|--------|
| 1  | Two Pointers | [1.two_pointer_problems](1.two_pointer_problems/) | 19 problems (opposite_ends ×8, same_direction ×5, partition ×6) |
| 2  | Sliding Window | [2.sliding_window](2.sliding_window/) | 8 problems (fixed ×2, variable ×4, monotonic ×2) |
| 3  | Prefix Based | [3.prefix_based](3.prefix_based/) | 7 problems (sum ×3, xor ×1, product ×1, diff ×1, 2D ×1) |
| 4  | Subarray Techniques | [4.subarray_techniques](4.subarray_techniques/) | 3 problems (kadane ×1, product ×1, circular ×1) |
| 5  | Binary Search | [5.binary_search](5.binary_search/) | 8 problems (classic ×4, search-on-answer ×2, rotated ×2) |
| 6  | Hashing | [6.hashing](6.hashing/) | 7 problems (frequency ×3, set ×3, prefix ×1) |
| 7  | Intervals | [7.intervals](7.intervals/) | 6 problems (merge ×2, insert ×1, line_sweep ×3) |
| 8  | Matrix (2D) | [8.matrix](8.matrix/) | 6 problems (traversal ×3, rotation ×1, simulation ×2) |
| 9  | Monotonic Stack | [9.monotonic_stack](9.monotonic_stack/) | 7 problems (next_greater ×3, next_smaller ×2, histogram ×2) |
| 10 | Greedy | [10.greedy](10.greedy/) | 6 problems (reachability ×2, resource ×1, local_exchange ×3) |
| 11 | Advanced | [11.advanced](11.advanced/) | 17 problems (heap ×3, bit ×3, divide&conquer ×3, sorting ×1, math ×3, union_find ×2, trie ×2) |

See [notes.txt](notes.txt) for the full roadmap and the broader 80–90% coverage map.

## How to add a problem

1. Pick the right pattern folder.
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
python "1.Arrays\<folder>\<file>.py"
```

Or open the file in VS Code and press `Ctrl+F5` (Run Without Debugging).
