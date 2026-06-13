'''
376. Wiggle Subsequence (Medium)
Problem Statement

A wiggle sequence is one where the differences between successive numbers strictly
alternate between positive and negative. A sequence with fewer than two elements is
trivially a wiggle sequence, and a single element (or two unequal elements) is a wiggle
sequence of length 1 (or 2).

Given an integer array nums, return the length of the longest subsequence of nums that
is a wiggle sequence. A subsequence is obtained by deleting some (possibly zero) elements
without changing the order of the remaining elements.

Example
Input:
nums = [1, 7, 4, 9, 2, 5]

Output:
6
'''


def wiggleMaxLength(nums):

    if not nums:
        return 0

    # up   = length of longest wiggle subseq ending with a rising  edge
    # down = length of longest wiggle subseq ending with a falling edge
    up = down = 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:        # rising edge -> extend a chain that last fell
            up = down + 1
        elif nums[i] < nums[i - 1]:      # falling edge -> extend a chain that last rose
            down = up + 1
        # equal -> no direction change, carry both forward unchanged

    return max(up, down)


if __name__ == "__main__":
    print(wiggleMaxLength([1, 7, 4, 9, 2, 5]))                       # Expected: 6
    print(wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]))     # Expected: 7
    print(wiggleMaxLength([1, 2, 3, 4, 5, 6, 7, 8, 9]))              # Expected: 2

'''
Pattern
✅ Array greedy (count direction changes via two running states)

Greedy Rule & Why It's Safe
Walk left to right tracking two lengths: `up` (best wiggle ending on a rise) and
`down` (best wiggle ending on a fall). On a rising step the only useful move is to
append to the best chain that just fell, so up = down + 1; symmetrically for a fall.
Greedily taking every genuine direction flip is safe because a longer wiggle can never
be lost by accepting a flip: each flip is independent, and keeping the most recent
extreme as the pivot leaves the most room for the next opposite move. Flat (equal)
steps add nothing and are skipped, which never blocks a future alternation. Thus the
locally optimal "count every change" coincides with the global optimum.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No. Every element must be inspected once (O(n) lower bound) and only two scalars
are kept (O(1) space). The equivalent O(n) DP is no faster and uses more memory.
'''
