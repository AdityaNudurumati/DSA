'''
1. Monotone Increasing Digits (Medium)
Problem Statement

Given a non-negative integer n, find the largest number that is less than or
equal to n whose digits are in non-decreasing order (each digit <= the digit to
its right). Return it as an integer.

Example
Input:
n = 332

Output:
299
'''

def monotoneIncreasingDigits(n):

    d = list(str(n))            # digits as characters, e.g. 332 -> ['3','3','2']
    mark = len(d)               # index from which everything becomes '9'

    # Walk right-to-left. On a violation (left digit > right digit), the greedy
    # safe move is: decrement the left digit by 1 and remember this position so
    # every digit after it can be maxed to '9' (keeps the number as large as
    # possible while staying <= n and non-decreasing).
    for i in range(len(d) - 1, 0, -1):
        if d[i - 1] > d[i]:
            d[i - 1] = str(int(d[i - 1]) - 1)
            mark = i

    # Flood everything from the (possibly updated) mark onward with '9'.
    for i in range(mark, len(d)):
        d[i] = '9'

    return int(''.join(d))


if __name__ == "__main__":
    print(monotoneIncreasingDigits(10))     # Expected: 9
    print(monotoneIncreasingDigits(1234))   # Expected: 1234
    print(monotoneIncreasingDigits(332))    # Expected: 299

'''
Pattern
✅ Monotonic Greedy — walk from the right, drop & borrow on a decrease

Greedy Rule & Why It's Safe
Scan adjacent pairs from the right. At the first violation d[i-1] > d[i], we must
lower the more significant digit d[i-1] (we cannot raise d[i] without exceeding n
once the prefix is fixed). Decrementing d[i-1] by exactly 1 is the smallest change
that fixes that step, and once a more significant digit drops, every less
significant digit is free to become '9' — the largest value that keeps the result
<= n. Going right-to-left is essential: a borrow may create a NEW violation further
left (e.g. 332 -> 3'2'2 -> still 3>2 -> 2 9 9), and the rightward pass naturally
re-checks it. Any larger candidate would either break monotonicity or exceed n, so
the choice is safe.

| Metric | Value     |
| ------ | --------- |
| Time   | O(log n)  |  # one pass over the ~log10(n) digits
| Space  | O(log n)  |  # the digit list

Better Possible?
❌ No. Output already has as many digits as n, and a single linear digit pass is
optimal.
'''
