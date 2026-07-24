class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def steps(n):
            if n <=1: 
                return 1

            if n in memo:
                return memo[n]
                
            ways = steps(n-1) + steps(n-2)
            memo[n] = ways

            return ways

        return steps(n)