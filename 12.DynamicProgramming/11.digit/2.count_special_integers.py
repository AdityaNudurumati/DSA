'''
2. Count Special Integers (Hard) (LC2376)
Problem Statement

A positive integer is "special" if all of its digits are distinct.
Given a positive integer n, return the number of special integers in [1, n].

Input:
n = 20

Output:
19

Explanation:
All numbers 1..20 have distinct digits except 11, so 20 - 1 = 19.
'''

from functools import lru_cache


def countSpecialNumbers(n):
    # Digit DP over the decimal digits of n, tracking which digits are used.
    digits = list(map(int, str(n)))
    L = len(digits)

    # State:
    #   pos     -> current digit index being chosen
    #   tight   -> prefix still equals n's prefix (current digit <= digits[pos])
    #   started -> have we placed a non-leading-zero digit yet (number has begun)
    #   mask    -> bitmask of digits 0..9 already used in the started number
    # A leading zero (not started) does NOT consume a digit in the mask, so
    # short numbers (fewer digits than n) are counted correctly.
    @lru_cache(None)
    def dp(pos, tight, started, mask):
        # Base: a full-length placement is valid iff it represents a real number.
        if pos == L:
            return 1 if started else 0
        hi = digits[pos] if tight else 9
        total = 0
        # Transition: choose digit d for this position.
        for d in range(0, hi + 1):
            if not started and d == 0:
                # Still in leading zeros: number hasn't begun, mask unchanged.
                total += dp(pos + 1, tight and (d == hi), False, 0)
            else:
                if mask & (1 << d):
                    continue  # digit already used -> not "special", skip
                total += dp(pos + 1, tight and (d == hi), True, mask | (1 << d))
        return total

    return dp(0, True, False, 0)


if __name__ == "__main__":
    print(countSpecialNumbers(20))   # Expected: 19
    print(countSpecialNumbers(5))    # Expected: 5
    print(countSpecialNumbers(135))  # Expected: 110


'''
Pattern
✅ Digit DP + bitmask (memoization)
We build numbers digit-by-digit under the bound n. `started` distinguishes
leading zeros (which keep the mask empty and let shorter numbers form) from
real digits; `mask` records used digits so any repeat is pruned. At the leaf we
count the number iff it actually started. Recurrence:
    dp(pos, tight, started, mask) = sum over valid d in [0..hi] of
        dp(pos+1, tight and d==hi, started or d>0,
           mask if (leading zero) else mask | (1<<d))
    skip d when started/used and bit d already set in mask
    base: dp(L, *, started, *) = 1 if started else 0

| Metric | Value                |
| ------ | -------------------- |
| Time   | O(L * 2 * 2 * 2^10 * 10) |
| Space  | O(L * 2^10)          |  (L = number of digits = O(log n))

Better Possible?
✅ Yes — a combinatorial counting argument (permutations of distinct digits per
length plus a tight prefix walk) gives O(L * 10) without the 2^10 mask states,
but Digit DP generalizes cleanly to other digit constraints.
'''
