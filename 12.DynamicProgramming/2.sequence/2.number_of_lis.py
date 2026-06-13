'''
2. Number of Longest Increasing Subsequences (Medium)
Problem Statement

Given an integer array nums, return the number of longest strictly increasing
subsequences.

Notice that the sequence has to be strictly increasing.

Example
Input:
nums = [1,3,5,4,7]

Output:
2
Explanation:
The two longest increasing subsequences are [1,3,4,7] and [1,3,5,7], both
of length 4.
'''


def findNumberOfLIS(nums):
    # O(n^2) DP carrying both length and count.
    #
    # State (per index i, considering runs that END at i):
    #   length[i] = length of the longest increasing subsequence ending at i
    #   count[i]  = how many such longest subsequences end at i
    # Transition: for each j < i with nums[j] < nums[i]:
    #   - if length[j] + 1 > length[i]: a strictly longer run -> adopt it,
    #         length[i] = length[j] + 1, count[i] = count[j]
    #   - elif length[j] + 1 == length[i]: another way to reach the same max
    #         -> count[i] += count[j]
    # Base: every element alone is a run of length 1 with count 1.
    # Answer: sum of count[i] over all i whose length[i] equals the global max.
    if not nums:
        return 0

    n = len(nums)
    length = [1] * n
    count = [1] * n

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                if length[j] + 1 > length[i]:
                    length[i] = length[j] + 1
                    count[i] = count[j]
                elif length[j] + 1 == length[i]:
                    count[i] += count[j]

    longest = max(length)
    return sum(c for l, c in zip(length, count) if l == longest)


if __name__ == "__main__":
    print(findNumberOfLIS([1, 3, 5, 4, 7]))      # Expected: 2
    print(findNumberOfLIS([2, 2, 2, 2, 2]))      # Expected: 5

'''
Pattern
✅ Sequence DP — LIS family, counting variant

Why this DP:
We extend the standard ending-at-i LIS recurrence to also track how many
distinct longest runs end at each index. When we find a longer run we reset
the count to that predecessor's count; when we find an equally long run we
accumulate. For [2,2,2,2,2] no element is strictly greater than another, so
each stays length 1 with count 1 and the answer is 5 (each single element).

| Metric | Value   |
| ------ | ------- |
| Time   | O(n^2)  |
| Space  | O(n)    |

Better Possible?
✅ Yes — an O(n log n) solution exists using Fenwick / segment trees over
(length, count) prefixes, but the O(n^2) version is the standard, readable
answer for interview ranges.
'''
