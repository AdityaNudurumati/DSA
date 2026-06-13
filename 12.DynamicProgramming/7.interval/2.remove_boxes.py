"""
546. Remove Boxes (Hard)

Problem Statement:
You are given several boxes in a row, each with a positive integer colour.
You remove the boxes in rounds. In each round you may choose a contiguous run
of boxes of the SAME colour (length k >= 1) and remove them, gaining k*k points.
After removal the remaining boxes close the gap. Return the maximum points
obtainable by removing all the boxes.

Example:
    Input:  [1,3,2,2,2,3,4,3,1]
    Output: 23

    Input:  [1,1,1]
    Output: 9
"""

import sys
from functools import lru_cache


def remove_boxes(boxes):
    n = len(boxes)

    # state:      dp(i, j, k) = max points from removing boxes[i..j], given that
    #             k extra boxes equal to boxes[i] are already attached just to
    #             the LEFT of i (they will be removed together with box i).
    # transition: two choices for the left block boxes[i] plus its k attachments:
    #   (a) remove that block of size (k+1) right now:
    #           (k+1)*(k+1) + dp(i+1, j, 0)
    #   (b) keep it and merge with a later box m (i<m<=j) of the same colour,
    #       first clearing everything strictly between i and m:
    #           dp(i+1, m-1, 0) + dp(m, j, k+1)
    #       so the k+1 boxes ride along until they meet box m.
    # base:       i > j -> 0 points.
    @lru_cache(maxsize=None)
    def dp(i, j, k):
        if i > j:
            return 0

        # Collapse a leading run of equal colours into the carry count k.
        while i < j and boxes[i + 1] == boxes[i]:
            i += 1
            k += 1

        # Choice (a): remove the current block of (k+1) same-coloured boxes.
        best = (k + 1) * (k + 1) + dp(i + 1, j, 0)

        # Choice (b): defer, merging with a matching box m further right.
        for m in range(i + 1, j + 1):
            if boxes[m] == boxes[i]:
                best = max(best, dp(i + 1, m - 1, 0) + dp(m, j, k + 1))

        return best

    return dp(0, n - 1, 0)


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    print(remove_boxes([1, 3, 2, 2, 2, 3, 4, 3, 1]))  # Expected: 23
    print(remove_boxes([1, 1, 1]))                     # Expected: 9


"""
Pattern: INTERVAL DP — top-down memoization with a 3D state (i, j, k).
Why: the score of removing a run is quadratic (k*k), so it pays to gather
same-coloured boxes before removing them. A plain 2D interval state cannot
record how many equal boxes are "waiting" to the left, so we add a third
dimension k = count of boxes equal to boxes[i] already glued to the left of i.
This lets the recurrence either cash in the whole block now, or postpone it to
merge with a matching box m deeper in the interval.

| Metric | Value    |
|--------|----------|
| Time   | O(n^4)   |
| Space  | O(n^3)   |

Better Possible?
O(n^3) states with O(n) work each gives O(n^4), the standard bound. Tighter
constant factors are possible but no simpler asymptotic is generally known.
"""
