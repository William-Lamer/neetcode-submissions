class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(row, col, i): 
            if i == len(word):
                return True

            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or word[i] != board[row][col]:
                return False

            board[row][col] = "#"
            res = (dfs(row + 1, col, i + 1) or
                   dfs(row - 1, col, i + 1) or
                   dfs(row, col - 1, i + 1) or
                   dfs(row, col + 1, i + 1))
            board[row][col] = word[i]
            return res
            


        found = False
        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0):
                    return True
                
        return False