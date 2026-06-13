'''
1. Assign Cookies (Easy)
Problem Statement

You are a parent who wants to give cookies to children. Each child i has a greed
factor g[i] (the minimum cookie size that will content them). Each cookie j has a
size s[j]. A child is content if they get a cookie with s[j] >= g[i], and each
cookie can go to at most one child. Return the maximum number of content children.

Example
Input:
g = [1, 2, 3]
s = [1, 1]

Output:
1

Explanation:
Two cookies of size 1 can satisfy at most the child with greed 1.
'''

def findContentChildren(g, s):

    # Greedy rule: sort both. Walk children (smallest greed first) and cookies
    # (smallest size first); feed the smallest cookie that satisfies the current
    # child to that child. Spend the smallest adequate cookie so larger cookies
    # stay available for greedier children.
    g.sort()
    s.sort()

    child = 0           # index into greed factors
    cookie = 0          # index into cookie sizes

    while child < len(g) and cookie < len(s):
        # If this cookie satisfies the current (smallest unserved) child, assign it.
        if s[cookie] >= g[child]:
            child += 1
        # Either way this cookie is now used up / too small, so advance it.
        cookie += 1

    return child        # number of content children


if __name__ == "__main__":
    print(findContentChildren([1, 2, 3], [1, 1]))   # Expected: 1
    print(findContentChildren([1, 2], [1, 2, 3]))   # Expected: 2

'''
Pattern
Sorting Greedy (Smallest First, two-pointer match)

Greedy rule & why it's safe
Sort children by greed and cookies by size; for the least greedy unserved child,
give the smallest cookie that still satisfies them.
Exchange argument: suppose an optimal assignment gives child c a cookie larger than
the smallest cookie that fits c. Swap so c takes that smallest fitting cookie and the
larger cookie returns to the pool. The larger cookie can satisfy any child the smaller
one could (it is bigger), so no previously-content child becomes unhappy and the count
never drops. Repeating these swaps turns any optimum into the greedy assignment, so the
greedy count is optimal. Serving the smallest greed first is symmetric: a smaller-greed
child is satisfied by any cookie a larger-greed child would accept, so prioritizing them
never wastes capacity.

| Metric | Value      |
| ------ | ---------- |
| Time   | O(n log n) |  (two sorts dominate the single linear pass)
| Space  | O(1)       |  (in-place sort, constant extra)

Better Possible?
No — the two pointers each cross their array once, so the linear pass is already
optimal; the O(n log n) sort is the unavoidable lower bound for this matching.
'''
