'''
40. Combination Sum II (Medium)
Problem Statement

Given a collection of candidate numbers (candidates) and a target number
(target), find all unique combinations in candidates where the candidate
numbers sum to target.

Each number in candidates may be used only once in the combination. The
solution set must not contain duplicate combinations.

Example:
Input:
candidates = [10,1,2,7,6,1,5], target = 8

Output:
[[1,1,6], [1,2,5], [1,7], [2,6]]
'''


def combinationSum2(candidates, target):
    candidates.sort()                     # group dups + enable break
    result = []

    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            # skip duplicate value at the same depth to avoid dup combos
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > remaining:  # sorted -> prune
                break
            path.append(candidates[i])
            # each number once -> recurse on i+1
            backtrack(i + 1, path, remaining - candidates[i])
            path.pop()

    backtrack(0, [], target)
    return result


if __name__ == "__main__":
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(sorted(combinationSum2(candidates, target)))
    # Expected: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]


'''
Pattern
✅ Backtracking, each element once + duplicate pruning
Sort, advance to i+1 so no element repeats, and skip equal values at the same
tree depth so duplicate combinations are never generated.
| Metric | Value    |
| ------ | -------- |
| Time   | O(2^n)   |
| Space  | O(n)     |
Better Possible?
❌ No

In the worst case the subset space is 2^n; pruning only trims duplicates and
overshoots.
'''
