class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            # stop case
            if total == target:
                res.append(cur.copy())
                return

            # not a valid path
            if i >= len(nums) or total > target:
                return


            # Create the path
            cur.append(nums[i])

            # can add the same number multiple times, so i and not i + 1
            dfs(i, cur, total + nums[i]) 

            # undo the choice
            cur.pop()

            #call dfs again for the next choice (the branch where we didnt add nums[i] but add nums[i + 1])
            dfs(i + 1, cur, total)





        

        dfs(0, [], 0)
        return res

            
