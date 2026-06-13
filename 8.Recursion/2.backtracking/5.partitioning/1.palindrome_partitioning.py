'''
131. Palindrome Partitioning (Medium)
Problem Statement

Given a string s, partition s such that every substring of the partition is a
palindrome. Return all possible palindrome partitionings of s.

Example:
Input:
s = "aab"

Output:
[["a","a","b"], ["aa","b"]]
'''


def partition(s):
    result = []

    def is_palindrome(sub):
        return sub == sub[::-1]

    def backtrack(start, path):
        if start == len(s):               # consumed whole string
            result.append(path[:])
            return
        for end in range(start + 1, len(s) + 1):
            piece = s[start:end]
            if is_palindrome(piece):      # only branch on valid cuts
                path.append(piece)
                backtrack(end, path)
                path.pop()

    backtrack(0, [])
    return result


if __name__ == "__main__":
    s = "aab"
    print(sorted(partition(s)))
    # Expected: [['a', 'a', 'b'], ['aa', 'b']]


'''
Pattern
✅ Partitioning via Backtracking
At each start we try every prefix as the next cut; we only recurse when the
prefix is a palindrome, pruning invalid splits early.
| Metric | Value        |
| ------ | ------------ |
| Time   | O(n * 2^n)   |
| Space  | O(n)         |
Better Possible?
❌ No

There can be up to 2^(n-1) partitions and palindrome checks cost O(n); this is
the standard bound (DP precheck only changes the constant).
'''
