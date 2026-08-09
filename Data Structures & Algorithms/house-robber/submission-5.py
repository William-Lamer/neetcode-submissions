class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2, prev1 = 0, 0

        for num in nums:
            temp = prev2
            prev2 = prev1
            prev1 = max(prev1, temp + num)

        return prev1