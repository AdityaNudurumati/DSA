'''
2. Valid Palindrome II (Easy)
Problem Statement

Given a string s, return True if it can become a palindrome after deleting
at most one character.

Example
Input:
s = "abca"

Output:
True
Explanation:
Deleting 'c' (or 'b') leaves "aba" / "aca", which is a palindrome.
'''

def validPalindrome(s):

    def isPal(lo, hi):
        # plain palindrome check on the slice s[lo..hi]
        while lo < hi:
            if s[lo] != s[hi]:
                return False
            lo += 1
            hi -= 1
        return True

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            # on the first mismatch, try skipping ONE side
            return isPal(left + 1, right) or isPal(left, right - 1)
        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    print(validPalindrome("aba"))   # Expected: True
    print(validPalindrome("abca"))  # Expected: True
    print(validPalindrome("abc"))   # Expected: False

'''
Pattern
Opposite Ends Two Pointers with one allowed "skip". On the first mismatch we
branch: either delete the left char or the right char, then verify the rest.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
No — a single linear scan with at most one extra check is optimal.
'''
