'''
1. Find All Occurrences of a Pattern in Text (Medium)
Problem Statement

Given a text and a pattern, return the starting indices of every occurrence
of the pattern inside the text (overlaps allowed).

Algorithm: Z-Algorithm. Build the string pat + '#' + text and compute its
Z-array, where Z[i] is the length of the longest substring starting at i that
matches a prefix of the whole combined string. Wherever Z[i] equals the
pattern length, the pattern occurs in the text at the mapped index.

Example
Input:  text = "aabaabaab", pat = "aab"
Output: [0, 3, 6]
'''


def z_array(s):
    n = len(s)
    z = [0] * n
    z[0] = n
    left = right = 0  # [left, right] is the current rightmost Z-box
    for i in range(1, n):
        if i < right:
            # Reuse previously computed value inside the Z-box.
            z[i] = min(right - i, z[i - left])
        # Extend the match beyond the box edge.
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        # Update the Z-box if we matched further right.
        if i + z[i] > right:
            left, right = i, i + z[i]
    return z


def find_all_occurrences(text, pat):
    sep = "#"  # a separator not present in either string
    combined = pat + sep + text
    z = z_array(combined)

    m = len(pat)
    result = []
    # Positions after the separator correspond to text indices.
    for i in range(m + 1, len(combined)):
        if z[i] == m:
            result.append(i - m - 1)  # map back to text index
    return result


if __name__ == "__main__":
    print(find_all_occurrences("aabaabaab", "aab"))  # Expected: [0, 3, 6]


'''
Pattern
Z-Algorithm — concatenate pat + '#' + text and compute the Z-array in one
linear pass. Every position whose Z-value equals the pattern length marks a
full occurrence, so all matches (including overlaps) are found in O(n + m).

| Metric | Value    |
| ------ | -------- |
| Time   | O(n + m) |
| Space  | O(n + m) |

Better Possible? No. Any algorithm must read the text once (O(n)); the Z
approach is optimal and finds all overlapping matches in a single scan.
'''
