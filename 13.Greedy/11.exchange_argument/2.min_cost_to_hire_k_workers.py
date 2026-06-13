'''
2. Minimum Cost to Hire K Workers (Hard) (LC857)
Problem Statement

There are n workers. The i-th worker has quality[i] and a minimum wage
expectation wage[i]. You want to hire EXACTLY k workers forming a "paid group"
under two rules:

  1. Every worker in the group is paid in proportion to their quality relative
     to the others in the group (same pay-per-quality rate for everyone).
  2. Every worker is paid at least their minimum wage expectation.

Return the least amount of money needed to form such a group.

Example
Input:
quality = [10, 20, 5]
wage    = [70, 50, 30]
k = 2

Output:
105.00000
Explanation:
Hire workers 0 and 2. Worker 0 sets the rate (wage/quality = 7). Pay worker 2
at rate 7 -> 5 * 7 = 35, worker 0 -> 10 * 7 = 70. Total = 105.00000
'''

import heapq


def mincost_to_hire_workers(quality, wage, k):
    # Each worker imposes a minimum pay-rate ratio = wage/quality.
    # If a worker is in the group, the group's rate must be >= that worker's ratio,
    # so the group's rate = the MAX ratio among chosen workers.
    # Total cost = rate * (sum of qualities in group).
    #
    # Greedy rule: sort workers by ratio ascending. Process each as the "rate setter"
    # (the highest-ratio member). Among workers seen so far (all with ratio <= current),
    # keep the k with the SMALLEST qualities via a max-heap, minimizing sum*rate.
    workers = sorted(zip(wage, quality), key=lambda wq: wq[0] / wq[1])

    max_quality_heap = []   # store negatives -> Python max-heap of qualities
    quality_sum = 0
    best = float("inf")

    for w, q in workers:
        rate = w / q                       # this worker sets the group's pay rate
        heapq.heappush(max_quality_heap, -q)
        quality_sum += q

        if len(max_quality_heap) > k:      # drop the largest quality to shrink the sum
            quality_sum += heapq.heappop(max_quality_heap)  # popped is negative -> subtracts

        if len(max_quality_heap) == k:     # a full group whose rate is `rate`
            best = min(best, quality_sum * rate)

    return best


if __name__ == "__main__":
    print(f"{mincost_to_hire_workers([10, 20, 5], [70, 50, 30], 2):.5f}")        # Expected: 105.00000
    print(f"{mincost_to_hire_workers([3, 1, 10, 10, 1], [4, 8, 2, 2, 7], 3):.5f}")  # Expected: 30.66667


'''
Pattern
Exchange Argument Greedy (ratio sort + min-quality max-heap)

Greedy rule & why it's safe
The group's pay rate is forced to be the maximum wage/quality ratio among its members.
So fix each worker as the rate-setter (highest ratio). All cheaper-ratio workers are
eligible to join under that rate. Cost = rate * sum(qualities), and rate is fixed once
the setter is chosen, so we minimize the quality sum by keeping the k smallest qualities
among the eligible set -- exactly what a size-k max-heap maintains.
Exchange argument: if an optimal group's rate-setter is fixed, swapping any included
higher-quality worker for an excluded lower-quality eligible worker reduces the quality
sum (hence the cost) without raising the rate, so the k-smallest-qualities choice is
optimal. Iterating the setter over all workers in ratio order covers every candidate rate.

| Metric | Value      |
| ------ | ---------- |
| Time   | O(n log n) |  (sort + n heap ops of O(log k))
| Space  | O(k)       |  (heap of at most k qualities)

Better Possible?
No. The ratio sort is the crux and is O(n log n); the heap maintenance is O(n log k),
both dominated by the sort. This is the standard optimal solution for LC857.
'''
