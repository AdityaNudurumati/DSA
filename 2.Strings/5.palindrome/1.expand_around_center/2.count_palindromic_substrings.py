'''
2. Palindromic Substrings (Medium)
Problem Statement

Given a string s, count how many of its substrings are palindromes.
Substrings at different start/end positions count separately even if they
are made of the same characters.

Example
Input:  s = "abc"
Output: 3            ("a", "b", "c")

Input:  s = "aaa"
Output: 6            ("a","a","a","aa","aa","aaa")
'''

def countSubstrings(s):

    count = 0

    # expand outward from a center; every successful step is one more palindrome
    def expand(left, right):
        c = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            c += 1            # s[left..right] is a palindrome
            left -= 1
            right += 1
        return c

    for i in range(len(s)):
        count += expand(i, i)        # odd-length centers
        count += expand(i, i + 1)    # even-length centers

    return count


if __name__ == "__main__":
    print(countSubstrings("abc"))  # Expected: 3
    print(countSubstrings("aaa"))  # Expected: 6

'''
Pattern
✅ Expand Around Center

Same 2n-1 centers as Longest Palindromic Substring, but instead of tracking
the longest match we add 1 for every successful expansion step, since each
step corresponds to a distinct palindromic substring.

| Metric | Value |
| ------ | ----- |
| Time   | O(n²) |
| Space  | O(1)  |

Better Possible?
✅ Yes — Manacher's algorithm gives all palindrome radii in O(n), from which
the count can be derived. See ../2.manacher/
'''
