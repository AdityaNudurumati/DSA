'''
2. Repeated Substring Pattern (Easy)
Problem Statement

Given a string s, check if it can be constructed by taking some substring
of it and appending multiple copies of that substring together.

Algorithm: KMP / LPS array. If the whole string is built from a repeating
block, then the longest prefix-suffix length leaves a remainder block of
size n - lps[n-1] that must divide n evenly.

Example
Input:  s = "abab"
Output: True   ("ab" repeated twice)
Input:  s = "aba"
Output: False
Input:  s = "abcabcabcabc"
Output: True   ("abc" repeated four times)
'''


def build_lps(s):
    # Standard KMP failure function over the whole string s.
    lps = [0] * len(s)
    k = 0
    for i in range(1, len(s)):
        while k and s[i] != s[k]:
            k = lps[k - 1]
        if s[i] == s[k]:
            k += 1
        lps[i] = k
    return lps


def repeatedSubstringPattern(s):
    n = len(s)
    lps = build_lps(s)
    longest = lps[n - 1]            # longest proper prefix that is also suffix
    block = n - longest            # candidate repeating block length
    # s is periodic with this block iff the block evenly tiles the string
    # AND there actually was a non-trivial border (longest > 0).
    return longest > 0 and n % block == 0


if __name__ == "__main__":
    print(repeatedSubstringPattern("abab"))          # Expected: True
    print(repeatedSubstringPattern("aba"))           # Expected: False
    print(repeatedSubstringPattern("abcabcabcabc"))  # Expected: True


'''
Pattern
KMP — the failure function exposes the string's smallest period. If the
longest border is non-empty and the leftover block length divides n, the
string is a repetition of that block.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible? No asymptotic improvement. A common alternative is the
"(s + s)[1:-1].find(s) != -1" trick which is also O(n) but uses naive search
under the hood; the LPS approach is the canonical linear-time method.
'''
