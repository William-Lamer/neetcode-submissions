class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(row, col):
            # Check if out of bounds or ocean
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] == "0":
                return 
            
            if grid[row][col] == "1":
                grid[row][col] = "0"

            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)


        islands = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    dfs(row, col)
                    islands += 1 

        return islands