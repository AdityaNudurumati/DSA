# Stack

Pattern-based roadmap for the **stack** data structure. Each numbered folder is one pattern
with a `notes.txt` (sub-pattern tree, template, problems checklist). When built out, a pattern
is split into sub-folders — same structure as [../1.Arrays](../1.Arrays/),
[../2.Strings](../2.Strings/), [../3.Hashing](../3.Hashing/).

> Stack overlaps heavily with existing work. The **monotonic-stack core** (NGE I/II, Daily
> Temperatures, Sum of Subarray Minimums, Largest Rectangle, Trapping Rain Water) lives in
> [../1.Arrays/9.monotonic_stack](../1.Arrays/9.monotonic_stack/), and **brackets / decode /
> calculator II / remove-dups** live in [../2.Strings/8.stack](../2.Strings/8.stack/). Those are
> **cross-referenced**, not duplicated. The material **unique** to this section: Basic Stack,
> Range/Span (Online Stock Span, Visible People), Maximal Rectangle, Expression Handling,
> Min/Max/Frequency Stack, Simplify Path, Asteroid Collision, Design (Stack↔Queue), and
> Sum of Subarray Ranges.

## Patterns

Built **self-contained** (each category implements its problems here). Pattern 2 is a
concept hub — its problems live in patterns 3/4/5/11.

| #  | Pattern | Folder | Status |
|----|---------|--------|--------|
| 1  | Basic Stack Operations | [1.basic_operations](1.basic_operations/) | 2 problems (Implement Stack, Baseball Game) |
| 2  | Monotonic Stack | [2.monotonic_stack](2.monotonic_stack/) | concept hub → patterns 3/4/5/11 |
| 3  | Nearest Element | [3.nearest_element](3.nearest_element/) | 5 problems (NGE I/II, next/prev smaller, prev greater) |
| 4  | Range / Span | [4.range_span](4.range_span/) | 3 problems (Online Stock Span, Daily Temps, Visible People) |
| 5  | Histogram / Rectangle | [5.histogram](5.histogram/) | 2 problems (Largest Rectangle, Maximal Rectangle) |
| 6  | Parentheses / Brackets | [6.parentheses](6.parentheses/) | 3 problems (Valid, Longest Valid, Min Remove) |
| 7  | Expression Handling | [7.expression](7.expression/) | 6 problems (RPN, Calc I/II/III, Infix→Postfix/Prefix) |
| 8  | Min / Max Stack | [8.min_max_stack](8.min_max_stack/) | 3 problems (Min, Max, Frequency) |
| 9  | Stack Simulation | [9.simulation](9.simulation/) | 4 problems (Decode, Simplify Path, Asteroids, Dedup) |
| 10 | Design Problems | [10.design](10.design/) | 3 problems (Stack↔Queue, Browser History) |
| 11 | Advanced Monotonic | [11.advanced_monotonic](11.advanced_monotonic/) | 3 problems (Subarray Min, Subarray Ranges, Rain Water) |

**Total: 34 problems**, every file runnable and verified.

See [notes.txt](notes.txt) for the full roadmap tree, learning order, and cross-references.

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
python "4.Stack\<folder>\<file>.py"
```

Or open the file in VS Code and press `Ctrl+F5` (Run Without Debugging).
