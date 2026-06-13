'''
207. Course Schedule (Medium)
Problem Statement

There are numCourses courses labeled 0 to numCourses-1. Some courses have
prerequisites given as pairs [a, b], meaning you must take course b before
course a.

Return True if you can finish all courses (the prerequisite graph is a DAG),
otherwise False (a cycle makes it impossible).

Input:
numCourses = 2
prerequisites = [[1, 0]]

Output:
True

Explanation:
Take 0 first, then 1. No cycle, so all courses can be finished.
'''

from collections import deque


def can_finish(num_courses, prerequisites):
    # Build adjacency list b -> a (edge from prereq to dependent course).
    adj = [[] for _ in range(num_courses)]
    indeg = [0] * num_courses
    for a, b in prerequisites:
        adj[b].append(a)
        indeg[a] += 1

    # Kahn's algorithm: repeatedly remove zero-indegree nodes.
    q = deque(u for u in range(num_courses) if indeg[u] == 0)
    taken = 0
    while q:
        u = q.popleft()
        taken += 1
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    # If we processed every course there was no cycle.
    return taken == num_courses


if __name__ == "__main__":
    print(can_finish(2, [[1, 0]]))            # Expected: True
    print(can_finish(2, [[1, 0], [0, 1]]))    # Expected: False


'''
Pattern
✅ Topological Sort (Kahn's BFS on indegrees)
We only need feasibility: a directed graph has a valid ordering iff it is
acyclic. Kahn's algorithm peels zero-indegree nodes; if it cannot process all
nodes, a cycle remains and the courses cannot be finished.

| Metric | Value    |
| ------ | -------- |
| Time   | O(V + E) |
| Space  | O(V + E) |

Better Possible?
❌ No. Every node and edge must be examined to detect a cycle, so O(V + E)
is optimal. DFS color-marking is an equivalent alternative.
'''
