'''
1. Subarray XOR Equals K (Medium)
Problem Statement

Given an integer array nums and an integer k, return the number of contiguous
subarrays whose XOR of all elements equals k.

Example
Input:
nums = [4,2,2,6,4], k = 6

Output:
4
'''

def subarrayXor(nums, k):

    seen = {0: 1}       # prefix_xor -> count
    running = 0
    count = 0

    for x in nums:
        running ^= x
        # we need a previous prefix p with p ^ running == k  =>  p == running ^ k
        count += seen.get(running ^ k, 0)
        seen[running] = seen.get(running, 0) + 1

    return count


if __name__ == "__main__":
    print(subarrayXor([4, 2, 2, 6, 4], 6))    # Expected: 4
    print(subarrayXor([5, 6, 7, 8, 9], 5))    # Expected: 2

'''
Pattern
✅ Prefix XOR + Hashmap (same shape as Subarray Sum = K, with ^ instead of +)

Key Observation
xor(i..j) = prefix[j] ^ prefix[i-1]. Wanting that = k means a previous prefix
equals (running ^ k), because XOR is its own inverse.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No.
'''
