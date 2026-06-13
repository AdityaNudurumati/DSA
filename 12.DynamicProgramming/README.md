# Dynamic Programming

Pattern-based roadmap for **dynamic programming**. Each numbered folder is one pattern with a
`notes.txt` (sub-pattern tree, template, problems checklist). When built out, a pattern is split
into sub-folders — same structure as [../1.Arrays](../1.Arrays/) … [../11.Trie](../11.Trie/).

> The DP recipe: **State → Transition → Base case → Memoize → Tabulate → Optimize**. FAANG focus:
> Linear, Grid, Knapsack, Sequence (LCS/LIS), Stock, Partition, Tree.
>
> DP overlaps with several built sections — those are **cross-referenced**:
> Fibonacci/Climbing/Robber/Coin/Unique-Paths → [../8.Recursion/4.memoization](../8.Recursion/4.memoization/);
> LCS/Edit/Distinct/Wildcard/Regex/PalPartition-II → [../2.Strings/10.dynamic_programming](../2.Strings/10.dynamic_programming/);
> House Robber III/Cameras → [../7.Trees/11.tree_dp](../7.Trees/11.tree_dp/);
> Longest Increasing Path/Largest Color Value → [../10.Graphs/14.graph_dp](../10.Graphs/14.graph_dp/);
> Jump Game VI/Constrained Subseq → [../5.Queue/4.monotonic_deque](../5.Queue/4.monotonic_deque/).

## Patterns

Built **self-contained**. Pattern 14 (DP + Monotonic Queue) is fully cross-referenced to Queue/Strings.

| #  | Pattern | Folder | Status |
|----|---------|--------|--------|
| 0  | Fundamentals | [0.fundamentals](0.fundamentals/) | 1 problem (Fibonacci — all 4 forms) |
| 1  | Linear DP (1D) | [1.linear](1.linear/) | 2 problems (Decode Ways, Min Cost Climbing) |
| 2  | Sequence DP | [2.sequence](2.sequence/) | 3 problems (LIS, Number of LIS, Russian Doll) + LCS cross-ref |
| 3  | Grid DP | [3.grid](3.grid/) | 5 problems (Unique Paths II, Min Path, Dungeon, Falling Path, Triangle) |
| 4  | Knapsack DP | [4.knapsack](4.knapsack/) | 5 problems (subset sum, target sum, 0/1, coin change II, comb sum IV) |
| 5  | Decision DP | [5.decision](5.decision/) | 3 problems (Delete & Earn, Stone Game, Predict Winner) |
| 6  | Partition DP | [6.partition](6.partition/) | 2 problems (Matrix Chain, Partition for Max Sum) |
| 7  | Interval DP | [7.interval](7.interval/) | 3 problems (Burst Balloons, Remove Boxes, Cut Stick) |
| 8  | Stock DP | [8.stock](8.stock/) | 6 problems (I–IV, Cooldown, Fee) |
| 9  | Tree DP | [9.tree](9.tree/) | 2 problems (Sum of Distances/rerooting, Max Independent Set) |
| 10 | Bitmask DP | [10.bitmask](10.bitmask/) | 2 problems (TSP, Partition to K Equal Sum) |
| 11 | Digit DP | [11.digit](11.digit/) | 2 problems (Count Digit One, Count Special Integers) |
| 12 | Graph DP | [12.graph](12.graph/) | 1 problem (Increasing Paths in Grid) + cross-ref |
| 13 | Probability DP | [13.probability](13.probability/) | 2 problems (Knight Probability, Soup Servings) |
| 14 | DP + Monotonic Queue | [14.monotonic_queue](14.monotonic_queue/) | cross-ref → Queue/Strings |
| 15 | DP Optimization | [15.optimization](15.optimization/) | 2 problems (space-opt demo, SOS DP) |

**Total: 41 problems**, every file runnable and verified.

See [notes.txt](notes.txt) for the full roadmap tree, the DP recipe, and cross-references.

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
✅ <which DP and why — state / transition / base>

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
python "12.DynamicProgramming\<folder>\<file>.py"
```

Or open the file in VS Code and press `Ctrl+F5` (Run Without Debugging).
