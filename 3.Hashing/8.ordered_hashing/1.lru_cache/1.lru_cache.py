'''
1. LRU Cache (Medium)
Problem Statement

Design a Least Recently Used cache with capacity. Support:
- get(key):  return value if present (and mark it most-recently-used), else -1
- put(key, value): insert/update; if over capacity, evict the least-recently-used key
Both operations must be O(1) average.

Example
LRUCache(2); put(1,1); put(2,2); get(1)->1; put(3,3) evicts 2; get(2)->-1;
put(4,4) evicts 1; get(1)->-1; get(3)->3; get(4)->4
'''

from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity):
        self.cache = OrderedDict()      # ordered by recency: oldest first
        self.cap = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)     # mark most-recently-used
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)   # evict least-recently-used


if __name__ == "__main__":
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))      # Expected: 1
    lru.put(3, 3)          # evicts key 2
    print(lru.get(2))      # Expected: -1
    lru.put(4, 4)          # evicts key 1
    print(lru.get(1))      # Expected: -1
    print(lru.get(3))      # Expected: 3
    print(lru.get(4))      # Expected: 4

'''
Pattern
✅ Ordered Hashing (hashmap + recency order)

Key Observation
An OrderedDict gives O(1) lookup plus O(1) reordering: move_to_end marks recent use,
popitem(last=False) evicts the oldest. (Equivalent: dict + doubly linked list.)

| Metric | Value |
| ------ | ----- |
| get/put| O(1)  |
| Space  | O(capacity) |

Better Possible?
❌ O(1) is optimal.
'''
