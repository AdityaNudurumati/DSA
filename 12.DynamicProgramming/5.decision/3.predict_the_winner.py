'''
3. Predict the Winner (Medium)   [LC486]
Problem Statement

You are given an integer array nums. Two players take turns, player 1 first.
On each turn a player picks a number from EITHER end of the array and adds it
to their score; that number is then removed. Play continues until the array
is empty.

Return True if player 1 can win (a tie counts as a win for player 1),
assuming both players play optimally to maximize their own score.

Input:
nums = [1, 5, 2]

Output:
False

Explanation:
Player 1 picks 1 or 2; player 2 then grabs 5. Player 1's best total is 3,
player 2 gets 5, so player 1 cannot win.
'''

from functools import lru_cache


def predictTheWinner(nums):
    n = len(nums)

    # Minimax via score difference (same engine as Stone Game).
    # state: diff(i, j) = best (current player score - opponent score) over
    #        nums[i..j] with current player to move.
    # transition: pick left  -> nums[i] - diff(i+1, j)
    #             pick right -> nums[j] - diff(i, j-1)
    #             diff(i, j) = max(left, right)
    # base: i > j -> 0
    @lru_cache(maxsize=None)
    def diff(i, j):
        if i > j:
            return 0
        pick_left = nums[i] - diff(i + 1, j)
        pick_right = nums[j] - diff(i, j - 1)
        return max(pick_left, pick_right)

    # Player 1 wins on a non-negative final lead (tie counts as a win).
    return diff(0, n - 1) >= 0


if __name__ == "__main__":
    print(predictTheWinner([1, 5, 2]))        # Expected: False
    print(predictTheWinner([1, 5, 233, 7]))   # Expected: True


'''
Pattern
✅ Decision DP (Game Choices -> Minimax)
Identical to Stone Game but the verdict allows ties: player 1 wins when the
optimal score difference over the whole array is >= 0. The difference trick
makes the opponent's optimal play fall out of a single max() recurrence.
| Metric | Value   |
| ------ | ------- |
| Time   | O(n^2)  |
| Space  | O(n^2)  |
Better Possible?
✅ Yes
The 2-D diff table can be compressed to a single rolling 1-D array of length
n, giving O(n) space; time stays O(n^2) since every interval must be examined.
'''
