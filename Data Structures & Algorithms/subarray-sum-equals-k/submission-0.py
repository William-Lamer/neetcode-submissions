class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        running = 0
        seen = defaultdict(int)
        seen[0] = 1

        for num in nums:
            running += num
            res += seen[running - k]
            seen[running] += 1
        return res