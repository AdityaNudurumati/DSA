'''
1. Baseball Game (Easy)
Problem Statement

You are keeping score for a game with a list of string operations. Each operation
is one of:
- An integer x: record a new score of x.
- "+": record the sum of the previous two scores.
- "D": record double the previous score.
- "C": invalidate (remove) the previous score.

Return the sum of all scores remaining after applying every operation.

Example
Input:
["5","2","C","D","+"]

Output:
30
'''

def calPoints(operations):

    stack = []                       # running list of valid scores (LIFO)

    for op in operations:
        if op == "C":
            stack.pop()              # cancel the last score
        elif op == "D":
            stack.append(2 * stack[-1])      # double the last score
        elif op == "+":
            stack.append(stack[-1] + stack[-2])  # sum of last two scores
        else:
            stack.append(int(op))    # a plain integer score

    return sum(stack)


if __name__ == "__main__":
    print(calPoints(["5", "2", "C", "D", "+"]))                 # Expected: 30
    print(calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"])) # Expected: 27

'''
Pattern
✅ Stack Simulation — replay operations on a stack

Key Observation
Each operation only touches the most recent one or two scores, which is exactly the
LIFO access a stack provides; "C"/"D"/"+" become pop / peek-and-push.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No — every operation must be processed once.
'''
