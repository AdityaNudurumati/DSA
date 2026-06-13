'''
3. Merge Strings Alternately (Easy)
Problem Statement

You are given two strings word1 and word2. Merge them by adding letters in
alternating order, starting with word1. If one string is longer, append the
extra letters onto the end of the merged string.

Example
Input:
word1 = "abc", word2 = "pqr"

Output:
"apbqcr"
Explanation:
a p b q c r — alternating, both same length.
'''

def mergeAlternately(word1, word2):

    i = 0
    j = 0
    result = []

    # take one char from each while both have characters left
    while i < len(word1) and j < len(word2):
        result.append(word1[i])
        result.append(word2[j])
        i += 1
        j += 1

    # append whatever remains from the longer string
    result.append(word1[i:])
    result.append(word2[j:])

    return "".join(result)


if __name__ == "__main__":
    print(mergeAlternately("abc", "pqr"))   # Expected: apbqcr
    print(mergeAlternately("ab", "pqrs"))   # Expected: apbqrs

'''
Pattern
Same Direction Two Pointers — one index per string, both advance together,
appending in turn; the leftover tail is appended once at the end.

| Metric | Value |
| ------ | ----- |
| Time   | O(n + m) |
| Space  | O(n + m) |  (the merged output)

Better Possible?
No — every character must be copied into the result exactly once.
'''
