"""
91. Decode Ways (Medium)

Problem Statement:
A message containing letters A-Z is encoded to numbers using the mapping
'A' -> "1", 'B' -> "2", ..., 'Z' -> "26".
Given a string s of digits, return the number of ways to decode it.
A leading zero, or a zero that cannot pair into a valid 10..26 group, makes
that prefix undecodable (contributes 0 ways).

Example:
    Input:  "12"
    Output: 2          # "AB" (1,2) or "L" (12)

    Input:  "226"
    Output: 3          # "BZ"(2,26), "VF"(22,6), "BBF"(2,2,6)

    Input:  "06"
    Output: 0          # leading zero -> invalid
"""


def num_decodings(s: str) -> int:
    # State: dp[i] = number of ways to decode the prefix s[:i] (first i chars).
    # Transition (rolling, look back 1 and 2 digits):
    #   if s[i-1] in '1'..'9'   -> add ways ending a 1-digit char  (prev)
    #   if "10" <= s[i-2:i] <= "26" -> add ways ending a 2-digit char (prev2)
    # Base: dp[0] = 1 (empty string has one decoding: the empty decoding).
    n = len(s)
    if n == 0:
        return 0

    prev2 = 1            # dp[i-2], starts as dp[0]
    prev = 1 if s[0] != '0' else 0   # dp[1]
    if n == 1:
        return prev

    for i in range(2, n + 1):
        cur = 0
        if s[i - 1] != '0':                 # single digit 1..9
            cur += prev
        two = s[i - 2:i]                    # two-digit window
        if "10" <= two <= "26":
            cur += prev2
        prev2, prev = prev, cur

    return prev


if __name__ == "__main__":
    print(num_decodings("12"))   # Expected: 2
    print(num_decodings("226"))  # Expected: 3
    print(num_decodings("06"))   # Expected: 0


"""
Pattern: LINEAR DP (1D) -- Fibonacci-style decode counting.
We use bottom-up tabulation reduced to two rolling variables. Each position's
count depends only on the previous one or two positions (a 1-digit or 2-digit
decode choice), exactly the dp[i] = f(dp[i-1], dp[i-2]) shape. Memoization
(top-down) would work too, but the dependency on just the last two states makes
O(1)-space tabulation the cleanest fit.

| Metric | Value |
|--------|-------|
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
No. Every digit must be examined at least once, so O(n) time is optimal, and
the two rolling variables already make space O(1).
"""
