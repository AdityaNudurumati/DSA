"""
312. Burst Balloons (Hard)

Problem Statement:
You are given n balloons, indexed 0..n-1, each painted with a number nums[i].
You burst all the balloons. If you burst balloon i you gain
    nums[i-1] * nums[i] * nums[i+1]
coins, where out-of-bounds neighbours are treated as a balloon with value 1.
After bursting, balloon i is removed and its neighbours become adjacent.
Return the maximum coins you can collect by bursting all balloons wisely.

Example:
    Input:  [3,1,5,8]
    Output: 167

    Input:  [1,5]
    Output: 10
"""


def max_coins(nums):
    # Pad with virtual value-1 balloons at both ends so every burst always has
    # two neighbours. Work on the padded array of length n+2.
    vals = [1] + nums + [1]
    n = len(vals)

    # state:      dp[i][j] = max coins from bursting every balloon strictly
    #             between the boundaries i and j (open interval (i, j)).
    # transition: pick balloon k in (i, j) to burst LAST in this interval. When
    #             it bursts, its only remaining neighbours are i and j, so:
    #             dp[i][j] = max over k of
    #                        dp[i][k] + vals[i]*vals[k]*vals[j] + dp[k][j]
    #             The "burst last" trick fixes the neighbours of k.
    # base:       intervals with no balloon inside (j <= i+1) contribute 0.
    dp = [[0] * n for _ in range(n)]

    # Iterate by increasing gap so dp[i][k] and dp[k][j] are already solved.
    for gap in range(2, n):
        for i in range(0, n - gap):
            j = i + gap
            best = 0
            for k in range(i + 1, j):
                coins = dp[i][k] + vals[i] * vals[k] * vals[j] + dp[k][j]
                if coins > best:
                    best = coins
            dp[i][j] = best

    return dp[0][n - 1]


if __name__ == "__main__":
    print(max_coins([3, 1, 5, 8]))  # Expected: 167
    print(max_coins([1, 5]))        # Expected: 10


"""
Pattern: INTERVAL DP — tabulation over open intervals with the "burst last" trick.
Why: bursting first is hard to model because the neighbours of a balloon keep
changing as others pop. Instead we ask which balloon bursts LAST inside (i, j):
at that moment its neighbours are exactly the fixed boundaries i and j, which
cleanly splits the interval into two independent already-solved subintervals
(i, k) and (k, j). That yields
    dp[i][j] = max_k dp[i][k] + vals[i]*vals[k]*vals[j] + dp[k][j].

| Metric | Value    |
|--------|----------|
| Time   | O(n^3)   |
| Space  | O(n^2)   |

Better Possible?
O(n^3) time and O(n^2) space are the standard optimum for this problem; no
known asymptotically faster general solution exists.
"""
