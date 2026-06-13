'''
1. XOR Queries of a Subarray (Medium)
Problem Statement

You are given an array arr of positive integers and a list of queries where
queries[i] = [l, r].

For each query compute the XOR of the elements arr[l] ^ arr[l+1] ^ ... ^ arr[r]
(both endpoints inclusive) and return a list of all the answers.

Input:
arr = [1, 3, 4, 8]
queries = [[0, 1], [1, 2], [0, 3], [3, 3]]

Output:
[2, 7, 14, 8]

Explanation:
[0,1] -> 1 ^ 3       = 2
[1,2] -> 3 ^ 4       = 7
[0,3] -> 1 ^ 3 ^ 4 ^ 8 = 14
[3,3] -> 8           = 8
'''

def xorQueries(arr, queries):
    # Bit trick: prefix XOR. Because a ^ a = 0, the XOR of a range telescopes.
    # pre[i] = arr[0] ^ ... ^ arr[i-1]  (pre[0] = 0).
    # xor(l..r) = pre[r+1] ^ pre[l]  -> the shared prefix arr[0..l-1] cancels out.
    n = len(arr)
    pre = [0] * (n + 1)
    for i, x in enumerate(arr):
        pre[i + 1] = pre[i] ^ x

    # Each query answered in O(1) using the prefix array.
    return [pre[r + 1] ^ pre[l] for l, r in queries]


if __name__ == "__main__":
    arr = [1, 3, 4, 8]
    queries = [[0, 1], [1, 2], [0, 3], [3, 3]]
    print(xorQueries(arr, queries))  # Expected: [2, 7, 14, 8]


'''
Pattern
Prefix XOR (Range / Prefix XOR).
Build pre[] where pre[i+1] = pre[i] ^ arr[i]. Since XOR is its own inverse
(a ^ a = 0), the XOR over a range [l, r] equals pre[r+1] ^ pre[l]: the prefix
arr[0..l-1] appears in both terms and cancels, leaving exactly arr[l..r].
This turns each range query from O(n) into O(1) after an O(n) precompute.

| Metric | Value          |
| ------ | -------------- |
| Time   | O(n + q)       |
| Space  | O(n)           |

Better Possible?
No. We must read every element once to build the prefix array (O(n)) and emit
one answer per query (O(q)), so O(n + q) time is optimal. Space could drop to
O(1) extra only if queries were offline-sorted, but the prefix array is the
standard, optimal approach for arbitrary online range queries.
'''
