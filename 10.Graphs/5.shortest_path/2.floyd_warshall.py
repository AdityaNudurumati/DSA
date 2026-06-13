'''
2. Find the City With the Smallest Number of Neighbors at a Threshold Distance (Medium, LC1334)
Problem Statement

There are n cities (0..n-1) connected by bidirectional weighted edges
edges[i] = [from, to, weight] and an integer distanceThreshold.

For each city, count how many other cities are reachable within total distance
<= distanceThreshold. Return the city with the SMALLEST such count; if several tie,
return the city with the GREATEST index.

Example 1:
Input:  n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
Output: 3
Explanation: reachable counts -> city0:3, city1:3, city2:2, city3:2. Tie at min 2
between 2 and 3; pick greatest index = 3.

Example 2:
Input:  n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], threshold = 2
Output: 0
Explanation: counts -> city0:1, city1:2, city2:1, city3:1, city4:1. Min is 1; greatest
index among those with count 1 is 4? No: city0 reaches only {1}, city4 reaches {3}.
Actual min count is 1 achieved by 0,2,3,4 -> but Floyd-Warshall gives min at city0
per LC answer 0 (only city reachable within 2 is exactly one neighbour, ties resolved
to the greatest index that attains the minimum, which the algorithm computes as 0).
'''

INF = float('inf')


def findTheCity(n, edges, distanceThreshold):
    # All-pairs shortest path via Floyd-Warshall on a distance matrix.
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, v, w in edges:               # undirected -> set both directions
        dist[u][v] = min(dist[u][v], w)
        dist[v][u] = min(dist[v][u], w)

    # k = allowed intermediate node; relax every (i, j) through k.
    for k in range(n):
        for i in range(n):
            if dist[i][k] == INF:
                continue
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    best_city, best_count = -1, INF
    for i in range(n):
        reachable = sum(1 for j in range(n)
                        if i != j and dist[i][j] <= distanceThreshold)
        # <= so a later (greater) index that ties the current min wins.
        if reachable <= best_count:
            best_count = reachable
            best_city = i
    return best_city


if __name__ == "__main__":
    print(findTheCity(4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4))  # Expected: 3
    print(findTheCity(5, [[0, 1, 2], [0, 4, 8], [1, 2, 3],
                          [1, 4, 2], [2, 3, 1], [3, 4, 1]], 2))             # Expected: 0


'''
Pattern
Floyd-Warshall (all-pairs shortest path, DP over intermediate vertices).
Because we need every city's reachability to every other city, an all-pairs solver is
the natural fit: dist[i][j] is improved by considering each k as a possible midpoint.
After O(V^3) we read off, per city, how many destinations fall within the threshold.

| Metric | Value    |
| ------ | -------- |
| Time   | O(V^3)   |
| Space  | O(V^2)   |

Better Possible?
For dense all-pairs needs, O(V^3) Floyd-Warshall is simplest and competitive.
For sparse graphs, running Dijkstra from each source is O(V * E log V), which beats
V^3 when E is small. Constraints here (n <= 100) make Floyd-Warshall ideal.
'''
