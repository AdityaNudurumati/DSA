'''
502. IPO (Hard)
Problem Statement

You are given n projects. Project i has a pure profit profits[i] and a minimum
capital capital[i] needed to start it. Initially you have w capital. Whenever you
finish a project its profit is added to your capital (profits stack on top of w).

You can complete at most k distinct projects. Pick the projects to maximize your
final capital, and return that maximum.

Input:
k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]

Output:
4

Explanation:
With w=0 only project 0 (capital 0) is affordable -> take profit 1, w=1.
Now projects 1 and 2 (capital 1) are affordable -> take the bigger profit 3, w=4.
Two projects done. Final capital = 4.
'''

import heapq


def findMaximizedCapital(k, w, profits, capital):
    # Greedy rule: at each of the k rounds, do the single most-profitable project
    # that is currently affordable. Sort projects by capital so we can "unlock"
    # newly-affordable ones as w grows; keep their profits in a max-heap.
    #
    # Why it's safe: completing a project never decreases w, so the set of
    # affordable projects only grows over time. Therefore grabbing the largest
    # available profit now never blocks any project we could have taken instead
    # (that project stays available later, and our capital is >= what it would
    # otherwise be). An exchange argument confirms no other choice beats taking
    # the current max-profit affordable project.

    projects = sorted(zip(capital, profits))  # ascending by capital
    n = len(projects)
    affordable = []  # max-heap of profits (store negatives)
    i = 0

    for _ in range(k):
        # unlock every project whose capital requirement we can now meet
        while i < n and projects[i][0] <= w:
            heapq.heappush(affordable, -projects[i][1])
            i += 1
        if not affordable:
            break  # nothing affordable -> stop early
        w += -heapq.heappop(affordable)  # take the best profit

    return w


if __name__ == "__main__":
    print(findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]))  # Expected: 4
    print(findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2]))  # Expected: 6


'''
Pattern
Greedy + Heap
Greedy rule: in each round take the affordable project with the largest profit.
Why safe: capital is monotonically non-decreasing, so any project affordable now
stays affordable later; taking the current max profit can only raise (never lower)
the capital available for future rounds -> exchange argument holds.

| Metric | Value          |
| ------ | -------------- |
| Time   | O(n log n)     |
| Space  | O(n)           |

Better Possible?
No. We must sort by capital (O(n log n)) and each project is pushed/popped once.
Sorting lower bound makes O(n log n) optimal for comparison-based approaches.
'''
