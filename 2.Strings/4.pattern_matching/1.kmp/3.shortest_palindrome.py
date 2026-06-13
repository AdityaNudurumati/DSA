'''
3. Shortest Palindrome (Hard)
Problem Statement

You are given a string s. You can convert s to a palindrome by adding
characters in front of it. Return the shortest palindrome you can find by
performing this transformation.

Algorithm: KMP. Build the combined string s + '#' + reverse(s) and compute
its LPS array. The last LPS value is the length of the longest prefix of s
that is also a palindrome. The remaining suffix, reversed, is prepended.

Example
Input:  s = "aacecaaa"
Output: "aaacecaaa"
Input:  s = "abcd"
Output: "dcbabcd"
'''


def build_lps(s):
    lps = [0] * len(s)
    k = 0
    for i in range(1, len(s)):
        while k and s[i] != s[k]:
            k = lps[k - 1]
        if s[i] == s[k]:
            k += 1
        lps[i] = k
    return lps


def shortestPalindrome(s):
    if not s:
        return s

    rev = s[::-1]
    # '#' is a separator so the prefix-match cannot overflow across the
    # boundary. lps[-1] = longest prefix of s that is a palindrome.
    combined = s + "#" + rev
    lps = build_lps(combined)
    palin_len = lps[-1]

    # The tail of s (after the palindromic prefix), reversed, goes in front.
    to_add = rev[: len(s) - palin_len]
    return to_add + s


if __name__ == "__main__":
    print(shortestPalindrome("aacecaaa"))  # Expected: aaacecaaa
    print(shortestPalindrome("abcd"))      # Expected: dcbabcd


'''
Pattern
KMP on s + '#' + reverse(s). The failure function of this construction yields
the longest palindromic prefix in linear time; everything after it must be
mirrored in front to complete the palindrome.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible? No. The naive approach is O(n^2); the KMP trick (or Manacher)
brings it to optimal O(n).
'''
