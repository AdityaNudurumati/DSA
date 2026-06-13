'''
2. Distinct Echo Substrings (Hard)
Problem Statement

Return the number of DISTINCT non-empty substrings of s that can be written as
the concatenation of some string with itself (an "echo": t + t).

So we want distinct substrings of even length 2*L whose first half equals its
second half. We compare the two halves cheaply with a polynomial rolling hash
(prefix hashes give any substring's hash in O(1)), and we use DOUBLE hashing so
the (hash, length) signature we store in a set never collides by accident.

Example
Input:
s = "abcabcabc"

Output:
3
Explanation:
The distinct echoes are "abcabc" (=abc+abc), "bcabca" (=bca+bca),
"cabcab" (=cab+cab). "abcabcabc" itself is not an echo (odd length).
'''

BASE1, MOD1 = 131, (1 << 61) - 1
BASE2, MOD2 = 137, 1_000_000_007


def distinctEchoSubstrings(s):
    n = len(s)

    # prefix hashes: h[i] = hash of s[:i]; powers for O(1) substring hashing
    h1 = [0] * (n + 1)
    h2 = [0] * (n + 1)
    p1 = [1] * (n + 1)
    p2 = [1] * (n + 1)
    for i in range(n):
        h1[i + 1] = (h1[i] * BASE1 + ord(s[i])) % MOD1
        h2[i + 1] = (h2[i] * BASE2 + ord(s[i])) % MOD2
        p1[i + 1] = (p1[i] * BASE1) % MOD1
        p2[i + 1] = (p2[i] * BASE2) % MOD2

    def hash1(l, r):                       # hash of s[l:r)
        return (h1[r] - h1[l] * p1[r - l]) % MOD1

    def hash2(l, r):
        return (h2[r] - h2[l] * p2[r - l]) % MOD2

    seen = set()                           # signatures of distinct echoes

    # for every half-length L, slide the start i of the first half
    for L in range(1, n // 2 + 1):
        for i in range(0, n - 2 * L + 1):
            mid = i + L
            end = i + 2 * L
            # the two halves match iff both hashes match
            if hash1(i, mid) == hash1(mid, end) and \
               hash2(i, mid) == hash2(mid, end):
                # store a signature of the WHOLE echo so duplicates collapse
                seen.add((hash1(i, end), hash2(i, end), 2 * L))

    return len(seen)


if __name__ == "__main__":
    print(distinctEchoSubstrings("abcabcabc"))         # Expected: 3
    print(distinctEchoSubstrings("leetcodeleetcode"))  # Expected: 2

'''
Pattern
Double Hashing with prefix hashes. Comparing the two halves of a candidate is
O(1) thanks to prefix hashing, and a set of (hash1, hash2, length) signatures
deduplicates distinct echoes. Two mod bases keep accidental collisions away.

| Metric | Value  |
| ------ | ------ |
| Time   | O(n^2) |
| Space  | O(n)   |

Better Possible?
O(n^2) is essentially optimal here since there can be O(n^2) candidate halves;
the constant factor is what hashing buys us over re-comparing characters.
'''
