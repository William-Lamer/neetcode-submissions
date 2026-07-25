class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):
            if row >= len(grid) or row < 0:
                return
            if col >= len(grid[0]) or col < 0:
                return

            if grid[row][col] != "1": 
                return 

            # mark current as "x"
            grid[row][col] = "x"

            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)
                


        islands = 0
        for row in range(rows):
            for col in range(cols):
                current = grid[row][col]

                if current == "1":
                    dfs(row, col)
                    islands += 1

        return islands