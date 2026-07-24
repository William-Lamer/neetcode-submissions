class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def dfs(open, close):
            # stopping case
            if close == n:
                res.append("".join(stack))
                return
            
            # we have 2 choices, add a "(", or ")"

            # adding a "("
            if open < n:
                stack.append("(")
                dfs(open+1, close)
                stack.pop()

            # adding a ")"
            if open > close:
                stack.append(")")
                dfs(open, close+1)
                stack.pop()
            
        dfs(0, 0)
        return res