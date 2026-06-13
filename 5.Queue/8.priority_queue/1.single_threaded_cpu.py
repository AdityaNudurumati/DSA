'''
1834. Single-Threaded CPU (Medium)
Problem Statement

You are given n tasks where tasks[i] = [enqueueTime_i, processingTime_i].
A single CPU processes them under these rules:
  - A task can only start once its enqueueTime has passed (i.e. time >= enqueueTime).
  - If the CPU is idle and no task is available, it stays idle until the next task arrives.
  - When the CPU is free and tasks are available, it picks the one with the
    smallest processingTime; ties are broken by the smaller original index.
  - Once started, a task runs to completion without interruption.
Return the order in which the tasks are processed.

Example
Input:
tasks = [[1,2],[2,4],[3,2],[4,1]]

Output:
[0,2,3,1]

Input:
tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]

Output:
[4,3,2,0,1]
'''

import heapq

def getOrder(tasks):

    # remember each task's original index, then sort by enqueue time so we can
    # release tasks into the heap in arrival order with a single moving pointer
    indexed = sorted(range(len(tasks)), key=lambda i: tasks[i][0])

    heap = []          # min-heap of (processingTime, original_index) for available tasks
    order = []
    time = 0           # current CPU clock
    i = 0              # pointer into the enqueue-sorted task list
    n = len(tasks)

    while len(order) < n:
        # push every task that has arrived by the current time
        while i < n and tasks[indexed[i]][0] <= time:
            idx = indexed[i]
            heapq.heappush(heap, (tasks[idx][1], idx))
            i += 1

        if not heap:
            # CPU idle: jump forward to the next task's enqueue time
            time = tasks[indexed[i]][0]
            continue

        # run the smallest (processingTime, index) task to completion
        proc, idx = heapq.heappop(heap)
        time += proc
        order.append(idx)

    return order


if __name__ == "__main__":
    print(getOrder([[1, 2], [2, 4], [3, 2], [4, 1]]))                 # Expected: [0, 2, 3, 1]
    print(getOrder([[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]))       # Expected: [4, 3, 2, 0, 1]

'''
Pattern
✅ Greedy simulation with a min-heap (priority queue) keyed by (processingTime, index)

Sort task indices by enqueueTime so a single pointer releases newly-available tasks
into the heap. Whenever the CPU is free, the heap hands back the cheapest task with
the correct tie-break for free. If nothing is available, fast-forward the clock to the
next arrival instead of ticking second by second.

| Metric | Value      |
| ------ | ---------- |
| Time   | O(n log n) |
| Space  | O(n)       |

Better Possible?
No. We must look at every task and the heap pop/push is log n each; O(n log n) is
optimal for this ordering problem (it is dominated by the sort itself).
'''
