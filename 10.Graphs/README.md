# Graphs

Pattern-based roadmap for **graph algorithms**. Each numbered folder is one pattern with a
`notes.txt` (sub-pattern tree, template, problems checklist). When built out, a pattern is split
into sub-folders — same structure as [../1.Arrays](../1.Arrays/) … [../9.Heap](../9.Heap/).

> Every file defines its own adjacency list / edge list / grid input so it's self-contained.
> Representation cheat sheet lives in [notes.txt](notes.txt). Master through **Graph DP** for the
> majority of interview questions; SCC / Bridges / Network Flow are advanced rounds.
>
> Overlap: BFS basics (Clone Graph, Islands, Rotting Oranges, Walls & Gates) in
> [../5.Queue/2.bfs](../5.Queue/2.bfs/); state/bidirectional/0-1 BFS (Word Ladder, Open the Lock) in
> [../5.Queue/9.advanced_bfs](../5.Queue/9.advanced_bfs/); Dijkstra/Prim's/Cheapest Flights in
> [../9.Heap/8.graph_heap](../9.Heap/8.graph_heap/); Union-Find (Islands, Accounts Merge) in
> [../1.Arrays/11.advanced/6.union_find](../1.Arrays/11.advanced/6.union_find/). Those are **cross-referenced**.

## Patterns

Built **self-contained** — every file defines its own adjacency list / edge list / grid input.

| #  | Pattern | Folder | Status |
|----|---------|--------|--------|
| 1  | Traversal | [1.traversal](1.traversal/) | 3 problems (path exists, DFS, BFS) |
| 2  | Connected Components | [2.connected_components](2.connected_components/) | 3 problems (provinces, components, flood fill) |
| 3  | Cycle Detection | [3.cycle_detection](3.cycle_detection/) | 2 problems (undirected, directed) |
| 4  | Topological Sort | [4.topological_sort](4.topological_sort/) | 4 problems (course sched I/II, alien dict, MHT) |
| 5  | Shortest Path | [5.shortest_path](5.shortest_path/) | 3 problems (Bellman-Ford, Floyd-Warshall, DAG) + Dijkstra cross-ref |
| 6  | Minimum Spanning Tree | [6.mst](6.mst/) | 1 problem (Kruskal) + Prim cross-ref |
| 7  | Union Find (DSU) | [7.union_find](7.union_find/) | 2 problems (redundant connection, valid tree) |
| 8  | Bipartite Graph | [8.bipartite](8.bipartite/) | 2 problems (is bipartite, possible bipartition) |
| 9  | Multi-Source BFS | [9.multi_source_bfs](9.multi_source_bfs/) | 2 problems (01 matrix, as far from land) |
| 10 | 0-1 BFS | [10.zero_one_bfs](10.zero_one_bfs/) | 1 problem (min obstacle removal) |
| 11 | Grid Graph Problems | [11.grid_graphs](11.grid_graphs/) | 5 problems (islands, max area, regions, pacific-atlantic, shortest path) |
| 12 | Strongly Connected Comp | [12.scc](12.scc/) | 2 problems (Kosaraju, Tarjan) |
| 13 | Bridges & Articulation | [13.bridges_articulation](13.bridges_articulation/) | 2 problems (critical connections, articulation points) |
| 14 | Graph DP | [14.graph_dp](14.graph_dp/) | 2 problems (longest increasing path, largest color value) |
| 15 | State Space Search | [15.state_space](15.state_space/) | 2 problems (sliding puzzle, visit all nodes) |
| 16 | Advanced Shortest Path | [16.advanced_shortest_path](16.advanced_shortest_path/) | 1 problem (ways to arrive — Dijkstra counting) |
| 17 | Network Flow | [17.network_flow](17.network_flow/) | 2 problems (Edmonds-Karp max flow, bipartite matching) |

**Total: 39 problems**, every file runnable and verified.

See [notes.txt](notes.txt) for the full roadmap tree, representation cheat sheet, and cross-references.

## How to add a problem

1. Pick the right pattern folder (and sub-folder once built out).
2. Create `N.problem_name.py` (N = next number in that folder).
3. Follow the file template below. Define your own adjacency list / grid input.
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
python "10.Graphs\<folder>\<file>.py"
```

Or open the file in VS Code and press `Ctrl+F5` (Run Without Debugging).
