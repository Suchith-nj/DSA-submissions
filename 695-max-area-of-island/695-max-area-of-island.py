class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        ROW = len(grid)
        COL = len(grid[0])
        
        maxArea = 0
        
        def dfs(grid, i, j):
            if i<0 or j<0 or i>=ROW or j>=COL or grid[i][j] != 1:
                return 0

            
            grid[i][j] = '#'
            maxArea = 1+ dfs(grid, i+1, j) + dfs(grid, i-1, j) + dfs(grid, i, j+1) +  dfs(grid, i, j-1)
            

            return maxArea
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    result = dfs(grid, i, j)
                    maxArea = max(maxArea, result)
                    
        return maxArea
    
                    
    
        