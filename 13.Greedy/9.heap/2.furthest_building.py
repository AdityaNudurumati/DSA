'''
1642. Furthest Building You Can Reach (Medium)
Problem Statement

You are given an integer array heights of building heights, plus bricks and
ladders. You start at building 0 and move to adjacent buildings.

Moving from building i to i+1:
  - if heights[i+1] <= heights[i], no resource is needed.
  - if heights[i+1] >  heights[i], the climb is (heights[i+1] - heights[i]).
    You may cover that climb either with one ladder (any size) or with that many
    bricks.

Return the furthest building index (0-based) you can reach using the resources
optimally.

Input:
heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1

Output:
4

Explanation:
0->1 down (free). 1->2 climb 5 (use bricks, 5 left -> 0). 2->3 down (free).
3->4 climb 3 (use the ladder). Reach index 4. The next climb 4->5 is 5 and we
have neither bricks nor ladders left, so 4 is the furthest.
'''

import heapq


def furthestBuilding(heights, bricks, ladders):
    # Greedy rule: ladders are most valuable on the BIGGEST climbs. Tentatively
    # use a ladder on every climb; keep the climbs that consumed a ladder in a
    # min-heap. Once we exceed `ladders` ladders, the smallest such climb is
    # demoted to bricks (pop the heap min). If bricks ever go negative, stop.
    #
    # Why it's safe: among any set of climbs we must cover, assigning the ladders
    # to the largest climbs and bricks to the rest minimizes brick usage. The
    # min-heap lets us always reclaim the cheapest ladder-covered climb to pay
    # with bricks instead, which is exactly the optimal swap (exchange argument:
    # swapping a ladder off a large climb onto a smaller one never saves bricks).

    used_ladders = []  # min-heap of climb sizes currently covered by ladders

    for i in range(len(heights) - 1):
        diff = heights[i + 1] - heights[i]
        if diff <= 0:
            continue  # going down or flat is free

        heapq.heappush(used_ladders, diff)  # tentatively use a ladder
        if len(used_ladders) > ladders:
            # too many ladders in play -> demote the smallest climb to bricks
            bricks -= heapq.heappop(used_ladders)
            if bricks < 0:
                return i  # can't afford this step -> furthest reachable is i

    return len(heights) - 1  # reached the last building


if __name__ == "__main__":
    print(furthestBuilding([4, 2, 7, 6, 9, 14, 12], 5, 1))          # Expected: 4
    print(furthestBuilding([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2))  # Expected: 7


'''
Pattern
Greedy + Heap
Greedy rule: reserve ladders for the largest climbs; cover the remaining (smaller)
climbs with bricks. A min-heap of ladder-covered climbs lets us cheaply demote the
smallest one to bricks whenever a bigger climb arrives.
Why safe: for any fixed prefix of climbs we must pay for, putting ladders on the
largest climbs minimizes total bricks spent. The heap performs the optimal swap on
the fly; exchange argument shows no alternate assignment uses fewer bricks.

| Metric | Value          |
| ------ | -------------- |
| Time   | O(n log L)     |
| Space  | O(L)           |
(L = number of ladders)

Better Possible?
Not asymptotically for this online greedy. Each climb does at most one push and one
pop on a heap bounded by L, giving O(n log L), which is effectively optimal here.
'''
