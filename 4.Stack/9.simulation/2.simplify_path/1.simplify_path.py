'''
1. Simplify Unix Path (Medium)
Problem Statement

Given an absolute Unix-style path, return its simplified canonical form. A '.' refers to
the current directory, a '..' moves up one level, and multiple slashes collapse into one.
The canonical path starts with a single '/', has no trailing '/' (unless it is root), and
contains no '.' or '..' components.

Example
Input:
path = "/a/./b/../../c/"

Output:
"/c"
'''

def simplifyPath(path):

    stack = []      # directory names on the resolved path

    for part in path.split("/"):
        if part == "" or part == ".":
            continue                 # empty (// or trailing) or current dir -> skip
        elif part == "..":
            if stack:                # go up one level if possible
                stack.pop()
        else:
            stack.append(part)       # a real directory name

    return "/" + "/".join(stack)     # always rooted; "" -> "/"


if __name__ == "__main__":
    print(simplifyPath("/home/"))         # Expected: /home
    print(simplifyPath("/../"))           # Expected: /
    print(simplifyPath("/home//foo/"))    # Expected: /home/foo
    print(simplifyPath("/a/./b/../../c/"))# Expected: /c

'''
Pattern
✅ Stack Simulation — push dir names; '..' pops, '.' / '' skip

Key Observation
Splitting on '/' turns the path into tokens. A stack mirrors the directory hierarchy:
a name pushes, '..' pops (capped at root), and '.'/'' are no-ops. Re-joining with '/'
and prefixing root yields the canonical form.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No.
'''
