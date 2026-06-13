'''
1. Consistent Hashing (Advanced — concept demo)
Problem Statement

Consistent hashing maps both NODES and KEYS onto a circular hash space (a "ring").
A key is served by the first node clockwise from its hash. Adding/removing a node
only remaps the keys between it and its neighbor (≈ K/N keys), instead of nearly all
keys as plain `key % N` would. Virtual nodes (several ring positions per physical
node) smooth out the load.

This is the backbone of distributed caches / sharded databases (Memcached, Cassandra,
Dynamo).

Example
3 nodes A/B/C on the ring -> each key deterministically maps to one node; removing a
node reassigns only that node's keys.
'''

import bisect
import hashlib

class ConsistentHashRing:

    def __init__(self, nodes=None, vnodes=100):
        self.vnodes = vnodes          # virtual nodes per physical node (real systems use ~100+)
        self.ring = {}                # ring position (hash) -> physical node
        self.sorted_positions = []    # sorted ring positions for binary search
        for node in (nodes or []):
            self.add_node(node)

    def _hash(self, key):
        # md5 is deterministic across processes (Python's hash() is randomized for str)
        # and uniform regardless of input length, so node ids and data keys share one range
        digest = hashlib.md5(str(key).encode()).hexdigest()
        return int(digest, 16) % (2 ** 32)

    def add_node(self, node):
        for i in range(self.vnodes):
            pos = self._hash(f"{node}#{i}")
            self.ring[pos] = node
            bisect.insort(self.sorted_positions, pos)

    def remove_node(self, node):
        for i in range(self.vnodes):
            pos = self._hash(f"{node}#{i}")
            self.ring.pop(pos, None)
            self.sorted_positions.remove(pos)

    def get_node(self, key):
        if not self.ring:
            return None
        pos = self._hash(key)
        # first node clockwise (wrap around the ring)
        idx = bisect.bisect(self.sorted_positions, pos) % len(self.sorted_positions)
        return self.ring[self.sorted_positions[idx]]


if __name__ == "__main__":
    ring = ConsistentHashRing(["A", "B", "C"])
    keys = ["apple", "banana", "cherry", "date", "elderberry"]

    before = {k: ring.get_node(k) for k in keys}
    print(before)                      # each key -> some node (deterministic)

    ring.remove_node("B")
    after = {k: ring.get_node(k) for k in keys}

    moved = [k for k in keys if before[k] != after[k]]
    # only keys previously on B should move; A/C keys stay put
    print("moved after removing B:", moved)
    print("all moved keys were on B:", all(before[k] == "B" for k in moved))  # Expected: True

'''
Pattern
✅ Custom Hashing — hash ring + virtual nodes (binary search on sorted positions)

Key Observation
Hashing nodes AND keys onto the same ring means a topology change only disturbs the
arc owned by the changed node. Virtual nodes balance load and shrink variance.

| Metric | Value      |
| ------ | ---------- |
| Lookup | O(log V)   | (V = total virtual nodes)
| Add/Remove node | O(V log V) |

Better Possible?
This is the standard approach; bounded-load variants refine balance further.
'''
