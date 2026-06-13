# Heap / Priority Queue

Pattern-based roadmap for **heaps and priority queues**. Each numbered folder is one pattern
with a `notes.txt` (sub-pattern tree, template, problems checklist). When built out, a pattern is
split into sub-folders — same structure as [../1.Arrays](../1.Arrays/) … [../8.Recursion](../8.Recursion/).

> `heapq` is a **min-heap**; negate for a max-heap, or push `(priority, item)` tuples. The five
> highest-ROI patterns: **Top-K, K-Way Merge, Dual Heap, Greedy+Heap, Graph+Heap (Dijkstra)**.
>
> Overlap: Kth Largest / Top K Frequent / Median from Data Stream / Merge K Sorted live in
> [../1.Arrays/11.advanced/1.heap](../1.Arrays/11.advanced/1.heap/), [../6.LinkedList/4.merge](../6.LinkedList/4.merge/),
> [../1.Arrays/6.hashing](../1.Arrays/6.hashing/); Meeting Rooms II in [../1.Arrays/7.intervals](../1.Arrays/7.intervals/);
> Task Scheduler / Reorganize String in greedy. Those are **cross-referenced**. The new material
> is **Graph+Heap** (Dijkstra/Prim — first graph algorithms here), K Closest, Smallest Range,
> Sliding Window Median, Huffman, Connect Ropes, Min Platforms, Design Twitter, and lazy deletion.

## Patterns

Built **self-contained**. Pattern 7 (Range) is fully cross-referenced (Smallest Range → K-Way
Merge, Sliding Window Median → Dual Heap). Graph files define their own adjacency/edge inputs.

| #  | Pattern | Folder | Status |
|----|---------|--------|--------|
| 1  | Top-K Pattern | [1.top_k](1.top_k/) | 1 new (K Closest Points) + cross-refs |
| 2  | K-Way Merge | [2.k_way_merge](2.k_way_merge/) | 2 problems (Kth in Matrix, Smallest Range) |
| 3  | Streaming | [3.streaming](3.streaming/) | 1 new (Kth Largest in Stream) + cross-refs |
| 4  | Dual Heap | [4.dual_heap](4.dual_heap/) | 1 new (Sliding Window Median) + cross-ref |
| 5  | Greedy + Heap | [5.greedy_heap](5.greedy_heap/) | 2 new (Connect Ropes, Huffman) + cross-refs |
| 6  | Interval + Heap | [6.interval_heap](6.interval_heap/) | 1 new (Min Platforms) + cross-ref |
| 7  | Range Problems | [7.range](7.range/) | cross-ref → k-way-merge / dual-heap |
| 8  | Graph + Heap | [8.graph_heap](8.graph_heap/) | 4 problems (Network Delay, Min Effort, Cheapest Flights, Prim's MST) |
| 9  | Design Problems | [9.design](9.design/) | 2 problems (Design Twitter, Priority Queue) |
| 10 | Advanced Techniques | [10.advanced](10.advanced/) | 1 problem (Deletable Heap / lazy deletion) |

**Total: 15 problems**, every file runnable and verified.

See [notes.txt](notes.txt) for the full roadmap tree, learning order, and cross-references.

## How to add a problem

1. Pick the right pattern folder (and sub-folder once built out).
2. Create `N.problem_name.py` (N = next number in that folder).
3. Follow the file template below. Graph files define their own adjacency-list input.
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

import heapq

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
python "9.Heap\<folder>\<file>.py"
```

Or open the file in VS Code and press `Ctrl+F5` (Run Without Debugging).
