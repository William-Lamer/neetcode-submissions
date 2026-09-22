class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        perimeter = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    perimeter += 4
                
                    if r + 1 < ROWS and grid[r + 1][c] == 1:
                        perimeter -= 2
                    if c + 1 < COLS and grid[r][c + 1] == 1:
                        perimeter -= 2
                
        return perimeter