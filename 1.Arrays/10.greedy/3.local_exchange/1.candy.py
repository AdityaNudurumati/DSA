'''
1. Candy (Hard)
Problem Statement

n children stand in a line, each with a rating. Give candies so that every child
gets at least one, and any child with a higher rating than an immediate neighbor
gets more candies than that neighbor. Return the minimum total candies.

Example
Input:
ratings = [1,0,2]

Output:
5
Explanation:
[2,1,2] = 5 candies.
'''

def candy(ratings):

    n = len(ratings)
    candies = [1] * n

    # left-to-right: satisfy the "greater than left neighbor" rule
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    # right-to-left: satisfy the "greater than right neighbor" rule,
    # keeping whichever requirement is larger
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)


if __name__ == "__main__":
    print(candy([1, 0, 2]))   # Expected: 5
    print(candy([1, 2, 2]))   # Expected: 4

'''
Pattern
✅ Two-pass Greedy (each direction enforces one neighbor constraint)

Key Observation
A single pass can't see both neighbors. Sweep left then right, taking the max of the
two requirements so both inequalities hold with the minimum total.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
An O(1)-space slope-counting solution exists but is trickier.
'''
