class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        fresh = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    fresh += 1

        time = 0
        while fresh > 0:
            flag = False
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 2:
                        directions = [(-1,0), (1,0), (0,-1), (0,1)]
                        for dr, dc in directions:
                            if r + dr < 0 or r + dr >= ROWS or c + dc < 0 or c + dc >= COLS:
                                continue
                            if grid[r + dr][c + dc] == 1:
                                grid[r + dr][c + dc] = 3
                                fresh -= 1
                                flag = True
            
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 3:
                        grid[r][c] = 2

            time += 1

            if not flag:
                return -1
            
        return time