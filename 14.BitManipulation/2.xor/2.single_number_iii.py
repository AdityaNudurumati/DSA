'''
2. Single Number III (Medium)
Problem Statement

Given an integer array nums in which exactly two elements appear only once and
all the other elements appear exactly twice, find the two elements that appear
only once.

Return the answer in any order. The solution must run in linear time and use
only constant extra space.

Input:
nums = [1,2,1,3,2,5]

Output:
[3,5]

Explanation:
1 and 2 appear twice (cancel out); 3 and 5 appear once -> answer is [3, 5].
'''

def singleNumber(nums):
    # Bit trick step 1: XOR everything. Pairs cancel (a^a=0), leaving a^b where
    # a and b are the two unique numbers.
    xor_all = 0
    for n in nums:
        xor_all ^= n

    # Step 2: a != b, so a^b has at least one set bit. Isolate the lowest set bit
    # with x & (-x). a and b differ at this bit, so it partitions nums into two
    # groups: one containing a, the other containing b.
    diff = xor_all & (-xor_all)

    # Step 3: XOR within each group. Paired numbers still cancel inside their
    # group, isolating a in one group and b in the other.
    a = b = 0
    for n in nums:
        if n & diff:
            a ^= n
        else:
            b ^= n
    return [a, b]


if __name__ == "__main__":
    print(sorted(singleNumber([1, 2, 1, 3, 2, 5])))   # Expected: [3, 5]
    print(sorted(singleNumber([-1, 0])))              # Expected: [-1, 0]
    print(sorted(singleNumber([0, 1])))               # Expected: [0, 1]


'''
Pattern
XOR + partition by a differing bit.
Bit trick: XOR-ing all values cancels the duplicate pairs and yields a^b. Since
a and b differ, a^b has a set bit; the lowest set bit (x & -x) splits the array
into two groups that each contain exactly one unique number, so a second XOR
pass per group isolates each. Negative inputs work directly because Python's
& on a^b's lowest set bit consistently classifies each number.
| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |
Better Possible?
No. Two linear passes with O(1) space is optimal; every element must be read
at least once.
'''
