'''
1. Can I Win (Medium)
Problem Statement

In the "100 game", two players take turns adding, to a running total, any
integer from 1 to maxChoosableInteger. The player who first causes the running
total to reach or exceed desiredTotal wins. The same integer cannot be reused.

Given maxChoosableInteger and desiredTotal, assuming both players play
optimally, return True if the first player can force a win.

Example
Input:
maxChoosableInteger = 10, desiredTotal = 11
Output:
False

Input:
maxChoosableInteger = 10, desiredTotal = 0
Output:
True

Input:
maxChoosableInteger = 10, desiredTotal = 40
Output:
False
'''

from functools import lru_cache


def canIWin(maxChoosableInteger, desiredTotal):
    # If the desired total is already met, first player wins without moving.
    if desiredTotal <= 0:
        return True

    # If even the sum of every choosable number cannot reach the total,
    # nobody can win -> first player cannot win.
    if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
        return False

    # State compression: a single `mask` integer encodes which numbers are used.
    # Bit i (0-indexed) set => number (i + 1) has already been chosen.
    # dp[mask] = can the player to move force a win given this used-set.
    @lru_cache(None)
    def win(mask, remaining):
        for i in range(maxChoosableInteger):
            # Skip numbers whose bit is already set (already used).
            if (mask >> i) & 1:
                continue
            num = i + 1
            # Win now (num finishes the game) OR the opponent loses from the
            # resulting state (mask with bit i set).
            if num >= remaining or not win(mask | (1 << i), remaining - num):
                return True
        return False

    return win(0, desiredTotal)


if __name__ == "__main__":
    print(canIWin(10, 11))  # Expected: False
    print(canIWin(10, 0))   # Expected: True
    print(canIWin(10, 40))  # Expected: False

'''
Pattern
Bitmask DP (game-theory memo over a used-number mask)

Bit trick & why
We must remember exactly WHICH numbers are still available, and n <= 20, so the
chosen-set is encoded in one integer `mask`: bit i set means number (i+1) is
taken. "check used" is (mask >> i) & 1; "mark used" is mask | (1 << i). This
turns an exponential set state into a hashable int, letting lru_cache memoize
each distinct subset once. A position is winning if some move wins immediately
or leaves the opponent in a losing position (standard minimax recursion). The
`remaining` argument is derivable from the mask, but passing it avoids re-summing.

| Metric | Value          |
| ------ | -------------- |
| Time   | O(2^n * n)     |
| Space  | O(2^n)         |

Better Possible?
No. There are 2^n reachable subset states and each is processed once with an
O(n) scan; the exponential factor is inherent to the subset state space.
'''
