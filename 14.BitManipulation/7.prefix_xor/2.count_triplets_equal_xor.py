'''
2. Count Triplets That Can Form Two Arrays of Equal XOR (Medium)
Problem Statement

You are given an array of integers arr.

Pick three indices i, j, k with 0 <= i < j <= k < len(arr). Define:
    a = arr[i] ^ arr[i+1] ^ ... ^ arr[j-1]
    b = arr[j] ^ arr[j+1] ^ ... ^ arr[k]

Count the number of triplets (i, j, k) for which a == b.

Input:
arr = [2, 3, 1, 6, 7]

Output:
4

Explanation:
The valid (i, j, k) triplets are (0,3,4), (0,1,4), (0,2,4) and (2,3,4),
each giving a == b.

Input:
arr = [1, 1, 1, 1, 1]

Output:
10
'''

def countTriplets(arr):
    # Bit trick: prefix XOR + the key observation a == b  <=>  a ^ b == 0.
    # a ^ b is the XOR of the whole range arr[i..k], i.e. pre[k+1] ^ pre[i].
    # So a == b means pre[i] == pre[k+1]. Whenever two prefix values are equal,
    # j can be ANY index in (i, k], giving (k - i) valid triplets for that pair.
    n = len(arr)
    pre = [0] * (n + 1)
    for idx, x in enumerate(arr):
        pre[idx + 1] = pre[idx] ^ x

    # For every pair of prefix indices i < kk (kk = k+1) with equal prefix XOR,
    # add (kk - i - 1) = (k - i) to the count.
    count = 0
    for i in range(n + 1):
        for kk in range(i + 1, n + 1):
            if pre[i] == pre[kk]:
                count += (kk - i - 1)
    return count


if __name__ == "__main__":
    arr1 = [2, 3, 1, 6, 7]
    print(countTriplets(arr1))  # Expected: 4

    arr2 = [1, 1, 1, 1, 1]
    print(countTriplets(arr2))  # Expected: 10


'''
Pattern
Prefix XOR (Range / Prefix XOR).
The condition a == b is equivalent to a ^ b == 0. Since a ^ b is the XOR of the
entire range arr[i..k] = pre[k+1] ^ pre[i], the requirement collapses to
pre[i] == pre[k+1]. The middle index j is then free to be any of the (k - i)
positions strictly between i and k+1, so each matching prefix pair contributes
(k - i) triplets. This removes any dependence on j and reduces a triple loop to
a double loop over prefix values.

| Metric | Value   |
| ------ | ------- |
| Time   | O(n^2)  |
| Space  | O(n)    |

Better Possible?
Yes for the constant work, but O(n^2) is already efficient for the constraints.
Using a hashmap keyed by prefix value (tracking count and sum of indices seen),
the answer can be produced in a single O(n) pass: for each kk, the contribution
is count[pre[kk]] * (kk - 1) - sumIndices[pre[kk]]. That improves time to O(n)
with O(n) space. The O(n^2) version here is kept for clarity of the bit trick.
'''
