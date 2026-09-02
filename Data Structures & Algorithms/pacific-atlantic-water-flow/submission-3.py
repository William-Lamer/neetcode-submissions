class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        pacific, atlantic = set(), set()

        def dfs(row, col, prev_height, ocean):
            # Check the boundaries
            if row < 0 or col < 0 or row >= ROWS or col >= COLS:
                return

            # Check that the new height is greather than the previous height
            if heights[row][col] < prev_height:
                return 
            
            # Do not visit the same cell twice
            if (row, col) in ocean:
                return

            # Add the current cell to the visited set
            ocean.add((row, col))

            # Check all the neighboring cells
            directions = [(-1,0), (1,0), (0,-1), (0,1)]
            for dr, dc in directions:
                dfs(row + dr, col + dc, heights[row][col], ocean)




        # traverse all the top and bottom rows
        for col in range(COLS):
            dfs(0, col, 0, pacific)
            dfs(ROWS - 1, col, 0, atlantic)
        for row in range(ROWS):
            dfs(row, 0, 0, pacific)
            dfs(row, COLS - 1, 0, atlantic)


        # Return the intersection of the two sets
        return list(pacific & atlantic)



