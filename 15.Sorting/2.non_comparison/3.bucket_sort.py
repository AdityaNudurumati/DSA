"""
3. Bucket Sort (Medium)

Problem Statement
-----------------
Sort an array of integers using Bucket Sort. Distribute the elements into a number
of buckets based on their value range, sort each bucket, then concatenate the
buckets in order. Works best when the input is roughly uniformly distributed.

Example
    Input:  [29, 25, 3, 49, 9, 37, 21, 43]
    Output: [3, 9, 21, 25, 29, 37, 43, 49]
"""


def _insertion_sort(b):
    # Simple stable per-bucket sort, done by hand (not sorted()).
    for i in range(1, len(b)):
        key = b[i]
        j = i - 1
        while j >= 0 and b[j] > key:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = key
    return b


def bucket_sort(a):
    if not a:
        return []

    lo, hi = min(a), max(a)
    if lo == hi:
        return list(a)  # all equal -> already sorted

    n = len(a)
    span = hi - lo + 1
    # Map each value to a bucket index in [0, n-1] proportionally to its value.
    buckets = [[] for _ in range(n)]
    for x in a:
        idx = (x - lo) * (n - 1) // (span - 1) if span > 1 else 0
        buckets[idx].append(x)

    # Sort each bucket, then concatenate in bucket order.
    out = []
    for b in buckets:
        _insertion_sort(b)
        out.extend(b)
    return out


if __name__ == "__main__":
    print(bucket_sort([29, 25, 3, 49, 9, 37, 21, 43]))
    # Expected: [3, 9, 21, 25, 29, 37, 43, 49]


"""
Pattern
-------
Bucket Sort — a NON-COMPARISON distribution sort. Spread the elements across many
buckets keyed by value range, sort each (small) bucket with a cheap algorithm such
as insertion sort, then read the buckets back in order. When the data is uniformly
distributed, each bucket holds O(1) elements and the whole thing runs in linear
expected time.

| Metric | Value                                  |
|--------|----------------------------------------|
| Time   | O(n + k) average, O(n^2) worst case    |
| Space  | O(n + k)                               |
| Stable | Yes (with a stable per-bucket sort)    |

(n = elements, k = number of buckets)

Better Possible?
On uniformly distributed input the O(n) average beats comparison sorts. The catch
is the distribution assumption: skewed data can dump everything into one bucket and
degrade to O(n^2). For arbitrary data, a guaranteed O(n log n) comparison sort is
safer; bucket sort shines when you know the keys spread evenly.
"""
