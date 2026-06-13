'''
2. Average of Subarrays of Size K (Easy)
Problem Statement

Given an integer array nums and an integer k, return a list of the averages of
every contiguous subarray of size k.

Example
Input:
nums = [1,3,2,6,-1,4,1,8,2], k = 5

Output:
[2.2, 2.8, 2.4, 3.6, 2.8]
'''

def findAverages(nums, k):

    result = []
    window_sum = 0

    for right in range(len(nums)):

        window_sum += nums[right]

        if right >= k - 1:
            result.append(window_sum / k)
            window_sum -= nums[right - k + 1]

    return result


if __name__ == "__main__":
    print(findAverages([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))
    # Expected: [2.2, 2.8, 2.4, 3.6, 2.8]

'''
Pattern
✅ Fixed-Size Sliding Window

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  | (excluding the output list)

Better Possible?
❌ No.
'''
