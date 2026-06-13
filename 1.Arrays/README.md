# Arrays

Pattern-based roadmap for array problems. Each numbered folder is one pattern, holding
one `.py` file per problem plus a `notes.txt` with the pattern's sub-types, templates,
and a problems checklist.

## Patterns

| #  | Pattern | Folder | Status |
|----|---------|--------|--------|
| 1  | Two Pointers | [1.two_pointer_problems](1.two_pointer_problems/) | 7 problems (opposite_ends ×5, same_direction ×2) |
| 2  | Sliding Window | [2.sliding_window](2.sliding_window/) | notes only |
| 3  | Prefix Based | [3.prefix_based](3.prefix_based/) | notes only |
| 4  | Subarray Techniques | [4.subarray_techniques](4.subarray_techniques/) | notes only |
| 5  | Binary Search | [5.binary_search](5.binary_search/) | notes only |
| 6  | Hashing | [6.hashing](6.hashing/) | notes only |
| 7  | Intervals | [7.intervals](7.intervals/) | notes only |
| 8  | Matrix (2D) | [8.matrix](8.matrix/) | notes only |
| 9  | Monotonic Stack | [9.monotonic_stack](9.monotonic_stack/) | notes only |
| 10 | Greedy | [10.greedy](10.greedy/) | notes only |

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
