class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = [False] * len(nums)

        def dfs(i, subset):
            #stop case, reached full tree depth
            if i >= len(nums):
                res.append(subset.copy())
                return
            

            # start a dfs for each num currently not in subset
            for j in range(len(nums)):
                if visited[j]:
                    continue
                visited[j] = True
                subset.append(nums[j])
                dfs(i+1, subset)
                subset.pop()
                visited[j] = False
                

        dfs(0, [])
        return res
