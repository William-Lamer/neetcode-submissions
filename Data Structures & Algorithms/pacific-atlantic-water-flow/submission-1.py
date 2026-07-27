class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pac, atl = set(), set()

        def dfs(row, col, visit, prev_height):
            # Check if out of bounds or lower or if already present in the set:
            if (row < 0 or col < 0 or row >= len(heights) 
                or col >= len(heights[0]) or heights[row][col] < prev_height
                or (row, col) in visit):
                return
            

            # This is an accessible cell, so add it to the set.
            visit.add((row, col))

            # dfs on the neighbor cells
            dfs(row - 1, col, visit, heights[row][col])
            dfs(row + 1, col, visit, heights[row][col])
            dfs(row, col - 1, visit, heights[row][col])
            dfs(row, col + 1, visit, heights[row][col])

    


        # Top and bottom row 
        for col in range(COLS):
            dfs(0, col, pac, 0)
            dfs(ROWS - 1, col, atl, 0)

        # Left and right column
        for row in range(ROWS):
            dfs(row, 0, pac, 0)
            dfs(row, COLS - 1, atl, 0)
        

        return [[r,c] for r, c in pac & atl]