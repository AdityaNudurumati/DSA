'''
1. Number of Distinct Elements in Each Range (Hard)
Problem Statement

Given a static array arr and a list of offline queries, where each query is an
inclusive range [l, r], answer for every query how many DISTINCT values appear in
arr[l..r]. All queries are known in advance (offline), so we may reorder them.

Implement distinct_in_ranges(arr, queries) using Mo's algorithm:
  - process queries in an order that minimises two-pointer movement
  - maintain a frequency table as the window [cur_l, cur_r] grows/shrinks
  - return answers in the ORIGINAL query order.

Example
Input:
  arr     = [1, 1, 2, 1, 3]
  queries = [[0, 4], [1, 3], [2, 4]]
Output:
  [3, 2, 3]
  ([0,4]->{1,2,3}=3 ; [1,3]->{1,2}=2 ; [2,4]->{2,1,3}=3)
'''


# ---- Solution: Mo's algorithm (offline range distinct-count) ----
def distinct_in_ranges(arr, queries):
    n = len(arr)
    q = len(queries)
    if n == 0 or q == 0:
        return [0] * q

    block = max(1, int(n ** 0.5))

    # Attach original index so we can restore answer order after sorting.
    order = list(range(q))
    # Sort by (block of l, then r). Alternate r direction per block ("Hilbert-lite"
    # snake order) so cur_r sweeps forward then backward, cutting total movement.
    order.sort(key=lambda i: (queries[i][0] // block,
                              queries[i][1] if (queries[i][0] // block) % 2 == 0
                              else -queries[i][1]))

    freq = [0] * (max(arr) + 1) if arr else [0]
    distinct = 0          # number of values currently with freq > 0
    answers = [0] * q

    def add(idx):
        nonlocal distinct
        v = arr[idx]
        if freq[v] == 0:
            distinct += 1
        freq[v] += 1

    def remove(idx):
        nonlocal distinct
        v = arr[idx]
        freq[v] -= 1
        if freq[v] == 0:
            distinct -= 1

    # Invariant: window currently covers [cur_l, cur_r] inclusive (empty when cur_r < cur_l).
    cur_l, cur_r = 0, -1
    for i in order:
        l, r = queries[i]
        # Expand right, expand left, then shrink — order avoids touching freq<0.
        while cur_r < r:
            cur_r += 1
            add(cur_r)
        while cur_l > l:
            cur_l -= 1
            add(cur_l)
        while cur_r > r:
            remove(cur_r)
            cur_r -= 1
        while cur_l < l:
            remove(cur_l)
            cur_l += 1
        answers[i] = distinct

    return answers


if __name__ == "__main__":
    print(distinct_in_ranges([1, 1, 2, 1, 3], [[0, 4], [1, 3], [2, 4]]))  # Expected: [3, 2, 3]
    print(distinct_in_ranges([1, 2, 3, 4], [[0, 3], [1, 1]]))             # Expected: [4, 1]
    print(distinct_in_ranges([5, 5, 5, 5], [[0, 3], [2, 2], [0, 0]]))     # Expected: [1, 1, 1]
    print(distinct_in_ranges([], [[0, 0]]))                               # Expected: [0]

'''
Pattern
Mo's Algorithm (offline range statistics via two pointers)

Technique & why
Distinct-count is not decomposable like a sum, so prefix sums / Fenwick trees do
not directly apply. But adding or removing ONE element from the current window is
O(1): bump a frequency counter and adjust the running `distinct` total when a
count crosses 0. Mo's exploits this by answering all queries offline. Sort queries
into sqrt(n)-sized blocks by their left endpoint, and within a block by right
endpoint (alternating direction to snake). Then slide cur_l / cur_r toward each
query's bounds. Across all queries cur_l moves O(Q*block) and cur_r moves
O(n) per block * O(n/block) blocks = O(n^2/block), minimised at block = sqrt(n),
giving O((N + Q) * sqrt(N)) element add/remove operations total.

| Metric                | Value             |
| --------------------- | ----------------- |
| Sort queries          | O(Q log Q)        |
| All pointer moves      | O((N + Q) sqrt N) |
| Per add/remove          | O(1)              |
| Space                  | O(N + Q + maxVal) |

Better Possible?
For OFFLINE distinct counting there is an O((N + Q) log N) approach: sort queries
by r, sweep r left-to-right keeping each value only at its latest position in a
Fenwick tree, then a query is a prefix-count from l. That beats Mo's asymptotically
for distinct-count specifically. Mo's wins on generality — it handles mode, range
frequency, and other hard-to-merge statistics with the same O(1) add/remove
skeleton, which is why it is the go-to offline tool when no clean decomposition
exists.
'''
