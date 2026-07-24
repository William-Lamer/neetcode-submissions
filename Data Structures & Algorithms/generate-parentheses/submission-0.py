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
                open += 1
                dfs(depth + 1, open, close)
                stack.pop()
                open -= 1

            # adding a ")"
            if open > close:
                stack.append(")")
                close += 1
                dfs(depth + 1, open, close)
                stack.pop()
                close -= 1
            



        dfs(0, 0, 0)
        return res