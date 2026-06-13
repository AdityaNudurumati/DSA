'''
1. Jump Game (Medium)
Problem Statement

Given an integer array nums where nums[i] is the maximum jump length from index i,
return True if you can reach the last index starting from index 0.

Example
Input:
nums = [2,3,1,1,4]

Output:
True
'''

def canJump(nums):

    farthest = 0

    for i, jump in enumerate(nums):
        if i > farthest:           # a gap we can't cross
            return False
        farthest = max(farthest, i + jump)

    return True


if __name__ == "__main__":
    print(canJump([2, 3, 1, 1, 4]))   # Expected: True
    print(canJump([3, 2, 1, 0, 4]))   # Expected: False

'''
Pattern
✅ Greedy reachability (track the farthest reachable index)

Key Observation
Sweep left to right keeping the farthest index reachable so far. If the current
index ever exceeds it, the end is unreachable.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No.
'''
