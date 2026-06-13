'''
433. Minimum Genetic Mutation (Medium)
Problem Statement

A gene string is 8 characters long, each from {'A','C','G','T'}. A single mutation
changes exactly one character. A mutated gene is valid only if it appears in the
given bank.

Given a start gene, an end gene, and a bank of valid gene strings, return the
minimum number of mutations to go from start to end, or -1 if impossible.

Input:
start = "AACCGGTT", end = "AAACGGTA",
bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]

Output:
2
'''

from collections import deque


def minMutation(start, end, bank):
    bank = set(bank)
    if end not in bank:          # end must be reachable & valid
        return -1

    choices = "ACGT"

    def neighbors(gene):
        for i in range(len(gene)):
            for c in choices:
                if c != gene[i]:
                    yield gene[:i] + c + gene[i + 1:]

    q = deque([(start, 0)])      # (gene, mutations)
    visited = {start}

    while q:
        gene, steps = q.popleft()
        if gene == end:
            return steps
        for nxt in neighbors(gene):
            if nxt in bank and nxt not in visited:
                visited.add(nxt)
                q.append((nxt, steps + 1))

    return -1


if __name__ == "__main__":
    print(minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))                              # Expected: 1
    print(minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]))      # Expected: 2


'''
Pattern
✅ State BFS
Each valid 8-char gene is a node; an edge joins two genes differing in one position
where the mutated gene is in the bank. BFS layers = mutation count, so the first time
we pop `end` we have the minimum number of mutations (unit-cost edges).

| Metric | Value                       |
| ------ | --------------------------- |
| Time   | O(B * L * 4)                |  B=bank size, L=8 length, 4 letters
| Space  | O(B)                        |  visited set + queue

Better Possible?
✅ Bidirectional BFS (expand from start and end alternately) cuts the explored set,
useful when the bank is large. Big-O is unchanged but practical work is reduced.
'''
