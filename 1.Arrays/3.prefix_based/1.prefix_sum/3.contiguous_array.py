'''
3. Contiguous Array (Medium)
Problem Statement

Given a binary array nums (only 0s and 1s), return the length of the longest
contiguous subarray with an equal number of 0s and 1s.

Example
Input:
nums = [0,1,0]

Output:
2
Explanation:
[0,1] (or [1,0]) has one 0 and one 1.
'''

def findMaxLength(nums):

    # Treat 0 as -1: a subarray is balanced iff its running sum is 0,
    # i.e. two prefixes share the same running value.
    first_index = {0: -1}   # running value -> earliest index it appeared
    running = 0
    best = 0

    for i, x in enumerate(nums):

        running += 1 if x == 1 else -1

        if running in first_index:
            best = max(best, i - first_index[running])
        else:
            first_index[running] = i

    return best


if __name__ == "__main__":
    print(findMaxLength([0, 1]))                       # Expected: 2
    print(findMaxLength([0, 1, 0]))                    # Expected: 2
    print(findMaxLength([0, 0, 1, 0, 0, 0, 1, 1]))     # Expected: 6

'''
Pattern
✅ Prefix Sum (0 -> -1 trick) + Hashmap of first index

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No.
'''
