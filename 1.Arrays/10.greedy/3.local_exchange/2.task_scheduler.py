'''
2. Task Scheduler (Medium)
Problem Statement

Given a list of CPU tasks (letters) and a cooldown n, identical tasks must be at
least n intervals apart. Each interval runs one task or is idle. Return the minimum
number of intervals to finish all tasks.

Example
Input:
tasks = ["A","A","A","B","B","B"], n = 2

Output:
8
Explanation:
A B idle A B idle A B  -> 8 intervals.
'''

from collections import Counter

def leastInterval(tasks, n):

    counts = Counter(tasks)
    max_freq = max(counts.values())

    # how many tasks share that maximum frequency (they each need a final slot)
    max_count = sum(1 for c in counts.values() if c == max_freq)

    # frame: (max_freq - 1) full blocks of size (n + 1), plus the last row
    intervals = (max_freq - 1) * (n + 1) + max_count

    # if there are enough distinct tasks, no idling is needed
    return max(intervals, len(tasks))


if __name__ == "__main__":
    print(leastInterval(["A", "A", "A", "B", "B", "B"], 2))   # Expected: 8
    print(leastInterval(["A", "A", "A", "B", "B", "B"], 0))   # Expected: 6
    print(leastInterval(["A", "C", "A", "B", "D", "B"], 1))   # Expected: 6

'''
Pattern
✅ Greedy counting (schedule the most frequent task first)

Key Observation
The busiest task defines the frame: (max_freq - 1) gaps of length (n + 1), then a
final slot per task tied for the max. If other tasks fill all idle slots, the answer
is simply len(tasks).

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  | (at most 26 task types)

Better Possible?
❌ No.
'''
