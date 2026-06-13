'''
2. Stone Game (Medium)   [LC877]
Problem Statement

Alice and Bob play with piles of stones arranged in a row; piles[i] is the
number of stones in pile i. The total number of stones is odd. Players
alternate turns, Alice first. On each turn a player takes the entire pile
from EITHER the start or the end of the row. The player with more stones wins.

Assuming both play optimally, return True if Alice wins, else False.

Input:
piles = [5, 3, 4, 5]

Output:
True

Explanation:
Alice takes the last pile (5). Whatever Bob takes from the ends (5 or 3),
Alice can always respond to finish ahead. Alice wins.
'''

from functools import lru_cache


def stoneGame(piles):
    n = len(piles)

    # Minimax via score difference.
    # state: diff(i, j) = best (current player's stones - opponent's stones)
    #        achievable from the subarray piles[i..j], current player to move.
    # transition: take left  -> piles[i] - diff(i+1, j)
    #             take right -> piles[j] - diff(i, j-1)
    #             diff(i, j) = max(left, right)
    # base: i > j -> 0  (no stones, zero difference)
    @lru_cache(maxsize=None)
    def diff(i, j):
        if i > j:
            return 0
        take_left = piles[i] - diff(i + 1, j)
        take_right = piles[j] - diff(i, j - 1)
        return max(take_left, take_right)

    # Alice wins iff her optimal lead over the whole row is positive.
    return diff(0, n - 1) > 0


if __name__ == "__main__":
    print(stoneGame([5, 3, 4, 5]))    # Expected: True
    print(stoneGame([3, 7, 2, 3]))    # Expected: True


'''
Pattern
✅ Decision DP (Game Choices -> Minimax)
Tracking the score DIFFERENCE collapses two players into one recurrence: the
mover maximizes (own pile - opponent's best diff on the rest). Overlapping
subarrays [i..j] are memoized over an interval state.
| Metric | Value   |
| ------ | ------- |
| Time   | O(n^2)  |
| Space  | O(n^2)  |
Better Possible?
✅ Yes
For THIS variant (even count of piles, odd total) Alice always wins, so the
answer is trivially True in O(1). The O(n^2) minimax is the general solution
that works regardless of those guarantees.
'''
