'''
141. Linked List Cycle (Easy)
Problem Statement

Given the head of a linked list, determine if the list has a cycle in it.

A cycle exists if some node can be reached again by continuously following the
next pointer. Return True if there is a cycle, otherwise False.

Input:
head = [3,2,0,-4], pos = 1   (tail connects back to index 1)

Output:
True

Explanation:
The tail node (-4) points back to the node with value 2, forming a loop.
A list with pos = -1 (no connection) returns False.
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


def hasCycle(head):
    # Floyd's tortoise & hare: if fast laps slow, they collide inside the loop.
    # If fast reaches the end, the list is acyclic.
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


if __name__ == "__main__":
    print(hasCycle(build([3, 2, 0, -4], pos=1)))   # Expected: True
    print(hasCycle(build([1, 2], pos=-1)))         # Expected: False


'''
Pattern
✅ Fast-Slow Pointers (Floyd's cycle detection)
Two pointers at speeds 1 and 2. In a loop the gap closes by one each step, so they
must eventually meet; with no loop, fast simply runs off the end. Constant memory,
unlike a hash-set of visited nodes.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No
Detection needs at least one traversal; O(n) time, O(1) space is optimal.
'''
