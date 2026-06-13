'''
3. Happy Number (Easy)
Problem Statement

A happy number is defined by: repeatedly replace the number by the sum of the
squares of its digits; if this reaches 1 it is happy, otherwise it loops forever.
Return True if n is happy.

Example
Input:
n = 19

Output:
True
Explanation:
1²+9²=82 -> 8²+2²=68 -> 6²+8²=100 -> 1²+0²+0²=1
'''

def isHappy(n):

    def square_digits(x):
        total = 0
        while x:
            d = x % 10
            total += d * d
            x //= 10
        return total

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = square_digits(n)

    return n == 1


if __name__ == "__main__":
    print(isHappy(19))   # Expected: True
    print(isHappy(2))    # Expected: False

'''
Pattern
✅ Cycle detection on a number sequence

Key Observation
The transform either reaches 1 or enters a cycle. Track seen values (or use
Floyd's tortoise/hare) to detect the loop and stop.

| Metric | Value |
| ------ | ----- |
| Time   | O(log n) per step, bounded total |
| Space  | O(1) with Floyd, O(k) with a set  |

Better Possible?
Floyd's two-pointer cycle detection removes the set -> O(1) space.
'''
