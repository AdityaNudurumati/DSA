'''
146. LRU Cache (Medium)
Problem Statement

Design a data structure that follows the Least Recently Used (LRU) cache policy.

Implement the LRUCache class:
- LRUCache(capacity)  initialize the cache with a positive size capacity.
- get(key)            return the value of the key if it exists, else return -1.
- put(key, value)     update the value if key exists; otherwise insert it.
                      If inserting exceeds capacity, evict the least recently used key.

Both get and put must run in O(1) average time.

Example
Input:
cap = 2
put(1,1); put(2,2); get(1); put(3,3); get(2); put(4,4); get(1); get(3); get(4)

Output:
get(1) -> 1
put(3,3) evicts key 2
get(2) -> -1
put(4,4) evicts key 1
get(1) -> -1
get(3) -> 3
get(4) -> 4
'''

# ----- Doubly linked list node (carries key so we can delete from the map on evict) -----
class ListNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key, self.val = key, val
        self.prev, self.next = prev, next


class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}                       # key -> node
        # head/tail sentinels: most-recent sits next to head, least-recent next to tail
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):                  # unlink a node from the list
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_front(self, node):               # insert right after head (most recent)
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)                    # touch -> move to front
        self._add_front(node)
        return node.val

    def put(self, key, value):
        if key in self.cache:                 # update existing + refresh recency
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add_front(node)
            return
        if len(self.cache) >= self.cap:       # evict least-recently-used (tail.prev)
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
        node = ListNode(key, value)
        self.cache[key] = node
        self._add_front(node)


if __name__ == "__main__":
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))   # Expected: 1
    lru.put(3, 3)       # evicts key 2
    print(lru.get(2))   # Expected: -1
    lru.put(4, 4)       # evicts key 1
    print(lru.get(1))   # Expected: -1
    print(lru.get(3))   # Expected: 3
    print(lru.get(4))   # Expected: 4


'''
Pattern
HashMap + Doubly Linked List.
The hashmap gives O(1) lookup of a node; the DLL gives O(1) reorder/eviction.
We keep head/tail sentinels so add/remove never special-case the empty/end cases.
On any access (get or put) the node moves to the front; eviction always pops tail.prev.

| Metric | Value  |
| ------ | ------ |
| Time   | O(1)   |  per get / put (amortized)
| Space  | O(cap) |

Better Possible?
No on time complexity (already O(1)). Code-wise, collections.OrderedDict
(move_to_end / popitem) hides the DLL, but the hand-built list is the
interview-expected answer and shows the mechanics.
'''
