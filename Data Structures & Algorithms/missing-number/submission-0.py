class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expectedSum = ((n) * (n + 1)) / 2
        diff = expectedSum - sum(nums)
        return int(diff)