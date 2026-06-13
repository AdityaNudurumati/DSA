'''
2. Task Scheduler (Medium)
Problem Statement

Given a list of CPU tasks (each a letter) and a cooldown n, the same task must
be separated by at least n intervals. Each interval runs one task or stays idle.

Return the minimum number of intervals needed to finish all tasks.

Example
Input:  tasks = ["A","A","A","B","B","B"], n = 2
Output: 8        (A B idle A B idle A B)

Input:  tasks = ["A","A","A","B","B","B"], n = 0
Output: 6        (no cooldown, just run them all)
'''

from collections import Counter


def leastInterval(tasks, n):
    counts = Counter(tasks)
    max_count = max(counts.values())          # most frequent task
    # How many tasks share that maximum frequency (they trail the last block).
    max_count_tasks = sum(1 for c in counts.values() if c == max_count)

    # Greedy frame: (max_count - 1) full blocks of width (n + 1), then a final
    # block holding every task tied for the max frequency.
    frame = (max_count - 1) * (n + 1) + max_count_tasks

    # If there are many distinct tasks, idle slots get filled and the answer
    # is simply the total number of tasks.
    return max(frame, len(tasks))


if __name__ == "__main__":
    print(leastInterval(["A", "A", "A", "B", "B", "B"], 2))  # Expected: 8
    print(leastInterval(["A", "A", "A", "B", "B", "B"], 0))  # Expected: 6


'''
Pattern
✅ Greedy Frequency Counting
The schedule length is driven by the most frequent task; build a frame around
it and clamp to the total task count when idle slots vanish.
| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |
(O(1) extra: counter holds at most 26 letters)
Better Possible?
❌ No. Must read every task once; the closed-form frame is already O(n).
'''
