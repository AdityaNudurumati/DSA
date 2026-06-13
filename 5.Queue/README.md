# Queue / Deque

Pattern-based roadmap for **queues, deques, and BFS**. Each numbered folder is one pattern
with a `notes.txt` (sub-pattern tree, template, problems checklist). When built out, a pattern
is split into sub-folders — same structure as [../1.Arrays](../1.Arrays/) … [../4.Stack](../4.Stack/).

> Three ideas cover almost every question here: **Queue → BFS / arrival order**,
> **Deque → sliding windows & 0-1 BFS**, **Priority Queue → order by priority**.
>
> Overlap: Sliding Window Maximum lives in [../1.Arrays/2.sliding_window](../1.Arrays/2.sliding_window/3.monotonic_window/),
> Queue↔Stack design in [../4.Stack/10.design](../4.Stack/10.design/), and the priority-queue
> problems (Kth Largest, Top K, Meeting Rooms II, Task Scheduler) across Arrays/Strings — those are
> **cross-referenced**. The **unique** material is all the BFS (level-order, multi-source, 0-1,
> bidirectional, state), Circular Queue/Deque, Sliding Window Minimum, and scheduling problems.

## Patterns

Built **self-contained** (BFS/tree/graph files define their own minimal inputs). Pattern 7
(Design) is fully covered by cross-references to [../4.Stack/10.design](../4.Stack/10.design/) and
patterns 1/3 here.

| #  | Pattern | Folder | Status |
|----|---------|--------|--------|
| 1  | Basic FIFO Processing | [1.basic_fifo](1.basic_fifo/) | 4 problems (queue impl ×2, stream ×2) |
| 2  | Level Order / BFS | [2.bfs](2.bfs/) | 7 problems (tree ×3, graph ×1, grid ×3) |
| 3  | Circular Queue | [3.circular_queue](3.circular_queue/) | 2 problems (Circular Queue, Circular Deque) |
| 4  | Monotonic Deque | [4.monotonic_deque](4.monotonic_deque/) | 3 problems (Jump Game VI, SW Min, Shortest Subarray) |
| 5  | Double Ended Queue | [5.deque](5.deque/) | 1 problem (Front-Middle-Back Queue) |
| 6  | Scheduling | [6.scheduling](6.scheduling/) | 2 problems (Dota2 Senate, Buy Tickets) |
| 7  | Design Problems | [7.design](7.design/) | cross-ref → Stack + patterns 1/3 |
| 8  | Priority Queue / Heap | [8.priority_queue](8.priority_queue/) | 1 new (Single-Threaded CPU) + cross-refs |
| 9  | Advanced BFS | [9.advanced_bfs](9.advanced_bfs/) | 4 problems (Open the Lock, Genetic Mutation, Word Ladder, 0-1 BFS) |

**Total: 24 problems**, every file runnable and verified.

See [notes.txt](notes.txt) for the full roadmap tree, learning order, and cross-references.

## How to add a problem

1. Pick the right pattern folder (and sub-folder once built out).
2. Create `N.problem_name.py` (N = next number in that folder).
3. Follow the file template below. BFS files define their own minimal TreeNode / adjacency / grid inputs.
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
python "5.Queue\<folder>\<file>.py"
```

Or open the file in VS Code and press `Ctrl+F5` (Run Without Debugging).
