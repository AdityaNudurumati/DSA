'''
1. Browser History (Medium)
Problem Statement

Design a browser history starting on a given homepage. Support:
- visit(url):  go to url from the current page; this clears all forward history
- back(steps): move back up to `steps` pages (stop at the oldest page); return
               the current url
- forward(steps): move forward up to `steps` pages (stop at the newest page);
               return the current url

Example
Input:
start "leetcode"; visit "google"; visit "fb"; back 1; back 1; forward 1;
visit "yt"; forward 2; back 2

Output:
back 1    -> "google"
back 1    -> "leetcode"
forward 1 -> "google"
forward 2 -> "yt"
back 2    -> "leetcode"
'''


class BrowserHistory:

    def __init__(self, homepage):
        self._hist = [homepage]            # array of visited pages
        self._cur = 0                      # index of the current page

    def visit(self, url):
        # Truncate any forward history, then append the new page and move to it.
        del self._hist[self._cur + 1:]     # clears forward entries
        self._hist.append(url)
        self._cur += 1

    def back(self, steps):
        # Move left but not past index 0.
        self._cur = max(0, self._cur - steps)
        return self._hist[self._cur]

    def forward(self, steps):
        # Move right but not past the last index.
        self._cur = min(len(self._hist) - 1, self._cur + steps)
        return self._hist[self._cur]


if __name__ == "__main__":
    b = BrowserHistory("leetcode")
    b.visit("google")
    b.visit("fb")
    print(b.back(1))        # Expected: google
    print(b.back(1))        # Expected: leetcode
    print(b.forward(1))     # Expected: google
    b.visit("yt")
    print(b.forward(2))     # Expected: yt
    print(b.back(2))        # Expected: leetcode

'''
Pattern
✅ Design — Array + pointer (a two-stack back/forward model)

Key Observation
History is naturally a stack of pages with a cursor: visiting clears the forward
stack (truncate everything after the cursor), while back/forward just slide the
cursor and clamp it to the valid range. An array with an index captures both the
back-stack (left of cursor) and forward-stack (right of cursor) in one structure.

| Metric | Value                                   |
| ------ | --------------------------------------- |
| Time   | visit amortized O(1); back/forward O(1) |
| Space  | O(n)                                    |

Better Possible?
❌ No — every operation is already O(1) (visit amortized); storage is inherent.
'''
