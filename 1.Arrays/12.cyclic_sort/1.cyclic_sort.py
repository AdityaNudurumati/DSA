'''
1. Cyclic Sort (Easy)
Problem Statement

Given an array containing n DISTINCT numbers taken from the range 1..n (each
number appears exactly once), sort it IN-PLACE in O(n) time without extra space.

The trick: the value v belongs at index v-1. Walk the array; if the current
value is not already at its correct index, swap it there. Only advance when the
current slot already holds the right value.

Example
Input:
nums = [3, 1, 5, 4, 2]

Output:
[1, 2, 3, 4, 5]
'''

def cyclicSort(nums):

    i = 0
    n = len(nums)

    while i < n:
        correct = nums[i] - 1            # value v -> index v-1
        if nums[i] != nums[correct]:     # not in place -> swap it home
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1                        # already correct -> move on

    return nums


if __name__ == "__main__":
    print(cyclicSort([3, 1, 5, 4, 2]))   # Expected: [1, 2, 3, 4, 5]
    print(cyclicSort([2, 1]))             # Expected: [1, 2]
    print(cyclicSort([1]))                # Expected: [1]

'''
Pattern
✅ Cyclic Sort (numbers in a known range 1..n)

Key Observation
Because the values are exactly 1..n, each value has ONE correct index (v-1).
Swapping a value straight to its home means every number reaches its slot in a
bounded number of swaps -> O(n) total, O(1) space. Whenever numbers come from a
fixed range 1..n (or 0..n), think cyclic sort.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No. You must touch every element; this does it in-place with O(n) swaps.
'''
