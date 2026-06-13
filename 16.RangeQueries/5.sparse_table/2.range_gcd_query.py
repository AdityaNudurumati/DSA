'''
2. Range GCD Query (Medium)
Problem Statement

Given a STATIC integer array (no updates), answer many queries of the form
query(l, r) = gcd(arr[l..r]) (inclusive) in O(1) time each.

gcd is IDEMPOTENT — gcd(x, x) = x and gcd is associative/commutative — so a
Sparse Table applies directly: two overlapping power-of-two blocks cover any
range and the overlap does not corrupt the result.

Example
Input:
arr = [2, 4, 6, 8, 3]
query(0, 1) -> 2
query(0, 4) -> 1
query(1, 3) -> 2
'''

from math import gcd


class SparseTableGCD:

    def __init__(self, arr):
        n = len(arr)
        self.n = n
        LOG = n.bit_length()
        # sp[k][i] = gcd of arr[i .. i + 2^k - 1]
        self.sp = [[0] * n for _ in range(LOG)]
        self.sp[0] = arr[:]
        for k in range(1, LOG):
            half = 1 << (k - 1)
            for i in range(n - (1 << k) + 1):
                self.sp[k][i] = gcd(self.sp[k - 1][i], self.sp[k - 1][i + half])

    def query(self, l, r):
        k = (r - l + 1).bit_length() - 1
        # gcd over two overlapping blocks of length 2^k covering [l, r]
        return gcd(self.sp[k][l], self.sp[k][r - (1 << k) + 1])


if __name__ == "__main__":
    st = SparseTableGCD([2, 4, 6, 8, 3])
    print(st.query(0, 1))   # Expected: 2
    print(st.query(0, 4))   # Expected: 1
    print(st.query(1, 3))   # Expected: 2

'''
Pattern
✅ Sparse Table (idempotent range GCD on a static array)

Same construction as range-min: precompute gcd for every power-of-two block.
gcd is idempotent, so two overlapping blocks of the same size answer any query
in O(1). Note each gcd call is itself O(log V) on the value magnitude, treated
as a near-constant factor here.

| Metric | Value      |
| ------ | ---------- |
| Build  | O(n log n) |
| Query  | O(1)       |
| Update | not supported (rebuild O(n log n)) |
| Space  | O(n log n) |

Better Possible?
❌ For a static array with idempotent gcd queries this is the standard O(1)
solution. If updates were needed, a Segment Tree storing gcd gives O(log n)
query and update instead.
'''
