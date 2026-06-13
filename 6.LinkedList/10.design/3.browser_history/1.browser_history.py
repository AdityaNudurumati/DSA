'''
1472. Design Browser History (Medium)
Problem Statement

You have a browser with one tab starting on a homepage. Design a structure that
supports:
- BrowserHistory(homepage)  the browser starts on homepage.
- visit(url)                visit url from the current page; this clears all
                            forward history.
- back(steps)               move back up to steps pages (stop at the oldest page);
                            return the current url.
- forward(steps)            move forward up to steps pages (stop at the newest page);
                            return the current url.

Example
Input:
BrowserHistory("homepage")  (then ignore homepage for the trace below)
visit("leetcode"); visit("google"); visit("fb");
back(1); back(1); forward(1); visit("yt"); forward(2); back(2)

Output:
back(1)    -> "google"
back(1)    -> "leetcode"
forward(1) -> "google"
visit("yt")                 (clears forward history beyond "google")
forward(2) -> "yt"          (clamped to newest page)
back(2)    -> "leetcode"
'''

# ----- Doubly linked list node: prev = previous page, next = forward page -----
class ListNode:
    def __init__(self, url="", prev=None, next=None):
        self.url = url
        self.prev, self.next = prev, next


class BrowserHistory:
    def __init__(self, homepage):
        self.cur = ListNode(homepage)        # current page pointer

    def visit(self, url):                    # new page after cur; drop forward chain
        node = ListNode(url, prev=self.cur)
        self.cur.next = node
        self.cur = node

    def back(self, steps):                   # walk prev links, stopping at oldest
        while steps > 0 and self.cur.prev:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.url

    def forward(self, steps):                # walk next links, stopping at newest
        while steps > 0 and self.cur.next:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.url


if __name__ == "__main__":
    bh = BrowserHistory("homepage")
    bh.visit("leetcode")
    bh.visit("google")
    bh.visit("fb")
    print(bh.back(1))      # Expected: google
    print(bh.back(1))      # Expected: leetcode
    print(bh.forward(1))   # Expected: google
    bh.visit("yt")         # clears forward history beyond "google"
    print(bh.forward(2))   # Expected: yt
    print(bh.back(2))      # Expected: leetcode


'''
Pattern
Doubly linked list with a single "current" pointer.
- visit  appends a node after cur and advances cur; because we overwrite cur.next,
         any old forward chain is dropped (no longer reachable) automatically.
- back / forward  just walk prev / next up to `steps` times, clamping at the ends.

| Metric | Value  |
| ------ | ------ |
| Time   | O(steps) per back/forward, O(1) per visit |
| Space  | O(n)   |  n = pages kept in history

Better Possible?
An array + index achieves O(1) random jumps but needs resizing/truncation; the DLL
is the cleaner pointer-based model. Either way back/forward are inherently O(steps).
'''
