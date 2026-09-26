class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        
        counter = defaultdict(int) #value -> count

        for num in nums:
            counter[num] += 1
            if counter[num] > len(nums) / 2:
                return num