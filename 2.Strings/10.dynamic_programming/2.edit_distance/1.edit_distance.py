'''
1. Edit Distance (Medium)
Problem Statement

Given two strings word1 and word2, return the minimum number of operations
required to convert word1 into word2.

You may insert a character, delete a character, or replace a character.

Example

Input:
word1 = "horse", word2 = "ros"

Output:
3

Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose  (delete 'r')
rose  -> ros   (delete 'e')
'''

def minDistance(word1, word2):
    m, n = len(word1), len(word2)

    # dp[i][j] = edit distance between word1[:i] and word2[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # turning a prefix into "" costs i deletions
    for i in range(m + 1):
        dp[i][0] = i
    # turning "" into a prefix costs j insertions
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                # chars match, no operation needed
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # min of delete, insert, replace, then +1
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # delete from word1
                    dp[i][j - 1],      # insert into word1
                    dp[i - 1][j - 1],  # replace
                )

    return dp[m][n]


if __name__ == "__main__":
    print(minDistance("horse", "ros"))            # Expected: 3
    print(minDistance("intention", "execution"))  # Expected: 5


'''
Pattern
✅ 2D DP over prefixes (Levenshtein distance)
Each cell is the cheapest of delete / insert / replace, with a free move
when the current characters already match.

| Metric | Value   |
| ------ | ------- |
| Time   | O(m*n)  |
| Space  | O(m*n)  |

Better Possible?
Space reduces to O(min(m, n)) with two rows.
Time O(m*n) is optimal in general (Hirschberg only saves space).
'''
