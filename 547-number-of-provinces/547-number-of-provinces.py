class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def dfs(isConnected,visited,i):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.append(j)
                    dfs(isConnected,visited,j)
        
        visited = []
        count = 0
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(isConnected,visited,i)
                count += 1
        return count 