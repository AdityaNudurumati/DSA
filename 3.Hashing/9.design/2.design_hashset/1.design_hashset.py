'''
1. Design HashSet (Easy)
Problem Statement

Implement a hash set WITHOUT using any built-in hash table library. Support:
- add(key)
- remove(key)
- contains(key) -> bool

Example
add(1); add(2); contains(1)->True; contains(3)->False; add(2); contains(2)->True;
remove(2); contains(2)->False
'''

class MyHashSet:

    def __init__(self):
        self.size = 1009
        self.buckets = [[] for _ in range(self.size)]

    def _index(self, key):
        return key % self.size

    def add(self, key):
        bucket = self.buckets[self._index(key)]
        if key not in bucket:
            bucket.append(key)

    def remove(self, key):
        bucket = self.buckets[self._index(key)]
        if key in bucket:
            bucket.remove(key)

    def contains(self, key):
        return key in self.buckets[self._index(key)]


if __name__ == "__main__":
    s = MyHashSet()
    s.add(1)
    s.add(2)
    print(s.contains(1))    # Expected: True
    print(s.contains(3))    # Expected: False
    s.add(2)
    print(s.contains(2))    # Expected: True
    s.remove(2)
    print(s.contains(2))    # Expected: False

'''
Pattern
✅ Hash table by hand (membership only): bucket array + chaining

| Metric | Value |
| ------ | ----- |
| Ops    | O(1) average |
| Space  | O(size + entries) |

Better Possible?
Same trade-offs as Design HashMap (open addressing / resizing).
'''
