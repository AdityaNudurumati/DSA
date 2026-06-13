'''
2. Jump Game II (Medium)
Problem Statement

Given an integer array nums where nums[i] is the maximum jump length from index i,
return the minimum number of jumps to reach the last index. You can always reach it.

Example
Input:
nums = [2,3,1,1,4]

Output:
2
Explanation:
Jump 1 step (0->1), then 3 steps (1->4).
'''

def jump(nums):

    jumps = 0
    cur_end = 0          # boundary of the current jump's reach
    farthest = 0         # farthest reachable while inside this boundary

    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == cur_end:             # must jump now to go further
            jumps += 1
            cur_end = farthest

    return jumps


if __name__ == "__main__":
    print(jump([2, 3, 1, 1, 4]))   # Expected: 2
    print(jump([2, 3, 0, 1, 4]))   # Expected: 2

'''
Pattern
✅ Greedy BFS-by-levels (implicit level boundaries)

Key Observation
Each "level" is the set of indices reachable in the same number of jumps. Extend the
boundary to the farthest index seen; bump the jump count when you hit the boundary.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No.
'''
