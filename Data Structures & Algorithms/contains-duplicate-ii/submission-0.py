class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {} # value -> index

        for i in range(len(nums)):
            if nums[i] in seen and abs(i - seen[nums[i]]) <= k:
                return True
            seen[nums[i]] = i
        return False