'''
3. Sqrt(x) (Easy)
Problem Statement

Given a non-negative integer x, return the integer square root of x, i.e.
the largest integer r such that r*r <= x (truncate the fractional part).

Use binary search implemented recursively over the answer space.

Input:
x = 8

Output:
2

Explanation:
sqrt(8) = 2.828..., truncated to 2 (2*2=4 <= 8, 3*3=9 > 8).
'''

def mySqrt(x):
    # 0 and 1 are their own integer square roots.
    if x < 2:
        return x
    # Search the answer space [1, x] recursively, tracking best valid r.
    return search(x, 1, x)


def search(x, low, high):
    # No candidates left: low-1 is the largest r with r*r <= x.
    if low > high:
        return high
    mid = (low + high) // 2
    if mid * mid == x:
        return mid
    elif mid * mid < x:
        # mid could be the answer; look for something larger.
        return search(x, mid + 1, high)
    else:
        # mid too big; shrink the upper bound.
        return search(x, low, mid - 1)


if __name__ == "__main__":
    print(mySqrt(8))   # Expected: 2
    print(mySqrt(16))  # Expected: 4
    print(mySqrt(0))   # Expected: 0
    print(mySqrt(1))   # Expected: 1


'''
Pattern
✅ Binary Search on the Answer (recursive)
The integer sqrt is monotonic, so we binary-search r in [1, x]: if r*r is too
small move right, if too big move left, halving the range each step.
| Metric | Value    |
| ------ | -------- |
| Time   | O(log x) |
| Space  | O(log x) |  (recursion stack depth)
Better Possible?
❌ Not asymptotically
Newton's method also converges in O(log x) (faster constant). An iterative
binary search drops space to O(1).
'''
