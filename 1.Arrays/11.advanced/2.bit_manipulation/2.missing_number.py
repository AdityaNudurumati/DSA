'''
2. Missing Number (Easy)
Problem Statement

Given an array nums containing n distinct numbers in the range [0, n], return the
one number in the range that is missing.

Example
Input:
nums = [3,0,1]

Output:
2
'''

def missingNumber(nums):

    n = len(nums)
    result = n               # start with the top of the range

    # XOR every index and value; the missing number is the one index never cancelled
    for i, x in enumerate(nums):
        result ^= i ^ x

    return result


if __name__ == "__main__":
    print(missingNumber([3, 0, 1]))                       # Expected: 2
    print(missingNumber([0, 1]))                           # Expected: 2
    print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))      # Expected: 8

'''
Pattern
✅ XOR of indices and values

Key Observation
XOR-ing 0..n with all array values cancels every present number, leaving the
missing one. (The Gauss-sum n*(n+1)/2 - sum(nums) also works.)

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No.
'''
