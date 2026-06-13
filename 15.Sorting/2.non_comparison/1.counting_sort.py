"""
1. Counting Sort (Easy)

Problem Statement
-----------------
Sort an array of integers using Counting Sort. Tally how many times each value
occurs, then rebuild the array from those tallies. The implementation must be
STABLE (equal elements keep their original relative order).

Example
    Input:  [4, 2, 2, 8, 3, 3, 1]
    Output: [1, 2, 2, 3, 3, 4, 8]

    Input:  []
    Output: []
"""


def counting_sort(a):
    # Empty input sorts to empty.
    if not a:
        return []

    lo, hi = min(a), max(a)
    k = hi - lo + 1

    # cnt[i] = how many times value (i + lo) appears.
    cnt = [0] * k
    for x in a:
        cnt[x - lo] += 1

    # Prefix sums -> cnt[i] becomes the end index (exclusive) for that value.
    for i in range(1, k):
        cnt[i] += cnt[i - 1]

    # Place from RIGHT to LEFT to preserve stability.
    out = [0] * len(a)
    for x in reversed(a):
        cnt[x - lo] -= 1
        out[cnt[x - lo]] = x
    return out


if __name__ == "__main__":
    print(counting_sort([4, 2, 2, 8, 3, 3, 1]))  # Expected: [1, 2, 2, 3, 3, 4, 8]
    print(counting_sort([]))                      # Expected: []


"""
Pattern
-------
Counting Sort — a NON-COMPARISON sort. Instead of comparing elements, it counts
occurrences of each key in a bounded range [lo, hi], turns those counts into
prefix sums (end positions), then scatters each element into its slot. Iterating
the input from right to left while decrementing the prefix count keeps equal keys
in their original order, which is what makes it stable.

| Metric | Value      |
|--------|------------|
| Time   | O(n + k)   |
| Space  | O(n + k)   |
| Stable | Yes        |

(n = number of elements, k = value range = hi - lo + 1)

Better Possible?
No for this model: when k = O(n), O(n + k) = O(n) is already linear and beats the
Omega(n log n) lower bound of comparison sorts. It is only a win when the key range
k is not much larger than n; for huge or unbounded ranges, a comparison sort or
radix sort is preferable.
"""
