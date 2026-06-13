'''
1. Sparse Table for Range Minimum Query (Medium)
Problem Statement

Given a STATIC integer array (no updates), answer many queries of the form
query(l, r) = minimum of arr[l..r] (inclusive) in O(1) time each.

Precompute, for every index i and every power of two 2^k, the minimum of the
block arr[i .. i + 2^k - 1]. Any range can then be covered by two (possibly
overlapping) power-of-two blocks; because min is IDEMPOTENT, overlap is harmless.

Example
Input:
arr = [1, 3, 2, 7, 9, 11, 4]
query(1, 3) -> 2
query(0, 6) -> 1
query(4, 6) -> 4
'''

class SparseTableMin:

    def __init__(self, arr):
        n = len(arr)
        self.n = n
        LOG = n.bit_length()             # number of power-of-two levels
        # sp[k][i] = min of arr[i .. i + 2^k - 1]
        self.sp = [[0] * n for _ in range(LOG)]
        self.sp[0] = arr[:]              # level 0: blocks of length 1
        for k in range(1, LOG):
            half = 1 << (k - 1)
            for i in range(n - (1 << k) + 1):
                # combine two halves of length 2^(k-1)
                self.sp[k][i] = min(self.sp[k - 1][i], self.sp[k - 1][i + half])

    def query(self, l, r):
        # largest k with 2^k <= length of [l, r]
        k = (r - l + 1).bit_length() - 1
        # two blocks of length 2^k: [l, l+2^k-1] and [r-2^k+1, r] cover [l, r]
        return min(self.sp[k][l], self.sp[k][r - (1 << k) + 1])


if __name__ == "__main__":
    st = SparseTableMin([1, 3, 2, 7, 9, 11, 4])
    print(st.query(1, 3))   # Expected: 2
    print(st.query(0, 6))   # Expected: 1
    print(st.query(4, 6))   # Expected: 4

'''
Pattern
✅ Sparse Table (idempotent RMQ on a static array)

The table holds the answer for every power-of-two length. Since min(min) of an
overlapping region equals min of the union, a query is covered by exactly two
blocks of the same power-of-two size — giving constant-time lookup. Works only
for idempotent operations (min/max/gcd/and/or) and only when the array is static.

| Metric | Value      |
| ------ | ---------- |
| Build  | O(n log n) |
| Query  | O(1)       |
| Update | not supported (rebuild O(n log n)) |
| Space  | O(n log n) |

Better Possible?
❌ For O(1) idempotent RMQ this is optimal in practice. A Segment Tree gives
O(log n) queries but supports updates; a more advanced O(n) build / O(1) query
RMQ exists (sparse table on block minima + lookup tables) but is rarely worth it.
'''
