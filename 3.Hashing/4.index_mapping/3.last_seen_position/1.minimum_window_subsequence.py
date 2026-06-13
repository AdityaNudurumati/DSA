'''
1. Minimum Window Subsequence (Hard)
Problem Statement

Given strings S and T, return the smallest (leftmost on ties) substring W of S such
that T is a SUBSEQUENCE of W. If no such window exists, return "".

Example
Input:
S = "abcdebdde", T = "bde"

Output:
"bcde"
Explanation:
"bcde" is the shortest window where 'b','d','e' appear in order.
'''

def minWindow(S, T):

    n, m = len(S), len(T)
    best_start, best_len = -1, float("inf")

    i = 0
    while i < n:

        # forward pass: advance until all of T has been matched in order
        t = 0
        while i < n:
            if S[i] == T[t]:
                t += 1
                if t == m:
                    break
            i += 1
        if t < m:
            break                       # T can no longer be completed

        # backward pass from this end position to find the tightest start
        end = i
        t = m - 1
        while t >= 0:
            if S[i] == T[t]:
                t -= 1
            i -= 1
        start = i + 1                   # position where the minimal window begins

        if end - start + 1 < best_len:
            best_len = end - start + 1
            best_start = start

        i = start + 1                   # restart the search just after this start

    return "" if best_start == -1 else S[best_start:best_start + best_len]


if __name__ == "__main__":
    print(minWindow("abcdebdde", "bde"))   # Expected: "bcde"
    print(minWindow("jmeqksfrsdcmsiwvaovztaqenprpvnbstl", "u"))  # Expected: ""
    print(minWindow("abcdebdde", "bd"))    # Expected: "bcd"

'''
Pattern
✅ Two-pointer position tracking (forward to find a window, backward to minimize it)

Key Observation
A forward scan locates an end index where T is fully matched; a backward scan from
that end finds the latest start still containing T as a subsequence. Restart just
past each start to find the overall minimum.

| Metric | Value   |
| ------ | ------- |
| Time   | O(n*m) worst |
| Space  | O(1)    |

Better Possible?
A DP over dp[i][j] (end index in S matching T[:j]) also runs in O(n*m).
'''
