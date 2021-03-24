"""
Leetcode - 70. Climbing Stairs

input: num - number of steps
output: num - number of distinct ways to get to the top == input

Note: can only take 1 or 2 steps

Thoughts
create a dictionary to keep track of ways we've gotten there (calulations)

"""
class Stairs(object):
    def __init__(self):
        self.memo = {}
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            self.memo[n] = 1
            return 1

        # already calculated this and is in memo
        if n in self.memo:
            print('grabbing memo for', n, self.memo[n])
            return self.memo[n]

        # calculating
        result = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        # memoizing
        self.memo[n] = result
        print(self.memo)
        return result

n = 1
# Output: 1
# [1, 0]

n1 = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step [2, 1, 0]
# 2. 2 steps [2, 0]

n2 = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step [3, 2, 1, 0] - from n = 2
# 2. 1 step + 2 steps [3, 2, 0] from n = 2
# 3. 2 steps + 1 step [3, 1, 0] from n = 1
# climbStairs(3) = climbStairs(2) + climbStairs(1)

print(Stairs().climbStairs(n1))
print(Stairs().climbStairs(n2))
print(Stairs().climbStairs(4))
