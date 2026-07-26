class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(row, col):
            # Check if out of bounds
            if row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0:
                return 0
            
            # Check if already visited or ocean
            if grid[row][col] != 1:
                return 0

            # Mark as visited
            grid[row][col] = -1
            
            return (1 + dfs(row - 1, col) + dfs(row + 1, col)
                    + dfs(row, col - 1) + dfs(row, col + 1))



        max_area = 0
        for row in range(ROWS):
            for col in range(COLS):
                
                max_area = max(max_area, dfs(row, col))

        return max_area