'''
2. Sum Over Subsets (SOS DP) (Hard)
Problem Statement

Given an array f of length 2^n indexed by bitmasks, compute F where
F[mask] = sum of f[submask] over all submasks of mask (submask & mask == submask).

The naive approach enumerates every submask of every mask in O(3^n). SOS DP
does it in O(n * 2^n) by adding one bit dimension at a time.

Input:
f = [1, 2, 3, 4]          # n = 2 bits, indices 00, 01, 10, 11

Output:
F = [1, 3, 4, 10]

Explanation:
F[00]=f[00]=1
F[01]=f[00]+f[01]=1+2=3
F[10]=f[00]+f[10]=1+3=4
F[11]=f[00]+f[01]+f[10]+f[11]=1+2+3+4=10
'''


def sum_over_subsets(f, n):
    # State: after processing bit i, F[mask] = sum of f[sub] over submasks that
    #        differ from mask only in bits 0..i.
    # Transition: for each bit i, if mask has bit i set, fold in the value of the
    #        same mask with bit i cleared:
    #            F[mask] += F[mask ^ (1 << i)]
    # Base: F[mask] = f[mask] (no bits processed -> only the mask itself).
    F = list(f)                          # base case
    for i in range(n):
        for mask in range(1 << n):
            if mask & (1 << i):
                F[mask] += F[mask ^ (1 << i)]
    return F


if __name__ == "__main__":
    f = [1, 2, 3, 4]                     # n = 2 bits
    print(sum_over_subsets(f, 2))        # Expected: [1, 3, 4, 10]


'''
Pattern
✅ SOS DP (Sum Over Subsets)
A naive subset-sum enumerates each mask's submasks (the famous submask trick),
costing O(3^n). SOS DP instead processes ONE bit dimension at a time: bit i acts
as a knapsack-style "include the contribution coming from clearing bit i" step.
After all n bits are folded in, every submask has been accumulated exactly once.
This is itself a space/time optimization of subset aggregation, done in place.

| Metric | Value        |
| ------ | ------------ |
| Time   | O(n * 2^n)   |
| Space  | O(2^n)       |

Better Possible?
❌ Not meaningfully. The output alone has 2^n entries, so any algorithm is at
least O(2^n). SOS DP's O(n * 2^n) is the standard optimum and a large
improvement over the O(3^n) naive submask enumeration. Space is already optimal
(in-place over the input-sized array).
'''
