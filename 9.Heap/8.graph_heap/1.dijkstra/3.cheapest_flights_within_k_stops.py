"""
787. Cheapest Flights Within K Stops (Medium)

Problem Statement
-----------------
There are n cities (0..n-1) connected by flights, where flights[i] = (u, v, price)
is a directed edge. Given src, dst, and an integer k, return the cheapest price to
fly from src to dst using AT MOST k stops (i.e. at most k+1 flights). If there is
no such route, return -1.

Example
-------
Input:  n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],
        src = 0, dst = 3, k = 1
Output: 700
    (0->1->3 costs 100+600=700 with 1 stop; the cheaper 0->1->2->3=400 needs 2 stops)

Input:  n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Input:  same n/flights, src = 0, dst = 2, k = 0
Output: 500
"""

import heapq


def find_cheapest_price(n, flights, src, dst, k):
    # Build adjacency list: u -> list of (v, price)
    adj = {i: [] for i in range(n)}
    for u, v, p in flights:
        adj[u].append((v, p))

    # Heap of (cost_so_far, node, stops_used). We track stops because the same
    # node may be worth revisiting if reached with fewer stops remaining.
    pq = [(0, src, 0)]
    # best_stops[node] = fewest stops with which we have settled this node
    best_stops = {}

    while pq:
        cost, u, stops = heapq.heappop(pq)
        if u == dst:
            return cost           # min-cost heap pops cheapest valid route first
        if stops > k:
            continue              # cannot take another flight
        # Prune: if we already reached u using <= stops, this path is no better.
        if u in best_stops and best_stops[u] <= stops:
            continue
        best_stops[u] = stops
        for v, p in adj[u]:
            heapq.heappush(pq, (cost + p, v, stops + 1))
    return -1


if __name__ == "__main__":
    print(find_cheapest_price(
        4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
        0, 3, 1))                                            # Expected: 700
    print(find_cheapest_price(
        3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1))  # Expected: 200
    print(find_cheapest_price(
        3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0))  # Expected: 500


"""
Pattern
-------
Graph + Heap -> Dijkstra-style search with an extra "stops" dimension. Plain
Dijkstra is unsafe here because the global cheapest path may exceed the stop
budget, so cost alone cannot finalize a node. We expand the cheapest frontier by
cost but carry stops in the state, and the first time we pop dst we have the
cheapest route within the budget. The best_stops map prunes states that reach a
node with no fewer stops than before, keeping the search bounded.

| Metric | Value          |
|--------|----------------|
| Time   | O(E*K log(E*K))|
| Space  | O(V + E)       |

Better Possible?
----------------
Bellman-Ford limited to k+1 relaxation rounds solves it in O(K*E) time and O(V)
space with no heap, and is often preferred for this exact constraint. The heap
variant shown here matches the "Graph + Heap" pattern and is competitive.
"""
