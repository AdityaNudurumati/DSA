'''
1. Job Sequencing Problem (Medium)
Problem Statement

You are given a list of jobs, each as (id, deadline, profit). Every job takes
exactly 1 unit of time and must finish on or before its deadline. The machine
runs one job per unit of time. Schedule a subset of jobs to maximize total
profit, and return (count_of_jobs_done, total_profit).

Example
Input:
jobs = [(1,4,20),(2,1,10),(3,1,40),(4,1,30)]

Output:
(2, 60)
Explanation:
Pick job 3 (profit 40) in slot 1 and job 1 (profit 20) in slot 4 -> 2 jobs, 60.
'''

def job_sequencing(jobs):
    # Greedy rule: process jobs in DESCENDING profit order. For each job, place it
    # in the LATEST still-free time slot at or before its deadline.
    #
    # Why it's safe: a job occupies exactly one slot. Considering the most
    # profitable job first guarantees we never skip a high-profit job for a lower
    # one. Choosing the latest free slot (instead of the earliest) keeps earlier
    # slots open for jobs with tighter deadlines, so it never blocks a feasible
    # future placement (exchange argument: any feasible schedule can be rearranged
    # to this latest-slot form without losing profit).

    jobs_sorted = sorted(jobs, key=lambda j: -j[2])   # by profit, desc
    max_deadline = max((d for _, d, _ in jobs_sorted), default=0)

    slot = [False] * (max_deadline + 1)               # slot[t] free? (1-indexed)
    count = 0
    total = 0

    for _id, deadline, profit in jobs_sorted:
        t = min(deadline, max_deadline)               # latest usable slot
        while t > 0 and slot[t]:                       # walk back to a free slot
            t -= 1
        if t > 0:
            slot[t] = True
            count += 1
            total += profit

    return (count, total)


if __name__ == "__main__":
    print(job_sequencing([(1, 4, 20), (2, 1, 10), (3, 1, 40), (4, 1, 30)]))            # Expected: (2, 60)
    print(job_sequencing([(1, 2, 100), (2, 1, 19), (3, 2, 27), (4, 1, 25), (5, 1, 15)]))  # Expected: (2, 127)


'''
Pattern
✅ Scheduling Greedy (sort by profit desc, fill the latest free slot before the deadline)

Key Observation
Each job needs one slot. Take the richest jobs first; for each, grab the latest
open slot it can still meet. Using the latest slot preserves earlier slots for
tighter-deadline jobs, so the greedy choice is never worse than any alternative.

| Metric | Value         |
| ------ | ------------- |
| Time   | O(n log n + n * D) |
| Space  | O(D)          | (D = max deadline)

Better Possible?
✅ The inner slot search can be sped up to near O(n log n) overall by using a
Disjoint Set Union (union-find) that maps each deadline to its latest free slot
in nearly O(1) amortized time. The profit-sort lower bound of O(n log n) remains.
'''
