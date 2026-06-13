'''
3. Daily Temperatures (Medium)
Problem Statement

Given an array temperatures, return an array where answer[i] is the number of days
you must wait after day i to get a warmer temperature. If none, answer[i] = 0.

Example
Input:
temperatures = [73,74,75,71,69,72,76,73]

Output:
[1,1,4,2,1,1,0,0]
'''

def dailyTemperatures(temperatures):

    n = len(temperatures)
    result = [0] * n
    stack = []                  # indices of days awaiting a warmer day

    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:
            j = stack.pop()
            result[j] = i - j   # distance to the next warmer day
        stack.append(i)

    return result


if __name__ == "__main__":
    print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    # Expected: [1, 1, 4, 2, 1, 1, 0, 0]
    print(dailyTemperatures([30, 40, 50, 60]))   # Expected: [1, 1, 1, 0]

'''
Pattern
✅ Monotonic (decreasing) Stack storing INDICES

Key Observation
Same "next greater" pattern, but store indices so the answer is the index distance
i - j rather than the value.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No.
'''
