'''
1. Asteroid Collision (Medium)
Problem Statement

Given an array of integers, each representing an asteroid in a row, the absolute value is
its size and the sign its direction (positive = right, negative = left). When two asteroids
moving toward each other meet, the smaller explodes; equal sizes both explode. Same-direction
asteroids never collide. Return the state after all collisions.

Example
Input:
asteroids = [5, 10, -5]

Output:
[5, 10]
'''

def asteroidCollision(asteroids):

    stack = []      # surviving asteroids, left to right

    for a in asteroids:
        alive = True
        # a collision happens only when a moves left into a right-moving top
        while alive and a < 0 and stack and stack[-1] > 0:
            if stack[-1] < -a:
                stack.pop()        # top is smaller -> it explodes, keep checking
                continue
            elif stack[-1] == -a:
                stack.pop()        # equal -> both explode
            alive = False          # incoming destroyed (or both did)
        if alive:
            stack.append(a)        # survives all collisions

    return stack


if __name__ == "__main__":
    print(asteroidCollision([5, 10, -5]))     # Expected: [5, 10]
    print(asteroidCollision([8, -8]))         # Expected: []
    print(asteroidCollision([10, 2, -5]))     # Expected: [10]
    print(asteroidCollision([-2, -1, 1, 2]))  # Expected: [-2, -1, 1, 2]

'''
Pattern
✅ Stack Simulation — push; resolve collisions against the top

Key Observation
Only a left-moving asteroid can collide, and only with a right-moving asteroid on top of
the stack. We pop the stack while the top loses, stop when the incoming one loses, and push
when nothing on top opposes it. Each asteroid is pushed and popped at most once.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No.
'''
