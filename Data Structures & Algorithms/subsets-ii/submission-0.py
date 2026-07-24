class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(depth, subset):
            if depth == len(nums):
                res.append(subset[:])
                return
            
            subset.append(nums[depth])
            dfs(depth + 1, subset)
            subset.pop()

            while depth + 1 < len(nums) and nums[depth] == nums[depth + 1]:
                depth += 1
            
            dfs(depth + 1, subset)
        
        dfs(0, [])
        return res