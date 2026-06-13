"""
4. Maximum Gap (Hard) — LC164

Problem Statement
-----------------
Given an unsorted array `nums`, return the maximum difference between two
successive elements in its sorted form. If the array contains fewer than two
elements, return 0. The algorithm must run in linear time and use linear space,
so we exploit bucket sort instead of fully sorting.

Example
    Input:  [3, 6, 9, 1]   Output: 3   (sorted [1,3,6,9], gaps 2,3,3 -> max 3)
    Input:  [10]           Output: 0   (fewer than 2 elements)
    Input:  [1, 1, 1, 1]   Output: 0   (all equal)
"""


def maximum_gap(nums):
    n = len(nums)
    if n < 2:
        return 0

    lo, hi = min(nums), max(nums)
    if lo == hi:
        return 0  # all values identical -> no gap

    # Pigeonhole idea: with n elements spanning [lo, hi], the max gap is at least
    # ceil((hi-lo)/(n-1)). Use that as bucket size so the answer is always a gap
    # BETWEEN buckets, never inside one. We then only need each bucket's min/max.
    bucket_size = max(1, (hi - lo) // (n - 1))
    bucket_count = (hi - lo) // bucket_size + 1

    bucket_min = [None] * bucket_count
    bucket_max = [None] * bucket_count
    for x in nums:
        b = (x - lo) // bucket_size
        bucket_min[b] = x if bucket_min[b] is None else min(bucket_min[b], x)
        bucket_max[b] = x if bucket_max[b] is None else max(bucket_max[b], x)

    # Walk non-empty buckets; gap = current bucket min - previous bucket max.
    max_gap = 0
    prev_max = lo
    for i in range(bucket_count):
        if bucket_min[i] is None:
            continue
        max_gap = max(max_gap, bucket_min[i] - prev_max)
        prev_max = bucket_max[i]
    return max_gap


if __name__ == "__main__":
    print(maximum_gap([3, 6, 9, 1]))   # Expected: 3
    print(maximum_gap([10]))           # Expected: 0
    print(maximum_gap([1, 1, 1, 1]))   # Expected: 0


"""
Pattern
-------
Maximum Gap — a NON-COMPARISON / bucket-sort application. The trick is the
pigeonhole principle: across n values spanning [lo, hi], the largest successive
gap is at least ceil((hi-lo)/(n-1)). If we size buckets to that floor, two numbers
in the SAME bucket can never produce the maximum gap, so we only track each
bucket's min and max. The answer is the largest jump from one non-empty bucket's
max to the next non-empty bucket's min — found in one linear pass, no full sort.

| Metric | Value  |
|--------|--------|
| Time   | O(n)   |
| Space  | O(n)   |
| Stable | N/A    |

(N/A: the routine returns a numeric gap, not a reordered array, so stability
does not apply.)

Better Possible?
No. Reading all n inputs already costs Omega(n), so the O(n) time / O(n) space
solution is optimal. A naive sort-then-scan approach is simpler but O(n log n);
the bucket method is what achieves the required linear bound.
"""
