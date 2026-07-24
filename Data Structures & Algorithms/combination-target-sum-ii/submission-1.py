class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        # sort the array to idenfity duplicates
        candidates.sort()


        def dfs(i, cur, total):
            # stop case
            if total == target:
                res.append(cur.copy())
                return
            # not a valid path
            if i >= len(candidates) or total > target:
                return
            
            # make our first choice, still valid even if duplicate number
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            cur.pop()
            # done using that number, no duplicates allowed.
            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            
            dfs(i + 1, cur, total)


        dfs(0, [], 0)
        return res