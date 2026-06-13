'''
2. Partition to K Equal Sum Subsets (Medium)
Problem Statement

Given an integer array nums and an integer k, return True if it is possible to
divide all of the elements of nums into k non-empty subsets whose sums are all
equal.

Each element must be used exactly once.

Input:
nums = [4, 3, 2, 3, 5, 2, 1], k = 4

Output:
True

Explanation:
The target per subset is 20 / 4 = 5. One valid partition is
{5}, {1,4}, {2,3}, {2,3}.

Input:
nums = [1, 2, 3, 4], k = 3

Output:
False

Explanation:
Total is 10, which is not divisible by 3, so equal partition is impossible.
'''

from functools import lru_cache


def canPartitionKSubsets(nums, k):
    total = sum(nums)
    if k <= 0 or total % k != 0:
        return False
    target = total // k

    n = len(nums)
    nums = sorted(nums, reverse=True)        # fail fast on oversized items
    if nums and nums[0] > target:
        return False

    FULL = (1 << n) - 1

    # State: dp(mask) = True iff the items already used (bits set in `mask`) can
    #        be perfectly arranged into completed buckets PLUS a partially
    #        filled current bucket. We track only `mask`, deriving the current
    #        bucket's fill as (sum of used items) % target — every time a bucket
    #        tops out at `target` it "rolls over" and a fresh bucket starts.
    # Transition: from mask, pick any unused item i. It is placeable only if it
    #        fits in the remaining room of the current bucket:
    #            used = sum(items in mask) % target
    #            if used + nums[i] <= target: try dp(mask | 1<<i)
    # Base: dp(FULL) = True (all items placed -> exactly k full buckets).
    @lru_cache(maxsize=None)
    def dp(mask):
        if mask == FULL:
            return True

        used = 0
        for i in range(n):
            if (mask >> i) & 1:
                used += nums[i]
        used %= target                       # fill level of current bucket

        for i in range(n):
            if (mask >> i) & 1:
                continue
            if used + nums[i] <= target:     # fits in current bucket
                if dp(mask | (1 << i)):
                    return True
            # Pruning: if this item exactly empties to a fresh bucket boundary
            # and still fails, no equal-or-larger item will help. Since nums is
            # sorted desc, break to skip duplicate-value attempts at this level.
            if used + nums[i] == target or used == 0:
                break
        return False

    return dp(0)


if __name__ == "__main__":
    print(canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))  # Expected: True
    print(canPartitionKSubsets([1, 2, 3, 4], 3))           # Expected: False


'''
Pattern
✅ Bitmask DP (Subset States)
With n <= ~16 items, the set of already-placed items is a subset encoded as an
n-bit mask. The clever part: we do NOT store how many buckets are done or the
current bucket level separately — both are recoverable from the mask because
(sum of chosen items) % target is exactly the current bucket's fill. That makes
the state a single integer dp[mask], giving overlapping subproblems we memoize.

| Metric | Value      |
| ------ | ---------- |
| Time   | O(2^n * n) |
| Space  | O(2^n)     |

Better Possible?
❌ This problem is NP-complete (generalizes the partition problem), so no known
polynomial-time algorithm exists. The 2^n bitmask DP with sorting + pruning is
the standard practical optimum and dramatically beats naive backtracking that
re-explores identical "set of used items" states.
'''
