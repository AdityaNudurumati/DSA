# Greedy

Pattern-based roadmap for **greedy algorithms**. Each numbered folder is one pattern with a
`notes.txt` (sub-pattern tree, template, problems checklist). When built out, a pattern is split
into sub-folders — same structure as [../1.Arrays](../1.Arrays/) … [../12.DynamicProgramming](../12.DynamicProgramming/).

> The greedy mindset: find a **local rule** and prove it's **safe** with an exchange argument. If
> you can't argue it, suspect DP. FAANG focus: Interval, Jump Game, Resource Allocation,
> Scheduling, String, Greedy+Heap.
>
> Greedy overlaps heavily with built sections — those are **cross-referenced**: Intervals →
> [../1.Arrays/7.intervals](../1.Arrays/7.intervals/); Jump/Gas/Candy → [../1.Arrays/10.greedy](../1.Arrays/10.greedy/);
> String greedy → [../2.Strings/9.greedy](../2.Strings/9.greedy/); Connect Ropes/Huffman/Task Scheduler →
> [../9.Heap/5.greedy_heap](../9.Heap/5.greedy_heap/); Remove K Digits → [../1.Arrays/9.monotonic_stack](../1.Arrays/9.monotonic_stack/).

## Patterns

Built **self-contained**. Patterns 5 (Merge Cost) and 7 (String Greedy) are fully cross-referenced
to Heap and Strings respectively.

| #  | Pattern | Folder | Status |
|----|---------|--------|--------|
| 1  | Interval Greedy | [1.interval](1.interval/) | 1 problem (Activity Selection) + cross-refs |
| 2  | Scheduling Greedy | [2.scheduling](2.scheduling/) | 1 problem (Job Sequencing) |
| 3  | Resource Allocation | [3.resource_allocation](3.resource_allocation/) | 1 problem (Car Pooling) + cross-refs |
| 4  | Jump Game Pattern | [4.jump_game](4.jump_game/) | 1 problem (Jump Game III) + cross-ref |
| 5  | Merge Cost / Huffman | [5.merge_cost](5.merge_cost/) | cross-ref → Heap |
| 6  | Sorting Greedy | [6.sorting](6.sorting/) | 2 problems (Assign Cookies, Lemonade Change) |
| 7  | String Greedy | [7.string](7.string/) | cross-ref → Strings |
| 8  | Array Greedy | [8.array](8.array/) | 1 problem (Wiggle Subsequence) + cross-refs |
| 9  | Greedy + Heap | [9.heap](9.heap/) | 2 problems (IPO, Furthest Building) |
| 10 | Monotonic Greedy | [10.monotonic](10.monotonic/) | 1 problem (Monotone Increasing Digits) + cross-refs |
| 11 | Exchange Argument | [11.exchange_argument](11.exchange_argument/) | 2 problems (Fractional Knapsack, Hire K Workers) |
| 12 | Advanced Greedy | [12.advanced](12.advanced/) | 1 problem (The Skyline Problem) + cross-refs |

**Total: 13 problems**, every file runnable and verified.

See [notes.txt](notes.txt) for the full roadmap tree, the greedy mindset, and cross-references.

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
✅ <the greedy rule and why it's safe>

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
python "13.Greedy\<folder>\<file>.py"
```

Or open the file in VS Code and press `Ctrl+F5` (Run Without Debugging).
