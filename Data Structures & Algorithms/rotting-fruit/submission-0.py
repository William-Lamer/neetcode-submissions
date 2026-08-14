class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    fresh += 1

        time = 0
        while fresh > 0:
            flag = False

            for row in range(ROWS):
                for col in range(COLS):
                    if grid[row][col] == 2:
                        directions = [(1,0), (-1, 0), (0,1), (0,-1)]
                        for dr, dc in directions:
                            r, c = row + dr, col + dc
                            if r < ROWS and c < COLS and r >= 0 and c >= 0 and grid[r][c] == 1:
                                grid[r][c] = 3
                                fresh -= 1
                                flag = True
                    
            
            if not flag:
                return -1

            for row in range(ROWS):
                for col in range(COLS):
                    if grid[row][col] == 3:
                        grid[row][col] = 2

            time += 1


        return time