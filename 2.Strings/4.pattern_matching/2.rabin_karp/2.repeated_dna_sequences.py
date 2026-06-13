'''
2. Repeated DNA Sequences (Medium)
Problem Statement

The DNA sequence is composed of the letters A, C, G, and T. Given a string s,
return all the 10-letter-long sequences (substrings) that occur more than
once in the DNA molecule. You may return the answer in any order.

Algorithm: Rabin-Karp polynomial rolling hash over every 10-character window.
Maintain the running hash in O(1) per step and count how many times each
window's verified substring appears.

Example
Input:  s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC", "CCCCCAAAAA"]   (sorted before printing)
'''

WINDOW = 10
BASE = 4          # 4 nucleotides -> base-4 rolling hash
MOD = (1 << 61) - 1

CODE = {"A": 0, "C": 1, "G": 2, "T": 3}


def findRepeatedDnaSequences(s):
    n = len(s)
    if n < WINDOW:
        return []

    highest_pow = pow(BASE, WINDOW - 1, MOD)

    # hash_seen[h] -> set of substrings with that hash (collision-safe count)
    seen_once = {}
    result = []
    added = set()

    h = 0
    for i in range(WINDOW):
        h = (h * BASE + CODE[s[i]]) % MOD

    for start in range(n - WINDOW + 1):
        sub = s[start:start + WINDOW]
        # Verify by exact substring keyed under the hash bucket.
        bucket = seen_once.setdefault(h, set())
        if sub in bucket:
            if sub not in added:
                result.append(sub)
                added.add(sub)
        else:
            bucket.add(sub)
        # Roll forward.
        if start < n - WINDOW:
            h = (h - CODE[s[start]] * highest_pow) % MOD
            h = (h * BASE + CODE[s[start + WINDOW]]) % MOD

    return result


if __name__ == "__main__":
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print(sorted(findRepeatedDnaSequences(s)))  # Expected: ['AAAAACCCCC', 'CCCCCAAAAA']


'''
Pattern
Rabin-Karp — encode each fixed-length (10) window as a base-4 rolling hash so
each slide is O(1). Bucket substrings by hash and report any that appear more
than once. Verifying the real substring inside the bucket avoids false hits.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible? Not asymptotically. A plain dict of 10-char slices is also
O(n) but recomputes each slice; the rolling hash makes window updates O(1)
and generalizes to larger window sizes.
'''
