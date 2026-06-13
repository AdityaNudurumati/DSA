'''
1. Contains Duplicate (Easy)
Problem Statement

Given an integer array, return True if any value appears at least twice, and
False if every element is distinct.

Example
Input: [1, 2, 3, 1]    -> True   (1 repeats)
Input: [1, 2, 3, 4]    -> False  (all distinct)
'''

def containsDuplicate(nums):

    seen = set()
    for x in nums:
        if x in seen:           # already encountered -> duplicate found
            return True
        seen.add(x)             # record first sighting

    return False


if __name__ == "__main__":
    print(containsDuplicate([1, 2, 3, 1]))     # Expected: True
    print(containsDuplicate([1, 2, 3, 4]))     # Expected: False

'''
Pattern
✅ Set-Based Hashing (set membership)

Key Observation
A set gives O(1) membership tests. Stream through the array; the first value
that is already in the set proves a duplicate, so we can return early without
scanning the rest.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ Without extra space you would need an O(n log n) sort; the set trades space
for optimal linear time.
'''
