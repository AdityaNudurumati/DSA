'''
3. One Edit Distance (Medium)
Problem Statement

Given two strings s and t, return True if they are exactly one edit distance
apart, otherwise return False.

One edit means one of: insert a character, delete a character, or replace a
character. Two identical strings are zero edits apart, so they return False.

Example

Input:
s = "ab", t = "acb"

Output:
True

Explanation:
Inserting 'c' into "ab" produces "acb", which is a single edit.
'''

def isOneEditDistance(s, t):
    m, n = len(s), len(t)

    # if length gap is more than 1, impossible in a single edit
    if abs(m - n) > 1:
        return False

    # ensure s is the shorter (or equal length) string
    if m > n:
        return isOneEditDistance(t, s)

    for i in range(m):
        if s[i] != t[i]:
            if m == n:
                # same length -> the rest must match (one replace)
                return s[i + 1:] == t[i + 1:]
            else:
                # t is longer -> skip t[i] (one insert), rest must match
                return s[i:] == t[i + 1:]

    # no mismatch in the common prefix: valid only if t has exactly 1 extra
    return n - m == 1


if __name__ == "__main__":
    print(isOneEditDistance("ab", "acb"))    # Expected: True
    print(isOneEditDistance("cab", "ad"))    # Expected: False
    print(isOneEditDistance("1203", "1213"))  # Expected: True


'''
Pattern
✅ Two-pointer scan (single-pass edit check)
Instead of a full DP table, we scan once: at the first mismatch we decide
between replace (equal lengths) or insert/delete (length differs by one),
then require the remaining tails to be identical.

| Metric | Value      |
| ------ | ---------- |
| Time   | O(min(m,n))|
| Space  | O(1)       |

Better Possible?
No. We must look at characters up to the first mismatch, so O(n) time
and O(1) space is optimal.
'''
