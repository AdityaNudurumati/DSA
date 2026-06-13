"""
1547. Minimum Cost to Cut a Stick (Hard)

Problem Statement:
A wooden stick of length n is given, labelled from position 0 to n. You are
also given an array cuts of positions where cuts must be made (in any order).
The cost of one cut equals the CURRENT length of the stick segment being cut.
After a cut, the stick splits into two segments that are then cut independently.
Return the minimum total cost to perform all the cuts.

Example:
    Input:  n = 7, cuts = [1,3,4,5]
    Output: 16

    Input:  n = 9, cuts = [5,6,1,4,2]
    Output: 22
"""


def min_cost(n, cuts):
    # Add the two stick ends as fixed boundaries and sort, so every segment is
    # defined by a pair of adjacent-or-distant cut positions.
    points = sorted(cuts + [0, n])
    m = len(points)

    # state:      dp[i][j] = min cost to make every cut strictly between the
    #             boundary positions points[i] and points[j].
    # transition: choose which cut k (i<k<j) is made FIRST in this segment. That
    #             first cut costs the full current segment length
    #             points[j]-points[i], then the segment splits into (i,k) and
    #             (k,j) which are solved independently:
    #             dp[i][j] = min over k of
    #                        dp[i][k] + dp[k][j] + (points[j]-points[i])
    # base:       no cut between i and j (j <= i+1) -> 0 cost.
    dp = [[0] * m for _ in range(m)]

    # Iterate by increasing gap so the sub-segments are already solved.
    for gap in range(2, m):
        for i in range(0, m - gap):
            j = i + gap
            seg = points[j] - points[i]
            best = float("inf")
            for k in range(i + 1, j):
                cost = dp[i][k] + dp[k][j] + seg
                if cost < best:
                    best = cost
            dp[i][j] = best

    return dp[0][m - 1]


if __name__ == "__main__":
    print(min_cost(7, [1, 3, 4, 5]))     # Expected: 16
    print(min_cost(9, [5, 6, 1, 4, 2]))  # Expected: 22


"""
Pattern: INTERVAL DP — tabulation over cut boundaries with the "cut first" choice.
Why: the cost of a cut depends on the current segment length, which depends on
the order of cuts — so greedy fails. By sorting cut positions and adding the
stick ends, each interval (i, j) is the segment between two boundaries. Deciding
which cut happens FIRST fixes the cost of that cut as the whole segment length
and splits the rest into two independent subintervals:
    dp[i][j] = min_k dp[i][k] + dp[k][j] + (points[j] - points[i]).

| Metric | Value                            |
|--------|----------------------------------|
| Time   | O(c^3)  (c = number of cuts + 2) |
| Space  | O(c^2)                           |

Better Possible?
The cubic interval DP is the standard solution; cost depends on the number of
cuts, not the stick length n, which is the key efficiency.
"""
