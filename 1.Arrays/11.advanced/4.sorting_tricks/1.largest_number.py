'''
1. Largest Number (Medium)
Problem Statement

Given a list of non-negative integers nums, arrange them so that they form the
largest possible number. Return it as a string (it can be huge).

Example
Input:
nums = [3,30,34,5,9]

Output:
"9534330"
'''

from functools import cmp_to_key

def largestNumber(nums):

    strs = list(map(str, nums))

    # custom order: a before b iff a+b > b+a as strings
    def compare(a, b):
        if a + b > b + a:
            return -1
        if a + b < b + a:
            return 1
        return 0

    strs.sort(key=cmp_to_key(compare))

    result = "".join(strs)
    return "0" if result[0] == "0" else result      # handle all-zeros -> "0"


if __name__ == "__main__":
    print(largestNumber([10, 2]))               # Expected: "210"
    print(largestNumber([3, 30, 34, 5, 9]))     # Expected: "9534330"
    print(largestNumber([0, 0]))                # Expected: "0"

'''
Pattern
✅ Sort with a custom pairwise comparator

Key Observation
Standard numeric/lexicographic order fails ("3" vs "30"). Compare concatenations:
place a before b when a+b > b+a. This ordering is transitive, so sorting works.

| Metric | Value      |
| ------ | ---------- |
| Time   | O(n log n) |
| Space  | O(n)       |

Better Possible?
❌ No — sorting is the core idea.
'''
