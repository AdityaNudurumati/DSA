"""
1. Coordinate Compression (Medium)

Problem Statement:
Given an array of values (possibly large, sparse, or duplicated), replace each
value with its RANK among the sorted-unique values. The smallest distinct value
maps to 0, the next distinct value to 1, and so on. Equal values get equal ranks.
This keeps relative order while shrinking the value range to 0..m-1 (m = number of
distinct values) so it can index arrays / BITs / segment trees.

Prompt:
Return a new list where each element is the 0-indexed rank of the original value
in the sorted set of unique values.

Example:
    Input:  [100, 3, 100, 5, 3]
    Output: [2, 0, 2, 1, 0]      # sorted-unique = [3,5,100] -> 3:0, 5:1, 100:2
"""


def compress(values):
    # sorted(set(...)) gives the distinct values in increasing order.
    # Here sorted() is the POINT of the pattern (we need ranks), not a sort we must hand-roll.
    rank = {v: i for i, v in enumerate(sorted(set(values)))}  # value -> rank
    return [rank[v] for v in values]                          # remap every element


if __name__ == "__main__":
    print(compress([100, 3, 100, 5, 3]))  # Expected: [2, 0, 2, 1, 0]
    print(compress([40, 40, 40]))         # Expected: [0, 0, 0]
    print(compress([]))                   # Expected: []


"""
Pattern: Coordinate Compression (a Sorting-Based pattern).
Algorithm & why: take set() to drop duplicates, sorted() to order distinct values,
then enumerate to assign each its rank. The rank dict turns the final remap into O(1)
lookups. We compress because many algorithms (BIT/Fenwick, segment tree, counting)
cost O(value_range); after compression the range is just the count of distinct values,
so they become feasible even when raw values are huge or sparse — relative order, which
is all those structures need, is preserved.

| Metric | Value |
| Time   | O(n log n)  (dominated by the sort) |
| Space  | O(n)  (set + rank map + output) |
| Stable | N/A  (output is a value->rank mapping, not a reordering of elements) |

Better Possible? The O(n log n) sort is the bottleneck and is optimal for comparison-based
ranking. If values are bounded small integers you could counting-sort the distinct values
for O(n + k), but for general values O(n log n) is the best achievable.
"""
