'''
1. Activity Selection (Easy)
Problem Statement

You are given a list of activities, each with a start and end time as [start, end].
A person can work on only one activity at a time. Two activities are compatible
if they do not overlap (one finishes before or exactly when the next one starts).

Return the maximum number of mutually non-overlapping activities that can be performed.

Input:
activities = [[1,2],[3,4],[0,6],[5,7],[8,9],[5,9]]

Output:
4

Explanation:
Pick [1,2], [3,4], [5,7], [8,9] -> 4 non-overlapping activities.
'''

def max_activities(activities):
    # Greedy rule: sort by END time, then repeatedly take the activity that
    # finishes earliest among those still compatible with the last picked one.
    intervals = sorted(activities, key=lambda x: x[1])

    count = 0
    prev_end = float('-inf')          # end time of last chosen activity

    for start, end in intervals:
        if start >= prev_end:         # compatible: starts after previous finishes
            count += 1
            prev_end = end            # commit to this activity

    return count


if __name__ == "__main__":
    print(max_activities([[1, 2], [3, 4], [0, 6], [5, 7], [8, 9], [5, 9]]))  # Expected: 4
    print(max_activities([[1, 3], [2, 4], [3, 5]]))                          # Expected: 2


'''
Pattern
✅ Interval Greedy (sort by end, pick earliest finisher)

Greedy rule:
Sort activities by their finishing time. Always select the activity that ends
earliest and is still compatible (its start >= last chosen end).

Why it is safe (exchange argument):
The earliest-finishing activity leaves the maximum amount of remaining time for
all future activities. If some optimal solution does NOT start with the earliest
finisher, we can swap its first activity for the earliest finisher without losing
compatibility and without reducing the count. Repeating this swap shows the greedy
choice is contained in some optimal solution, so greedy is optimal.

| Metric | Value      |
| ------ | ---------- |
| Time   | O(n log n) |  # dominated by the sort
| Space  | O(1)       |  # in-place aside from the sorted copy

Better Possible?
❌ No
Any algorithm must at least sort/order the activities by finish time; comparison
sorting is Omega(n log n). If end times were small bounded integers, a counting
sort could push the selection scan to O(n), but the general case is optimal at
O(n log n).
'''
