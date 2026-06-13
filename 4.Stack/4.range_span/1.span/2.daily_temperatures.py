'''
2. Daily Temperatures (Medium)
Problem Statement

You are given an array temperatures where temperatures[i] is the temperature
on the i-th day.

For each day, find out how many days you have to wait until a warmer
temperature. If there is no future day with a warmer temperature, the answer
for that day is 0.

Return an array answer where answer[i] is the number of days to wait.

Example
Input:
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

Output:
[1, 1, 4, 2, 1, 1, 0, 0]

Input:
temperatures = [30, 40, 50, 60]

Output:
[1, 1, 1, 0]
'''

def dailyTemperatures(temperatures):
    n = len(temperatures)
    answer = [0] * n
    # Monotonic decreasing stack of indices waiting for a warmer day.
    stack = []

    for i, temp in enumerate(temperatures):
        # Today is warmer than the days sitting on the stack:
        # resolve each of them, distance = i - that day's index.
        while stack and temperatures[stack[-1]] < temp:
            prev = stack.pop()
            answer[prev] = i - prev
        stack.append(i)

    return answer


if __name__ == "__main__":
    print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    # Expected: [1, 1, 4, 2, 1, 1, 0, 0]
    print(dailyTemperatures([30, 40, 50, 60]))
    # Expected: [1, 1, 1, 0]


'''
Pattern
✅ Monotonic Decreasing Stack (Next Greater Element distance)

Why: This is "next greater element" reframed as a distance. Holding unresolved
days in a decreasing stack lets each warmer day pop and answer all the cooler
days waiting on it. Every index is pushed and popped once → linear time instead
of the O(n^2) brute force of scanning forward for each day.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No

Each element is pushed/popped once; O(n) is optimal.
'''
