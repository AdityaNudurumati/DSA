'''
1. Two Sum II (Easy)
Problem Statement

You are given a 1-indexed sorted array of integers numbers and an integer target.

Find two numbers such that they add up to target.

Return the indices of the two numbers as an array [index1, index2].

You may assume that exactly one solution exists.

Input:
numbers = [2,7,11,15]
target = 9

Output:
[1,2]

Explanation:
2 + 7 = 9
'''

def twoSum(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        current = numbers[left] + numbers[right]

        if current == target:
            return [left + 1, right + 1]

        elif current < target:
            left += 1

        else:
            right -= 1


if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    print(twoSum(numbers, target))  # Expected: [1, 2]


'''
Best Pattern
✅ Two Pointers
Because array is already sorted.
| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |
Can we do better?
❌ No

Need to inspect elements at least once.
Optimal = O(n)
'''