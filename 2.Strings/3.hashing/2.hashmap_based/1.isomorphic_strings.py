'''
1. Isomorphic Strings (Easy)
Problem Statement

Given two strings s and t, return True if they are isomorphic. They are
isomorphic if the characters in s can be replaced to get t, where each character
maps to exactly one character and no two characters map to the same one (a
bijection that preserves order).

Example
Input:
s = "egg", t = "add"

Output:
True
'''

def isIsomorphic(s, t):

    if len(s) != len(t):
        return False

    s_to_t = {}   # forward mapping char(s) -> char(t)
    t_to_s = {}   # reverse mapping to enforce one-to-one

    for a, b in zip(s, t):
        # conflict if either direction already mapped to something else
        if a in s_to_t and s_to_t[a] != b:
            return False
        if b in t_to_s and t_to_s[b] != a:
            return False
        s_to_t[a] = b
        t_to_s[b] = a

    return True


if __name__ == "__main__":
    print(isIsomorphic("egg", "add"))       # Expected: True
    print(isIsomorphic("foo", "bar"))       # Expected: False
    print(isIsomorphic("paper", "title"))   # Expected: True

'''
Pattern
✅ HashMap Based (bijection check)

Key Observation
Two maps enforce a one-to-one correspondence: forward catches "one char -> two
different chars" and reverse catches "two chars -> same char".

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
O(n) is optimal. Space is O(1) for a bounded alphabet.
'''
