class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(row, col):
            if row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0:
                return 0
            
            if grid[row][col] != 1:
                return 0
            
            # Mark it as visited, and increase the current size
            grid[row][col] = -1

            #dfs on all the neighboring cells
            up = dfs(row - 1, col)
            down = dfs(row + 1, col)
            left = dfs(row, col - 1)
            right = dfs(row, col + 1)

            return 1 + up + down + left + right



        max_island_area = 0
        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):

                max_island_area = max(max_island_area, dfs(row, col))


        return max_island_area