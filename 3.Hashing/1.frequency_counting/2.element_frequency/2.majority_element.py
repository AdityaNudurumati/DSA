'''
2. Majority Element (Easy)
Problem Statement

Given an array nums of size n, return the majority element — the element that
appears more than n // 2 times. You may assume the majority element always
exists.

Example
Input:
nums = [2, 2, 1, 1, 1, 2, 2]

Output:
2
'''

def majorityElement(nums):

    # Boyer-Moore voting: keep a candidate and a running balance
    candidate = None
    count = 0

    for x in nums:
        # when balance hits zero, adopt the current value as the new candidate
        if count == 0:
            candidate = x
        # same value reinforces the candidate, different value cancels one vote
        count += 1 if x == candidate else -1

    return candidate


if __name__ == "__main__":
    print(majorityElement([3, 2, 3]))                 # Expected: 3
    print(majorityElement([2, 2, 1, 1, 1, 2, 2]))     # Expected: 2

'''
Pattern
✅ Element Frequency Counting (Boyer-Moore majority vote)

Key Observation
A true majority element occurs more than n/2 times, so pairing it off against
every other element still leaves it standing. The voting balance never drops the
real majority for good, so the final candidate is the answer.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
A Counter solution is also O(n) time but O(n) space. Boyer-Moore achieves the
optimal O(1) space, so this cannot be improved.
'''
