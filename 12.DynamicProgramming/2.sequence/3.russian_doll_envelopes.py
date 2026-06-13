'''
3. Russian Doll Envelopes (Hard)
Problem Statement

You are given a 2D array of integers envelopes where
envelopes[i] = [w_i, h_i] represents the width and the height of an envelope.

One envelope can fit into another if and only if both its width and height
are strictly greater than the other envelope's width and height.

Return the maximum number of envelopes you can Russian doll (i.e. put one
inside another).

Note: You cannot rotate an envelope.

Example
Input:
envelopes = [[5,4],[6,4],[6,7],[2,3]]

Output:
3
Explanation:
The maximum number of envelopes is 3 ([2,3] => [5,4] => [6,7]).
'''

import bisect


def maxEnvelopes(envelopes):
    # Reduce 2D nesting to a 1D LIS.
    #
    # Sort key: width ascending, and for EQUAL widths, height DESCENDING.
    #   - Ascending width guarantees we only ever look forward in width.
    #   - Descending height on ties prevents two equal-width envelopes from
    #     both counting (they can't nest), because a later equal-width
    #     envelope has a smaller-or-equal height and cannot extend the run.
    # After sorting, run a strict LIS on the heights:
    #   State: tails[i] = smallest tail height of an increasing run of len i+1
    #   Transition: bisect_left(tails, h) -> append if at end else replace
    #   Base: tails empty; answer = len(tails).
    if not envelopes:
        return 0

    envelopes.sort(key=lambda e: (e[0], -e[1]))

    tails = []
    for _, h in envelopes:
        i = bisect.bisect_left(tails, h)  # strictly increasing heights
        if i == len(tails):
            tails.append(h)
        else:
            tails[i] = h
    return len(tails)


if __name__ == "__main__":
    print(maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]))  # Expected: 3
    print(maxEnvelopes([[1, 1], [1, 1], [1, 1]]))          # Expected: 1

'''
Pattern
✅ Sequence DP — LIS in 2D

Why this DP:
Nesting needs strict increase in BOTH dimensions. By sorting on width
ascending we fix one dimension's order; the descending-height tie-break is
the crucial trick that makes a plain LIS over heights correct — without it,
equal-width envelopes could be wrongly chained. The remaining problem is
exactly Longest Increasing Subsequence on the height column, solved with the
same O(n log n) patience method as problem 1. For [[1,1],[1,1],[1,1]] all
widths tie, heights sort as [1,1,1] descending, and strict LIS yields 1.

| Metric | Value      |
| ------ | ---------- |
| Time   | O(n log n) |
| Space  | O(n)       |

Better Possible?
❌ No
Sorting dominates at O(n log n), and that matches the optimal LIS bound.
'''
