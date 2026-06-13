'''
39. Combination Sum (Medium)
Problem Statement

Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers
sum to target. You may reuse the same number an unlimited number of times.

Two combinations are unique if the frequency of at least one chosen number
differs.

Example:
Input:
candidates = [2,3,6,7], target = 7

Output:
[[2,2,3], [7]]
'''


def combinationSum(candidates, target):
    candidates.sort()                     # enables early break on overshoot
    result = []

    def backtrack(start, path, remaining):
        if remaining == 0:                # goal reached
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:  # sorted -> all later also too big
                break
            path.append(candidates[i])
            # reuse allowed -> pass i (not i+1)
            backtrack(i, path, remaining - candidates[i])
            path.pop()

    backtrack(0, [], target)
    return result


if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    print(sorted(combinationSum(candidates, target)))
    # Expected: [[2, 2, 3], [7]]


'''
Pattern
✅ Backtracking with reuse (recurse on same index)
Recursing with the same start index allows repeating a candidate; sorting lets
us break as soon as a candidate exceeds the remaining target.
| Metric | Value          |
| ------ | -------------- |
| Time   | O(n^(T/min))   |
| Space  | O(T/min)       |
Better Possible?
❌ No

The combination count is exponential in target/min-candidate; this explores
each valid combination once.
'''
