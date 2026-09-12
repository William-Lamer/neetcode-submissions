class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])


        def backtrack(r, c, i):
            if i == len(word):
                return True

            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != word[i]:
                return False
            
            board[r][c] = "#"
            directions = [(-1,0), (1,0), (0,-1), (0,1)]
            for dr, dc in directions:
                if backtrack(r + dr, c + dc, i + 1):
                    return True

            board[r][c] = word[i]
            return False


        for row in range(ROWS):
            for col in range(COLS):
                if backtrack(row, col, 0):
                    return True
        return False