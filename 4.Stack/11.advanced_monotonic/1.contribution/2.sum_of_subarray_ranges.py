'''
2. Sum of Subarray Ranges (Medium)
Problem Statement

You are given an integer array nums. The range of a subarray is the difference
between the largest and smallest element in it. Return the sum of all subarray
ranges of nums.

Example
Input:
nums = [1,2,3]

Output:
4

Explanation:
[1]->0, [2]->0, [3]->0, [1,2]->1, [2,3]->1, [1,2,3]->2. Sum = 4.
'''


def subarrayRanges(nums):

    # sum of (max - min) over all subarrays
    #   = (sum of maxes over all subarrays) - (sum of mins over all subarrays)
    # Each part is a contribution-technique computation.
    # No modulo here: answer fits in normal integers (problem has no mod).

    n = len(nums)

    def sum_of_extremes(want_max):
        # Generic contribution sum.
        # For minimums: count subarrays where nums[i] is the min.
        # For maximums: count subarrays where nums[i] is the max.
        # Strict comparison on the LEFT pass, non-strict on the RIGHT pass, so
        # equal elements are attributed to exactly one of them.
        prev = [-1] * n   # boundary on the left
        nxt = [n] * n     # boundary on the right

        # left boundary: previous element that is "more extreme or equal"
        stack = []
        for i in range(n):
            while stack and (nums[stack[-1]] <= nums[i] if want_max
                             else nums[stack[-1]] >= nums[i]):
                stack.pop()
            prev[i] = stack[-1] if stack else -1
            stack.append(i)

        # right boundary: next element that is strictly more extreme
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and (nums[stack[-1]] < nums[i] if want_max
                             else nums[stack[-1]] > nums[i]):
                stack.pop()
            nxt[i] = stack[-1] if stack else n
            stack.append(i)

        total = 0
        for i in range(n):
            left = i - prev[i]
            right = nxt[i] - i
            total += nums[i] * left * right
        return total

    return sum_of_extremes(True) - sum_of_extremes(False)


if __name__ == "__main__":
    print(subarrayRanges([1, 2, 3]))            # Expected: 4
    print(subarrayRanges([1, 3, 3]))            # Expected: 4
    print(subarrayRanges([4, -2, -3, 4, 1]))    # Expected: 59

'''
Pattern
✅ Advanced Monotonic Stack — Contribution Technique

Key Observation
Sum of ranges = (sum of subarray maxes) - (sum of subarray mins). Each term uses
the same contribution trick: count the subarrays where an element is the extreme
via prev/next boundaries, with strict on one side and non-strict on the other to
avoid double counting equal elements.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No on time. (An O(n) single-stack one-pass variant exists but is the same
complexity; this two-part form is clearer.)
'''
