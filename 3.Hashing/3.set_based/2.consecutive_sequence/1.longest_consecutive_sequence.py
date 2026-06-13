'''
1. Longest Consecutive Sequence (Medium)
Problem Statement

Given an unsorted array of integers, return the length of the longest run of
consecutive integers (values that differ by 1). The numbers may appear in any
order and the algorithm should run in linear time.

Example
Input: [100, 4, 200, 1, 3, 2]   -> 4   (the run 1,2,3,4)
Input: [0,3,7,2,5,8,4,6,0,1]    -> 9   (the run 0..8)
Input: []                       -> 0
'''

def longestConsecutive(nums):

    s = set(nums)               # O(1) membership; also drops duplicates
    best = 0

    for x in s:
        if x - 1 not in s:      # x is the START of a run (no predecessor)
            length = 1
            while x + length in s:   # walk the run forward
                length += 1
            best = max(best, length)

    return best


if __name__ == "__main__":
    print(longestConsecutive([100, 4, 200, 1, 3, 2]))      # Expected: 4
    print(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # Expected: 9
    print(longestConsecutive([]))                          # Expected: 0

'''
Pattern
✅ Set-Based Hashing (set + start-of-run check)

Key Observation
Dump everything into a set, then only start counting from a value x whose
predecessor x-1 is absent. Each element is visited at most twice (once in the
outer loop, once while extending its run), so the whole scan is O(n) despite
the inner while loop.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ Linear time is optimal; every element must be examined at least once.
'''
