class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pac, atl = set(), set()

        def dfs(row, col, visit, prev_height):
            # Check if out of bounds
            if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                return 

            # Check if already visited
            if (row, col) in visit:
                return 
            
            #check if height is higher
            if heights[row][col] < prev_height:
                return 

            # valid cell, add to set
            visit.add((row, col))

            # dfs on all adjacent nodes
            dfs(row - 1, col, visit, heights[row][col])
            dfs(row + 1, col, visit, heights[row][col])
            dfs(row, col - 1, visit, heights[row][col])
            dfs(row, col + 1, visit, heights[row][col])


        

        for row in range(ROWS):
            dfs(row, 0, pac, 0)
            dfs(row, COLS - 1, atl, 0)
        for col in range(COLS):
            dfs(0, col, pac, 0)
            dfs(ROWS - 1, col, atl, 0)


        return [[r, c] for r, c in pac & atl]