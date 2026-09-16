class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])

        # Check rows: 
        for row in range(ROWS):
            seen = set()
            for num in board[row]:
                if num == ".":
                    continue
                if num in seen:
                    return False
                else:
                    seen.add(num)
            
        # Check cols:
        for col in range(COLS):
            seen = set()
            for row in range(ROWS):
                if board[row][col] == ".":
                    continue
                
                if board[row][col] in seen:
                    return False
                else:
                    seen.add(board[row][col])
        
        # Check squares:
        for square_y in range(3):
            for square_x in range(3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        r, c = 3*square_y + i, 3*square_x + j
                        if board[r][c] == ".":
                            continue
                        if board[r][c] in seen:
                            return False
                        else:
                            seen.add(board[r][c])
        
        return True

























