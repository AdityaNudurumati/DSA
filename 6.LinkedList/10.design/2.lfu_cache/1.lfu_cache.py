'''
460. LFU Cache (Hard)
Problem Statement

Design a data structure that follows the Least Frequently Used (LFU) cache policy.

Implement the LFUCache class:
- LFUCache(capacity)  initialize the cache with a positive size capacity.
- get(key)            return the value if present (and bump its use count), else -1.
- put(key, value)     update/insert. When over capacity, evict the least frequently
                      used key; if there is a tie in frequency, evict the least
                      recently used among them.

Both get and put must run in O(1) average time.

Example
Input:
cap = 2
put(1,1); put(2,2); get(1); put(3,3); get(2); get(3); put(4,4); get(1); get(3); get(4)

Output:
get(1) -> 1               (freq: 1->2, 2->1)
put(3,3) evicts key 2     (key 2 had lowest freq 1)
get(2) -> -1
get(3) -> 3               (freq: 1->2, 3->2)
put(4,4) evicts key 1     (1 and 3 both freq 2; 1 is LRU)
get(1) -> -1
get(3) -> 3
get(4) -> 4
'''

# ----- Node of a per-frequency doubly linked list -----
class ListNode:
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.freq = 1
        self.prev = self.next = None


# ----- A doubly linked list (with head/tail sentinels) holding all nodes of one frequency -----
class DLL:
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_front(self, node):            # most-recent end is just after head
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def pop_lru(self):                    # least-recent of this bucket = tail.prev
        node = self.tail.prev
        self.remove(node)
        return node


class LFUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}                   # key -> node
        self.freqs = {}                   # freq -> DLL of nodes with that freq
        self.min_freq = 0

    def _bump(self, node):                # move node from its bucket to freq+1 bucket
        f = node.freq
        self.freqs[f].remove(node)
        if self.freqs[f].size == 0:
            del self.freqs[f]
            if self.min_freq == f:        # bucket emptied -> min shifts up by one
                self.min_freq += 1
        node.freq += 1
        self.freqs.setdefault(node.freq, DLL()).add_front(node)

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._bump(node)
        return node.val

    def put(self, key, value):
        if self.cap <= 0:
            return
        if key in self.cache:             # update value + bump frequency
            node = self.cache[key]
            node.val = value
            self._bump(node)
            return
        if len(self.cache) >= self.cap:   # evict LFU (tie -> LRU within min_freq bucket)
            lru = self.freqs[self.min_freq].pop_lru()
            if self.freqs[self.min_freq].size == 0:
                del self.freqs[self.min_freq]
            del self.cache[lru.key]
        node = ListNode(key, value)       # new nodes start at freq 1
        self.cache[key] = node
        self.freqs.setdefault(1, DLL()).add_front(node)
        self.min_freq = 1


if __name__ == "__main__":
    lfu = LFUCache(2)
    lfu.put(1, 1)
    lfu.put(2, 2)
    print(lfu.get(1))   # Expected: 1
    lfu.put(3, 3)       # evicts key 2 (lowest freq)
    print(lfu.get(2))   # Expected: -1
    print(lfu.get(3))   # Expected: 3
    lfu.put(4, 4)       # 1 and 3 tie at freq 2 -> evict LRU (key 1)
    print(lfu.get(1))   # Expected: -1
    print(lfu.get(3))   # Expected: 3
    print(lfu.get(4))   # Expected: 4


'''
Pattern
HashMap + frequency buckets of Doubly Linked Lists.
- cache:  key -> node (O(1) lookup)
- freqs:  freq -> DLL of all nodes at that frequency, ordered by recency
- min_freq tracks the smallest live frequency so eviction is O(1).
On access, a node hops from its freq bucket to the freq+1 bucket (front = most recent).
Eviction pops the tail (LRU) of the min_freq bucket, breaking frequency ties by recency.

| Metric | Value  |
| ------ | ------ |
| Time   | O(1)   |  per get / put
| Space  | O(cap) |

Better Possible?
No. O(1) is optimal; the only trick that makes it O(1) (rather than scanning for the
minimum frequency) is the min_freq pointer plus per-frequency DLLs.
'''
