# Linked List

Pattern-based roadmap for the **linked list** data structure. Each numbered folder is one
pattern with a `notes.txt` (sub-pattern tree, template, problems checklist). When built out, a
pattern is split into sub-folders — same structure as [../1.Arrays](../1.Arrays/) … [../5.Queue](../5.Queue/).

> Two ideas unlock most problems: the **dummy node** (uniform head handling) and the
> **fast-slow pointer** (middle / cycle / nth-from-end). Each file defines its own minimal
> `ListNode` + `build()`/`to_list()` helpers so it's self-contained and runnable.
>
> Minimal overlap: **LRU Cache** ([../3.Hashing/8.ordered_hashing](../3.Hashing/8.ordered_hashing/))
> and **Happy Number** ([../3.Hashing/2.lookup](../3.Hashing/2.lookup/)) exist elsewhere and are
> cross-referenced; the design folder re-implements LRU by hand (HashMap + DLL) as the
> interview-expected answer.

## Patterns

Built **self-contained** — every file defines its own `ListNode` + `build`/`to_list` helpers.

| #  | Pattern | Folder | Status |
|----|---------|--------|--------|
| 1  | Basic Traversal | [1.basic_traversal](1.basic_traversal/) | 3 problems (count, search, recursive reverse) |
| 2  | Pointer Techniques | [2.pointer_techniques](2.pointer_techniques/) | 4 problems (middle, cycle, cycle II, remove Nth) |
| 3  | Reversal Pattern | [3.reversal](3.reversal/) | 4 problems (full, between, K-group, alternate-K) |
| 4  | Merge Pattern | [4.merge](4.merge/) | 2 problems (two sorted, K lists) |
| 5  | Dummy Node Pattern | [5.dummy_node](5.dummy_node/) | 2 problems (remove elements, swap pairs) |
| 6  | Intersection Pattern | [6.intersection](6.intersection/) | 1 problem (intersection of two lists) |
| 7  | List Rearrangement | [7.rearrangement](7.rearrangement/) | 4 problems (odd-even, reorder, rotate, partition) |
| 8  | Sorting Linked Lists | [8.sorting](8.sorting/) | 2 problems (sort list, insertion sort) |
| 9  | Circular Linked Lists | [9.circular](9.circular/) | 2 problems (sorted circular insert, Josephus) |
| 10 | Design Problems | [10.design](10.design/) | 3 problems (LRU, LFU, Browser History) |
| 11 | Advanced Pointer | [11.advanced_pointer](11.advanced_pointer/) | 3 problems (copy random, flatten multilevel/nested) |

**Total: 30 problems**, every file runnable and verified.

See [notes.txt](notes.txt) for the full roadmap tree, learning order, and the ListNode boilerplate.

## How to add a problem

1. Pick the right pattern folder (and sub-folder once built out).
2. Create `N.problem_name.py` (N = next number in that folder).
3. Follow the file template below. Define a minimal `ListNode` + `build`/`to_list` helpers.
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

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

def solution(head, ...):
    ...


if __name__ == "__main__":
    # build list from a Python list, run, print result as a Python list
    print(...)   # Expected: ...

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
python "6.LinkedList\<folder>\<file>.py"
```

Or open the file in VS Code and press `Ctrl+F5` (Run Without Debugging).
