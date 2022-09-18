class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        ROW = len(grid)
        COL = len(grid[0])
        islands = 0
        
        
        def dfs(grid, r,c):
            if r<0 or c<0 or r>=ROW or c>=COL or grid[r][c] != '1':
                return
            grid[r][c] = '#'            #Avoids using visited set
            dfs(grid, r+1, c)
            dfs(grid, r-1, c)
            dfs(grid, r, c+1)
            dfs(grid, r, c-1)
        
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == '1':
                    dfs(grid, r, c)
                    islands += 1
        return islands
            