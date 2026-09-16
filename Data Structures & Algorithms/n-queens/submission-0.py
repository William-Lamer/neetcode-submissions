class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        queen = [] # queens[r] is the position of the queen on the row r
        col, posDiag, negDiag = set(), set(), set()

        def backtrack(r):
            if r == n:
                # We have a valid board, so append it to res
                current_board = []
                for c in queen:
                    current_board.append("." * c + "Q" + "." * (n - c - 1))
                res.append(current_board)
                return

            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    # There is conflict between two queens
                    continue
                
                queen.append(c)
                col.add(c)
                negDiag.add(r-c)
                posDiag.add(r+c)

                backtrack(r + 1)

                queen.pop()
                col.remove(c)
                negDiag.remove(r-c)
                posDiag.remove(r+c)


        backtrack(0)
        return res