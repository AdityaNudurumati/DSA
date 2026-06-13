# Trees

Pattern-based roadmap for **binary trees, BSTs, and advanced tree structures**. Each numbered
folder is one pattern with a `notes.txt` (sub-pattern tree, template, problems checklist). When
built out, a pattern is split into sub-folders — same structure as [../1.Arrays](../1.Arrays/) … [../6.LinkedList](../6.LinkedList/).

> Every file defines its own minimal `TreeNode` + `build(level_order_list)` helper so it's
> self-contained and runnable. Two recursion shapes solve most problems: **top-down**
> (`dfs(node, info_from_parent)`) and **bottom-up** (combine children's returns).
>
> Overlap: BFS tree traversals (Level Order, Zigzag, Right Side View) live in
> [../5.Queue/2.bfs/1.tree_bfs](../5.Queue/2.bfs/1.tree_bfs/); Trie / Word Search II in
> [../2.Strings/7.trie](../2.Strings/7.trie/) and [../1.Arrays/11.advanced/7.trie](../1.Arrays/11.advanced/7.trie/). Those are **cross-referenced**.

## Patterns

Built **self-contained** — every file defines its own `TreeNode` + level-order `build()` helper.

| #  | Pattern | Folder | Status |
|----|---------|--------|--------|
| 1  | Traversal Patterns | [1.traversal](1.traversal/) | 4 problems (pre/in/post-order, vertical) |
| 2  | Recursive Patterns | [2.recursive](2.recursive/) | 3 problems (paths, same tree, symmetric) |
| 3  | Path-Based Problems | [3.path](3.path/) | 5 problems (path sum I/II/III, root-to-leaf, max path) |
| 4  | Height / Depth / Diameter | [4.height_depth](4.height_depth/) | 4 problems (max/min depth, diameter, balanced) |
| 5  | Binary Search Tree | [5.bst](5.bst/) | 5 problems (search, insert, delete, validate, kth) |
| 6  | Tree Construction | [6.construction](6.construction/) | 3 problems (pre+in, in+post, sorted→BST) |
| 7  | Lowest Common Ancestor | [7.lca](7.lca/) | 2 problems (binary tree, BST) |
| 8  | Tree Modification | [8.modification](8.modification/) | 4 problems (invert, flatten, merge, prune) |
| 9  | Tree Views | [9.views](9.views/) | 4 problems (left, top, bottom, boundary) |
| 10 | Ancestor / Descendant | [10.ancestor](10.ancestor/) | 2 problems (distance K, kth ancestor) |
| 11 | Tree DP | [11.tree_dp](11.tree_dp/) | 2 problems (House Robber III, Cameras) |
| 12 | Traversal w/o Recursion | [12.iterative_traversal](12.iterative_traversal/) | 3 problems (iter inorder/postorder, Morris) |
| 13 | Advanced Tree Structures | [13.advanced_structures](13.advanced_structures/) | 5 problems (segment ×2, Fenwick ×2, N-ary) |
| 14 | Design & Serialization | [14.serialization](14.serialization/) | 2 problems (serialize/deserialize tree + BST) |

**Total: 48 problems**, every file runnable and verified.

See [notes.txt](notes.txt) for the full roadmap tree, learning order, and the TreeNode boilerplate.

## How to add a problem

1. Pick the right pattern folder (and sub-folder once built out).
2. Create `N.problem_name.py` (N = next number in that folder).
3. Follow the file template below. Define a minimal `TreeNode` + `build` helper.
4. Tick the box in that folder's `notes.txt` checklist.

### Per-problem file template

```python
'''
N. Problem Title (Difficulty)
Problem Statement

<what the problem asks>

Example
Input:  ...
Output: ...
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def solution(root, ...):
    ...


if __name__ == "__main__":
    # build a tree from a level-order list (None = missing), run, print result
    print(...)   # Expected: ...

'''
Pattern
✅ <which pattern and why>

| Metric | Value |
| ------ | ----- |
| Time   | O(?)  |
| Space  | O(?)  |

Better Possible?
❌/✅ <reasoning>
'''
```

### How to run any file

```powershell
python "7.Trees\<folder>\<file>.py"
```

Or open the file in VS Code and press `Ctrl+F5` (Run Without Debugging).
