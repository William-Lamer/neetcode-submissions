class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = curMax = curMin = nums[0]

        for n in nums[1:]:
            cands = (n, curMax * n, curMin * n)
            curMax, curMin = max(cands), min(cands)
            res = max(res, curMax)
        return res