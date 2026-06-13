"""
649. Dota2 Senate (Medium)

Problem Statement:
Two parties, "Radiant" (R) and "Dire" (D), vote in rounds. The string `senate`
gives the initial party of each senator in order. In each round every remaining
senator may ban one senator from the opposing party (removing their right to
vote). Senators act in the given round-robin order and a banned senator is
skipped. The first party to be the only one with voting rights wins. Return the
name of the winning party: "Radiant" or "Dire".

Example:
    Input:  senate = "RD"
    Output: "Radiant"
    Input:  senate = "RDD"
    Output: "Dire"
"""

from collections import deque


def predict_party_victory(senate):
    n = len(senate)
    # Queues hold the ORIGINAL indices of each party's senators, in turn order.
    radiant = deque(i for i, c in enumerate(senate) if c == "R")
    dire = deque(i for i, c in enumerate(senate) if c == "D")

    # Each round: the senator with the smaller index acts first and bans the
    # opponent at the front. The actor survives and re-queues at index + n
    # (i.e. "next round", keeping relative order via the larger key).
    while radiant and dire:
        r = radiant.popleft()
        d = dire.popleft()
        if r < d:
            radiant.append(r + n)   # Radiant senator bans this Dire senator
        else:
            dire.append(d + n)      # Dire senator bans this Radiant senator

    return "Radiant" if radiant else "Dire"


if __name__ == "__main__":
    print(predict_party_victory("RD"))   # Expected: Radiant
    print(predict_party_victory("RDD"))  # Expected: Dire

"""
Pattern: Scheduling (round-robin re-queueing).
Technique: two queues of indices, one per party. Compare the front indices to
decide who votes first this round; the survivor is re-appended with index + n so
it naturally lines up after everyone in the current pass. This simulates endless
rounds without rebuilding the order each time.
Why: a FIFO queue preserves turn order, and adding n keeps the cyclic ordering
correct across rounds.

| Metric | Value |
|--------|-------|
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
Each ban removes one senator and costs O(1), so total work is O(n) — optimal.
Space is O(n) for the two queues.
"""
