'''
269. Alien Dictionary (Hard)
Problem Statement

A list of words is sorted lexicographically by the rules of an unknown alien
language. Derive an ordering of the language's letters consistent with the
word list.

Return any valid ordering as a string. If no valid order exists (a cycle, or
an invalid prefix such as ["abc","ab"]), return "".

Input:
words = ["wrt", "wrf", "er", "ett", "rftt"]

Output:
"wertf"

Explanation:
Comparing adjacent words yields edges t->f, w->e, r->t, e->r, giving the order
w, e, r, t, f.
'''

from collections import deque


def alien_order(words):
    # Collect every distinct character as a node.
    adj = {c: set() for w in words for c in w}
    indeg = {c: 0 for c in adj}

    # Derive an edge from the first differing character of adjacent words.
    for first, second in zip(words, words[1:]):
        for a, b in zip(first, second):
            if a != b:
                if b not in adj[a]:
                    adj[a].add(b)
                    indeg[b] += 1
                break
        else:
            # No differing char: invalid if the longer word precedes its prefix.
            if len(first) > len(second):
                return ""

    # Kahn's algorithm over the characters.
    q = deque(sorted(c for c in indeg if indeg[c] == 0))
    order = []
    while q:
        c = q.popleft()
        order.append(c)
        for nxt in sorted(adj[c]):
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q.append(nxt)

    # If not all chars are placed a cycle exists.
    return "".join(order) if len(order) == len(indeg) else ""


if __name__ == "__main__":
    print(alien_order(["wrt", "wrf", "er", "ett", "rftt"]))  # Expected: wertf
    print(alien_order(["z", "x"]))                            # Expected: zx
    print(alien_order(["z", "x", "z"]))                       # Expected:


'''
Pattern
✅ Topological Sort (Kahn's BFS) over a derived dependency graph
The real work is graph construction: each pair of adjacent words contributes
one ordering constraint (edge) from its first differing letter. A valid
alphabet is then any topological order; a remaining cycle means no order
exists. The invalid-prefix case (["abc","ab"]) is handled explicitly.

| Metric | Value          |
| ------ | -------------- |
| Time   | O(C)           |
| Space  | O(1) (<=26 letters, so O(U + edges)) |

C = total characters across all words. Sorting the small alphabet adds only a
constant factor.

Better Possible?
❌ No. Every character must be read to build constraints, so O(C) is optimal.
'''
