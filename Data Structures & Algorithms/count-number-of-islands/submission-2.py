class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return
            
            # return if already visited
            if grid[row][col] != "1":
                return 
            
            # Mark it as visited
            grid[row][col] = "x"

            # Continue to all neighbor cells
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)



        islands = 0
        for row in range(ROWS):
            for col in range(COLS):

                if grid[row][col] == "1":
                    islands += 1
                    dfs(row, col)

        return islands