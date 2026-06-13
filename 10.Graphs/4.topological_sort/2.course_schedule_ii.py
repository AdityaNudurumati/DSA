'''
210. Course Schedule II (Medium)
Problem Statement

There are numCourses courses labeled 0 to numCourses-1 with prerequisite pairs
[a, b] meaning b must be taken before a.

Return any valid ordering in which to take all courses. If it is impossible
(a cycle exists), return an empty list.

Input:
numCourses = 2
prerequisites = [[1, 0]]

Output:
[0, 1]

Explanation:
Course 0 has no prerequisites, then course 1 depends on 0.
'''

from collections import deque


def find_order(num_courses, prerequisites):
    # Build graph b -> a and indegree counts.
    adj = [[] for _ in range(num_courses)]
    indeg = [0] * num_courses
    for a, b in prerequisites:
        adj[b].append(a)
        indeg[a] += 1

    # Start with all zero-indegree courses (push in ascending order for a
    # deterministic, canonical valid ordering).
    q = deque(u for u in range(num_courses) if indeg[u] == 0)
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    # Full ordering only if no cycle blocked any course.
    return order if len(order) == num_courses else []


if __name__ == "__main__":
    print(find_order(2, [[1, 0]]))                                   # Expected: [0, 1]
    print(find_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))           # Expected: [0, 1, 2, 3]


'''
Pattern
✅ Topological Sort (Kahn's BFS)
We not only check feasibility but emit an actual order. Nodes are output as
their indegree hits zero, guaranteeing every prerequisite precedes its
dependents. Many valid orders may exist; the one returned is one of them.

| Metric | Value    |
| ------ | -------- |
| Time   | O(V + E) |
| Space  | O(V + E) |

Better Possible?
❌ No. The output itself has size V and we must read all E edges, so
O(V + E) is optimal.
'''
