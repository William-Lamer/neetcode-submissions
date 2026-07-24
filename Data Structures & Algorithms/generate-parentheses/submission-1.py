class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def dfs(depth, open, close):
            # stopping case
            if depth >= n*2:
                res.append("".join(stack))
                return
            
            # we have 2 choices, add a "(", or ")"

            # adding a "("
            if open < n:
                stack.append("(")
                dfs(depth + 1, open+1, close)
                stack.pop()

            # adding a ")"
            if open > close:
                stack.append(")")
                dfs(depth + 1, open, close+1)
                stack.pop()
            



        dfs(0, 0, 0)
        return res