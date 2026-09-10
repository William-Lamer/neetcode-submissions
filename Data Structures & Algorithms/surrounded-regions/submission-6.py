class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != "O":
                return
            
            board[r][c] = "#"

            directions = [(-1,0), (1,0), (0,-1), (0,1)]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        
        for col in range(COLS):
            dfs(0, col)
            dfs(ROWS - 1, col)
        for row in range(ROWS):
            dfs(row, 0)
            dfs(row, COLS - 1)

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O":
                    board[row][col] = "X"
                if board[row][col] == "#":
                    board[row][col] = "O"