class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2 

            # Move right
            if nums[mid] > nums[r]:
                l = mid + 1
            else: #move left
                r = mid
            
        return nums[l]

                