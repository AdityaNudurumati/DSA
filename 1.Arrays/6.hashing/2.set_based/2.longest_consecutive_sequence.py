'''
2. Longest Consecutive Sequence (Medium)
Problem Statement

Given an unsorted integer array nums, return the length of the longest run of
consecutive integers (values differing by 1). Must run in O(n).

Example
Input:
nums = [100,4,200,1,3,2]

Output:
4
Explanation:
The run [1,2,3,4] has length 4.
'''

def longestConsecutive(nums):

    num_set = set(nums)
    best = 0

    for x in num_set:

        # only start counting from the smallest element of a run
        if x - 1 not in num_set:
            length = 1
            while x + length in num_set:
                length += 1
            best = max(best, length)

    return best


if __name__ == "__main__":
    print(longestConsecutive([100, 4, 200, 1, 3, 2]))            # Expected: 4
    print(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))   # Expected: 9
    print(longestConsecutive([]))                                # Expected: 0

'''
Pattern
✅ Set + start-of-run check

Key Observation
Put everything in a set. Only begin a count when x-1 is absent (x starts a run), so
each element is visited at most twice overall -> O(n), not O(n log n).

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No. Sorting would be O(n log n).
'''
