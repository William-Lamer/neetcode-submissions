class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        row_zero = any(matrix[0][c] == 0 for c in range(cols))
        col_zero = any(matrix[r][0] == 0 for r in range(rows))

        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if row_zero:
            for c in range(cols):
                matrix[0][c] = 0
        if col_zero:
            for r in range(rows):
                matrix[r][0] = 0
            