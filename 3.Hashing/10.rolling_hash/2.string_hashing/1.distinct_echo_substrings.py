'''
1. Distinct Echo Substrings (Hard)
Problem Statement

Return the number of DISTINCT non-empty substrings of text that can be written as the
concatenation of some string with itself, i.e. substrings of the form t + t (an "echo").

We use prefix hashing so the hash of any substring is available in O(1). For a candidate
echo of length 2L starting at i, the two halves echo iff hash(i, i+L) == hash(i+L, i+2L);
we collect the matching echoes in a set to keep only distinct ones.

Example
Input:
text = "abcabcabc"

Output:
3
Explanation:
The distinct echo substrings are "abcabc", "bcabca", "cabcab".
'''

BASE = 131
MOD = (1 << 61) - 1                       # huge modulus -> negligible collision risk


def distinctEchoSubstrings(text):

    n = len(text)

    # prefix hashes: h[i] = hash of text[0:i];  pows[k] = BASE^k % MOD
    h = [0] * (n + 1)
    pows = [1] * (n + 1)
    for i in range(n):
        h[i + 1] = (h[i] * BASE + ord(text[i])) % MOD
        pows[i + 1] = (pows[i] * BASE) % MOD

    def sub_hash(l, r):                    # hash of text[l:r]
        return (h[r] - h[l] * pows[r - l]) % MOD

    seen = set()                           # store hash of each distinct echo substring

    # for every start i and every half-length L, test if the two halves match
    for i in range(n):
        for L in range(1, (n - i) // 2 + 1):
            left = sub_hash(i, i + L)
            right = sub_hash(i + L, i + 2 * L)
            if left == right:
                # key includes L so different-length echoes can't collide as keys
                seen.add((left, L))

    return len(seen)


if __name__ == "__main__":
    print(distinctEchoSubstrings("abcabcabc"))         # Expected: 3
    print(distinctEchoSubstrings("leetcodeleetcode"))  # Expected: 2

'''
Pattern
✅ String (prefix) Hashing

Technique & why
Build prefix polynomial hashes once so the hash of any substring is O(1). An echo t+t is
detected by comparing the hashes of its two equal-length halves. Distinctness is enforced
by adding (hash, length) to a set. This replaces O(n) per-substring comparison with O(1)
hash equality, giving an O(n^2) scan over all (start, half-length) pairs.

| Metric | Value |
| ------ | ----- |
| Time   | O(n^2) |
| Space  | O(n) for prefix hashes + O(#echoes) for the set |

Better Possible?
❌ Not meaningfully; there can be O(n^2) distinct echo substrings, so listing/counting
them distinctly is already near-optimal for this hashing approach.
'''
