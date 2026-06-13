'''
1. Count Digit One (Hard) (LC233)
Problem Statement

Given an integer n, count the total number of times the digit '1' appears
in the decimal representations of all integers from 1 to n (inclusive).

Input:
n = 13

Output:
6

Explanation:
The number 1 appears in: 1, 10, 11 (twice), 12, 13 -> 1,10,11,11,12,13 = 6 times.
'''

from functools import lru_cache


def countDigitOne(n):
    # Digit DP over the decimal digits of n.
    # We count HOW MANY '1' digits appear across all numbers in [0, n].
    if n < 0:
        return 0
    digits = list(map(int, str(n)))
    L = len(digits)

    # State:
    #   pos   -> current digit index we are choosing (0 = most significant)
    #   tight -> True if the prefix chosen so far equals n's prefix, so the
    #            current digit is upper-bounded by digits[pos]; else bounded by 9
    #   count -> number of '1's already placed in the prefix
    # We return the SUM of '1' occurrences over all completions, not a plain count.
    @lru_cache(None)
    def dp(pos, tight, count):
        # Base: all positions chosen -> this single number contributes `count` ones.
        if pos == L:
            return count
        hi = digits[pos] if tight else 9
        total = 0
        # Transition: try every digit d for this position; accumulate ones.
        for d in range(0, hi + 1):
            total += dp(pos + 1, tight and (d == hi), count + (1 if d == 1 else 0))
        return total

    return dp(0, True, 0)


if __name__ == "__main__":
    print(countDigitOne(13))   # Expected: 6
    print(countDigitOne(0))    # Expected: 0
    print(countDigitOne(100))  # Expected: 21


'''
Pattern
✅ Digit DP (memoization)
We walk n's digits left-to-right, keeping a `tight` flag for the upper bound and
an accumulator of how many '1's the prefix holds. At the leaf we return that
accumulated count, so the recursion sums '1' occurrences over every number in
[0, n]. Recurrence:
    dp(pos, tight, count) = sum over d in [0..hi] of
        dp(pos+1, tight and d==hi, count + (d==1))
    base: dp(L, *, count) = count

| Metric | Value         |
| ------ | ------------- |
| Time   | O(L * 2 * 10) |
| Space  | O(L)          |  (L = number of digits = O(log n))

Better Possible?
✅ Yes — a closed-form O(log n) place-value formula (counting how often each
position is '1') avoids the per-digit loop, but Digit DP is the general,
reusable approach for arbitrary digit properties.
'''
