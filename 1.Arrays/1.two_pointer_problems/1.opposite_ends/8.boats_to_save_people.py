'''
8. Boats to Save People (Medium)
Problem Statement

Given an array people where people[i] is the weight of the i-th person, and an
integer limit (the max weight a boat can carry), return the minimum number of boats.

Each boat carries at most 2 people, as long as their combined weight <= limit.

Example
Input:
people = [3,2,2,1]
limit = 3

Output:
3

Explanation:
Boats: (1,2), (2), (3)
'''

def numRescueBoats(people, limit):

    people.sort()

    left = 0
    right = len(people) - 1

    boats = 0

    while left <= right:

        # Try to pair the lightest with the heaviest.
        if people[left] + people[right] <= limit:
            left += 1

        # The heaviest always takes a boat (alone or paired).
        right -= 1
        boats += 1

    return boats


if __name__ == "__main__":
    print(numRescueBoats([1, 2], 3))           # Expected: 1
    print(numRescueBoats([3, 2, 2, 1], 3))     # Expected: 3
    print(numRescueBoats([3, 5, 3, 4], 5))     # Expected: 4

'''
Pattern
✅ Sorting + Opposite-Ends Two Pointers (Greedy)

Key Observation
Pair the lightest with the heaviest. If they don't fit, the heaviest must go alone.
Either way the heaviest leaves on this boat, so move right inward every step.

| Metric | Value      |
| ------ | ---------- |
| Time   | O(n log n) |  (dominated by the sort)
| Space  | O(1)       |

Better Possible?
❌ No — sorting is required to pair optimally.
'''
