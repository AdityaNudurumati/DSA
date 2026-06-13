'''
1. Number of Provinces (Medium) [LC547]
Problem Statement

There are n cities. Some of them are connected, while some are not. A province
is a group of directly or indirectly connected cities and no other cities
outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the i-th
city and the j-th city are directly connected, and 0 otherwise.

Return the total number of provinces.

Example:
Input:  isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Input:  isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
'''


def numberOfProvinces(isConnected):
    n = len(isConnected)
    visited = [False] * n

    # mark every city reachable from `city` as one province
    def dfs(city):
        visited[city] = True
        for nxt in range(n):
            if isConnected[city][nxt] == 1 and not visited[nxt]:
                dfs(nxt)

    provinces = 0
    for city in range(n):
        if not visited[city]:
            provinces += 1      # new component => one traversal launch
            dfs(city)
    return provinces


if __name__ == "__main__":
    m1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(numberOfProvinces(m1))  # Expected: 2

    m2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    print(numberOfProvinces(m2))  # Expected: 3


'''
Pattern
✅ Connected Components (DFS over an adjacency matrix)
Each unvisited city starts a fresh DFS that floods its whole province; the number
of launches is the number of provinces. The matrix IS the adjacency relation.

| Metric | Value  |
| ------ | ------ |
| Time   | O(n^2) |
| Space  | O(n)   |

Time is O(n^2) because every cell of the matrix is inspected once; space O(n)
for the visited array + recursion stack.

Better Possible?
❌ Not asymptotically. With a dense matrix you must read all n^2 entries.
Union-Find gives the same O(n^2) here but with near-O(1) amortized unions.
'''
