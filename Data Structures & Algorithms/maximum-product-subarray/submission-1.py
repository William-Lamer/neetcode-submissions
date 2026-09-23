class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1, 1
        max_product = nums[0]
        for x in nums:
            temp_cur_min = curMin
            curMin = min(x, x * curMax, x * curMin)
            curMax = max(x, x * curMax, x * temp_cur_min)
            max_product = max(max_product, curMin, curMax)
        return max_product   