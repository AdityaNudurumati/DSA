'''
138. Copy List with Random Pointer (Hard)
Problem Statement

A linked list of length n is given where each node contains an additional
random pointer, which could point to any node in the list, or None.

Construct a DEEP COPY of the list. The copy should consist of exactly n brand
new nodes, where each new node's value is set to the value of its original node.
Both the next and random pointers of the new nodes should point to new nodes in
the copied list such that the pointers in the original and copied list represent
the same list state. None of the pointers in the new list should point to nodes
in the original list.

The list is represented as [[val, random_index], ...] where random_index is the
index of the node that random points to (or None).

Input:
[[7,None],[13,0],[11,4],[10,2],[1,0]]

Output:
[[7,None],[13,0],[11,4],[10,2],[1,0]]

Explanation:
The deep copy has identical structure: node values and the relative random
targets (by index) match the original exactly.
'''

# Node carries an EXTRA pointer (random) beyond next.
class ListNode:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


def build(pairs):
    # pairs: list of [val, random_index_or_None]; returns head with random wired.
    nodes = [ListNode(val) for val, _ in pairs]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    for i, (_, rnd) in enumerate(pairs):
        nodes[i].random = nodes[rnd] if rnd is not None else None
    return nodes[0] if nodes else None


def to_pairs(head):
    # Convert to [[val, random_index_or_None], ...] for verification.
    index = {}
    nodes = []
    cur = head
    while cur:
        index[cur] = len(nodes)
        nodes.append(cur)
        cur = cur.next
    out = []
    for node in nodes:
        out.append([node.val, index[node.random] if node.random else None])
    return out


def copyRandomList(head):
    if not head:
        return None

    # 1) Clone each node right after its original: A -> A' -> B -> B' -> ...
    cur = head
    while cur:
        clone = ListNode(cur.val, cur.next)
        cur.next = clone
        cur = clone.next

    # 2) Wire clones' random using interleaving: A'.random = A.random.next
    cur = head
    while cur:
        if cur.random:
            cur.next.random = cur.random.next
        cur = cur.next.next

    # 3) Unweave the two interleaved lists, restoring the original.
    cur = head
    copy_head = head.next
    while cur:
        clone = cur.next
        cur.next = clone.next
        clone.next = clone.next.next if clone.next else None
        cur = cur.next
    return copy_head


if __name__ == "__main__":
    original = build([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
    copied = copyRandomList(original)
    print(to_pairs(copied))  # Expected: [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]


'''
Pattern
✅ Advanced Pointer Manipulation — interleaved clone (O(1) extra space)

Technique & why:
Insert each clone directly after its original so the clone is reachable as
cur.next. The clone's random is then exactly cur.random.next (the clone of the
node the original pointed to). Finally split the woven list back into original
and copy. This avoids the hashmap old->new that the naive approach uses.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No. We must create n new nodes and visit each a constant number of times, so
O(n) time is optimal. The interleave trick already removes the O(n) hashmap, so
O(1) auxiliary space is optimal too (output not counted).
'''
