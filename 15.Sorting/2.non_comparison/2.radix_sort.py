"""
2. Radix Sort (Medium)

Problem Statement
-----------------
Sort an array of NON-NEGATIVE integers using LSD (Least Significant Digit) Radix
Sort. Sort the numbers digit by digit, from the least significant digit up to the
most significant, using a STABLE counting sort as the per-digit subroutine.

Example
    Input:  [170, 45, 75, 90, 802, 24, 2, 66]
    Output: [2, 24, 45, 66, 75, 90, 170, 802]
"""


def _counting_sort_by_digit(a, exp):
    # Stable counting sort using the digit at place value `exp` (1, 10, 100, ...).
    n = len(a)
    out = [0] * n
    cnt = [0] * 10  # digits 0..9

    for x in a:
        cnt[(x // exp) % 10] += 1

    # Prefix sums -> end-exclusive positions per digit.
    for i in range(1, 10):
        cnt[i] += cnt[i - 1]

    # Right to left keeps the sort stable across passes.
    for x in reversed(a):
        d = (x // exp) % 10
        cnt[d] -= 1
        out[cnt[d]] = x
    return out


def radix_sort(a):
    if not a:
        return []

    mx = max(a)
    exp = 1
    # One stable counting-sort pass per digit of the largest number.
    while mx // exp > 0:
        a = _counting_sort_by_digit(a, exp)
        exp *= 10
    return a


if __name__ == "__main__":
    print(radix_sort([170, 45, 75, 90, 802, 24, 2, 66]))
    # Expected: [2, 24, 45, 66, 75, 90, 170, 802]


"""
Pattern
-------
Radix Sort (LSD) — a NON-COMPARISON sort that processes keys one digit at a time,
from least to most significant. Each pass is a stable counting sort on a single
digit (base/radix b = 10 here). Because every pass is stable, ordering established
by lower digits survives while higher digits break ties, so after the last digit
the whole array is sorted.

| Metric | Value          |
|--------|----------------|
| Time   | O(d * (n + b)) |
| Space  | O(n + b)       |
| Stable | Yes            |

(n = elements, d = number of digits in the max value, b = radix/base = 10)

Better Possible?
For fixed-width integers d is constant, so this is effectively O(n) — beating the
comparison-sort Omega(n log n) bound. Choosing a larger base b reduces the number
of passes d at the cost of larger counting arrays. It assumes non-negative integer
keys; negatives or floats need extra encoding.
"""
