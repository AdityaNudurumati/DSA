'''
1. Happy Number (Easy)
Problem Statement

A happy number is defined by repeatedly replacing the number with the sum of the
squares of its digits. If this process eventually reaches 1, the number is happy.
If it loops endlessly in a cycle that never includes 1, it is not happy. Return True
if n is a happy number, otherwise False.

Example
Input:  19  -> True    (1^2+9^2=82, 8^2+2^2=68, 6^2+8^2=100, 1^2+0^2+0^2=1)
        2   -> False   (the chain falls into a cycle that never reaches 1)
'''

def isHappy(n):

    def next_value(x):                      # sum of squares of the digits of x
        total = 0
        while x > 0:
            x, d = divmod(x, 10)
            total += d * d
        return total

    seen = set()                            # set used for O(1) membership testing
    while n != 1 and n not in seen:         # stop at 1 (happy) or a repeat (cycle)
        seen.add(n)
        n = next_value(n)
    return n == 1                           # reached 1 => happy, else trapped in a cycle


if __name__ == "__main__":
    print(isHappy(19))                      # Expected: True
    print(isHappy(2))                       # Expected: False

'''
Pattern
✅ Membership Testing (a set detects when the sequence revisits a value)

Key Observation
The digit-square sequence is deterministic, so any non-terminating run must repeat a
value. Storing every value in a set lets us catch that repeat in O(1) and declare the
number unhappy without looping forever.

| Metric | Value |
| ------ | ----- |
| Time   | O(log n) per step, bounded total steps -> effectively O(log n) |
| Space  | O(log n) values stored in the set |

Better Possible?
✅ Floyd's cycle detection (slow/fast pointers) removes the set for O(1) space, but
the set version is clearer and the values are tiny.
'''
