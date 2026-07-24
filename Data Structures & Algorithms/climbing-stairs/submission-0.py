class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def steps(n):
            if n <=1: 
                return 1

            # Check if its already in the map
            if n in memo:
                return memo[n]
            print(f"n: {n}")
            # Compute and store it
            ways = steps(n-1) + steps(n-2)
            print(f"ways: {ways}")
            memo[n] = ways

            return ways

        return steps(n)