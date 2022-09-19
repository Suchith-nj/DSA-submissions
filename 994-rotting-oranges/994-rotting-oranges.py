class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        time, fresh = 0,0
        q = deque()
        
        for r in range (ROW):
            for c in range (COL):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2:
                    q.append([r,c])
        
        while q and fresh > 0:
            for i in range (len(q)):
                r,c = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr,dc in directions:
                    row, col = dr+r, dc+c
                    if (0<=row<ROW and 0<=col<COL and grid[row][col]== 1):
                        grid[row][col] = 2
                        q.append([row,col])
                        fresh -= 1
            time +=1
        return time if fresh == 0 else -1