'''
Josephus Problem (Medium)
Problem Statement

There are n people standing in a circle, numbered 1 to n. Starting from person
1, we count k people around the circle and eliminate the k-th person. Counting
then resumes from the next living person and again the k-th is eliminated. This
continues until only one person remains. Return the 1-indexed position of that
survivor.

Example:
Input:  n = 7, k = 3
Output: 4
Explanation:
Eliminated in order: 3, 6, 2, 7, 5, 1 -> survivor is 4.

Input:  n = 5, k = 2
Output: 3
Explanation:
Eliminated in order: 2, 4, 1, 5 -> survivor is 3.
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next


def build_circular(values):
    # Build a circular singly linked list; tail.next loops back to head.
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    curr.next = head  # close the ring
    return head


def josephus(n, k):
    # Model the n people as a circular list of positions 1..n.
    head = build_circular(list(range(1, n + 1)))
    if n == 1:
        return head.val

    # 'prev' trails 'curr' so we can splice the eliminated node out in O(1).
    prev = head
    while prev.next is not head:   # find the node before head (the tail)
        prev = prev.next
    curr = head

    # Each round: advance k-1 steps, then remove curr (the k-th person).
    while curr.next is not curr:   # stop when only one node points to itself
        for _ in range(k - 1):
            prev = curr
            curr = curr.next
        prev.next = curr.next      # eliminate curr
        curr = prev.next           # counting resumes from the next person

    return curr.val


if __name__ == "__main__":
    print(josephus(7, 3))   # Expected: 4
    print(josephus(5, 2))   # Expected: 3
    print(josephus(1, 1))   # Expected: 1


'''
Pattern
Circular Linked List simulation

Technique & why:
The eliminations happen around a ring, so a circular linked list models the
process directly. We keep a trailing 'prev' pointer so that removing the k-th
person is an O(1) splice (prev.next = curr.next). Each elimination advances
exactly k-1 steps, then unlinks, and counting continues from the next live node.
This faithfully simulates the game and naturally terminates when a node points
to itself.

| Metric | Value   |
| ------ | ------- |
| Time   | O(n*k)  |
| Space  | O(n)    |

Better Possible?
Yes. The classic recurrence josephus(n, k) = (josephus(n-1, k) + k) % n, with
the base case josephus(1, k) = 0, gives the 0-indexed survivor in O(n) time and
O(1) space (add 1 for the 1-indexed answer). The linked-list version is shown
here because it makes the circular elimination explicit and matches this folder.
'''
