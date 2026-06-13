'''
1. Range Addition (Medium)
Problem Statement

You have an array of `length` zeros. Apply a list of updates, where each update
[start, end, inc] adds inc to every element in nums[start..end] (inclusive).
Return the final array.

Do all updates in O(length + #updates) using a difference array.

Example
Input:
length = 5
updates = [[1,3,2],[2,4,3],[0,2,-2]]

Output:
[-2,0,3,5,3]
'''

def getModifiedArray(length, updates):

    diff = [0] * (length + 1)   # extra slot so end+1 is always valid

    # record only the boundaries of each range update
    for start, end, inc in updates:
        diff[start] += inc
        diff[end + 1] -= inc

    # prefix-sum the diff array to recover the real values
    result = [0] * length
    running = 0
    for i in range(length):
        running += diff[i]
        result[i] = running

    return result


if __name__ == "__main__":
    print(getModifiedArray(5, [[1, 3, 2], [2, 4, 3], [0, 2, -2]]))
    # Expected: [-2, 0, 3, 5, 3]

'''
Pattern
✅ Difference Array (inverse of prefix sum)

Key Observation
A range update +inc on [start, end] becomes two point edits: +inc at start and
-inc at end+1. Prefix-summing the diff array applies every update at once.

| Metric | Value              |
| ------ | ------------------ |
| Time   | O(length + U)      |
| Space  | O(length)          |

Better Possible?
❌ No. Naively applying each update is O(length * U).
'''
