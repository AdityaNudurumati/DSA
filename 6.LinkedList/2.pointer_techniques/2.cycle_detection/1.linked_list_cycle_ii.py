'''
142. Linked List Cycle II (Medium)
Problem Statement

Given the head of a linked list, return the node where the cycle begins.
If there is no cycle, return None.

Here we return the VALUE of the cycle-start node (or None) for easy printing.

Input:
head = [3,2,0,-4], pos = 1   (tail connects back to index 1)

Output:
2

Explanation:
The cycle starts at the node with value 2.
A list with pos = -1 (no cycle) returns None.
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next


def build(values, pos=-1):   # list -> linked list, tail.next -> node[pos] if pos>=0
    dummy = cur = ListNode()
    nodes = []
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
        nodes.append(cur)
    if pos >= 0 and nodes:
        cur.next = nodes[pos]    # create the cycle
    return dummy.next


def to_list(head):           # linked list -> list (safe only for acyclic lists)
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def detectCycle(head):
    # Phase 1: Floyd's meeting point.
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break
    else:
        return None              # fast hit the end -> no cycle
    if not (fast and fast.next):
        return None              # loop exited without meeting -> no cycle
    # Phase 2: distance from head to start == distance from meeting point to start.
    # Walk one pointer from head and one from the meeting point at equal speed.
    p = head
    while p is not slow:
        p = p.next
        slow = slow.next
    return p


if __name__ == "__main__":
    node = detectCycle(build([3, 2, 0, -4], pos=1))
    print(node.val if node else None)              # Expected: 2
    node = detectCycle(build([1, 2], pos=-1))
    print(node.val if node else None)              # Expected: None


'''
Pattern
✅ Fast-Slow Pointers (Floyd's cycle detection, phase two)
After the hare and tortoise meet inside the loop, the distance from the head to the
loop start equals the distance from the meeting point to the loop start. Advancing
two pointers at speed 1 from head and from the meeting point converges on the start.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No
A hash-set of visited nodes also finds the start but costs O(n) space; Floyd's keeps
it O(1). O(n) time is unavoidable.
'''
