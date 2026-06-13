'''
1. Isomorphic Strings (Easy)
Problem Statement

Two strings s and t are isomorphic if the characters in s can be replaced to get t,
where each character maps to exactly one other character and no two characters map to
the same one. The replacement order must be preserved and the mapping must be a
one-to-one correspondence (a bijection).

Given two strings s and t, return True if they are isomorphic, otherwise False.

Example
Input:
s = "egg", t = "add"

Output:
True
Explanation:
'e' -> 'a' and 'g' -> 'd' consistently, and no two source chars share a target.
'''

def isIsomorphic(s, t):

    if len(s) != len(t):
        return False

    s_to_t = {}                     # forward map: char in s -> char in t
    t_to_s = {}                     # reverse map: char in t -> char in s (guards bijection)

    for cs, ct in zip(s, t):
        # if cs was seen, its target must still match ct
        if cs in s_to_t:
            if s_to_t[cs] != ct:
                return False
        # if ct already claimed by a different source char, mapping is not one-to-one
        elif ct in t_to_s:
            return False
        else:
            s_to_t[cs] = ct
            t_to_s[ct] = cs

    return True


if __name__ == "__main__":
    print(isIsomorphic("egg", "add"))        # Expected: True
    print(isIsomorphic("foo", "bar"))        # Expected: False
    print(isIsomorphic("paper", "title"))    # Expected: True

'''
Pattern
✅ Value -> index/value mapping (two dicts enforce a char->char bijection)

Key Observation
A single map only guarantees "same source -> same target". Isomorphism also needs the
reverse: no two source chars collapse to the same target. Maintaining both maps and
checking consistency on each character catches both failure modes in one pass.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(k)  (k = distinct characters, bounded by alphabet) |

Better Possible?
O(n) is optimal since every character must be inspected. Space can drop to O(1) for a
fixed alphabet by indexing fixed-size arrays instead of dicts.
'''
