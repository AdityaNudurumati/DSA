'''
1. Reservoir Sampling (Medium)   [LC382 / LC398]
Problem Statement

Given a STREAM of items of UNKNOWN length (you can't store it all), pick k items
uniformly at random so that every item seen has an equal k/N chance of being in
the final sample. Uses O(k) space and one pass.

Algorithm (Algorithm R):
  - Put the first k items into the reservoir.
  - For the i-th item (i >= k), pick a random j in [0, i]. If j < k, replace
    reservoir[j] with the new item.
This guarantees each of the N items ends up selected with probability k/N.

Why it matters for AI/ML: this is exactly how you sample a fixed-size subset from
a data stream too large for memory (shuffling buffers, streaming datasets,
train/replay buffers).

Example
Input:
stream = [1..1000], k = 3   ->  3 items, each equally likely.
'''

import random

def reservoir_sample(stream, k):

    reservoir = []

    for i, item in enumerate(stream):
        if i < k:
            reservoir.append(item)          # fill the reservoir first
        else:
            j = random.randint(0, i)        # 0..i inclusive
            if j < k:
                reservoir[j] = item          # replace with prob k/(i+1)

    return reservoir


def sample_one(stream):
    # single-sample version (k = 1): the classic "random node" problem
    chosen = None
    for i, item in enumerate(stream):
        if random.randint(0, i) == 0:        # prob 1/(i+1)
            chosen = item
    return chosen


if __name__ == "__main__":
    random.seed(42)

    # Statistical check: over many trials, each element should appear ~uniformly.
    N, k, trials = 5, 2, 60000
    counts = [0] * N
    for _ in range(trials):
        for x in reservoir_sample(list(range(N)), k):
            counts[x] += 1
    freq = [round(c / trials, 3) for c in counts]
    print("k=2 of 5, selection freq per element:", freq)
    print("expected ~", round(k / N, 3), "each")   # ~0.4 each

    # single-sample uniformity
    counts = [0] * N
    for _ in range(trials):
        counts[sample_one(list(range(N)))] += 1
    print("single-sample freq:", [round(c / trials, 3) for c in counts])  # ~0.2

'''
Pattern
✅ Reservoir Sampling (uniform sample from an unknown-length stream)

Key Observation
The i-th item enters the reservoir with probability k/(i+1); a clean induction
shows every item ends with probability k/N despite never knowing N in advance.
One pass, O(k) memory.

| Metric | Value |
| ------ | ----- |
| Time   | O(N)  |
| Space  | O(k)  |

Better Possible?
❌ No. You must read every streamed item once; O(N) time, O(k) space is optimal.
'''
