'''
1. Design HashMap (Easy/Medium)
Problem Statement

Implement a hash map WITHOUT using any built-in hash table library. Support:
- put(key, value): insert or update
- get(key): return value, or -1 if absent
- remove(key): delete the mapping if present

Example
put(1,1); put(2,2); get(1)->1; get(3)->-1; put(2,1); get(2)->1; remove(2); get(2)->-1
'''

class MyHashMap:

    def __init__(self):
        self.size = 1009                      # a prime reduces clustering
        self.buckets = [[] for _ in range(self.size)]

    def _index(self, key):
        return key % self.size

    def put(self, key, value):
        bucket = self.buckets[self._index(key)]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)      # update existing
                return
        bucket.append((key, value))           # insert new

    def get(self, key):
        for k, v in self.buckets[self._index(key)]:
            if k == key:
                return v
        return -1

    def remove(self, key):
        bucket = self.buckets[self._index(key)]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return


if __name__ == "__main__":
    m = MyHashMap()
    m.put(1, 1)
    m.put(2, 2)
    print(m.get(1))     # Expected: 1
    print(m.get(3))     # Expected: -1
    m.put(2, 1)
    print(m.get(2))     # Expected: 1
    m.remove(2)
    print(m.get(2))     # Expected: -1

'''
Pattern
✅ Hash table by hand: bucket array + separate chaining

Key Observation
index = key % size selects a bucket; collisions live in a per-bucket list scanned
linearly. A prime table size spreads keys more evenly.

| Metric | Value |
| ------ | ----- |
| Ops    | O(1) average, O(n) worst (all collide) |
| Space  | O(size + entries) |

Better Possible?
Open addressing or resizing on load factor improves worst-case clustering.
'''
