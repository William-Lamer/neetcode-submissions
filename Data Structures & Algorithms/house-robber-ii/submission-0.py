class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(houses):
            prev2, prev1 = 0, 0

            for house in houses:
                prev2, prev1 = prev1, max(prev2 + house , prev1)
            
            return prev1
        
        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))
