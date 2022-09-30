class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = []
        n = len(isConnected)
        def dfs(i):
            for j in range(n):
                #since it is symetric matrix, if we have already visted [i][j]
                # we don't have to visit [j][i]
                #adding i and j will take care of this condition
                if isConnected[i][j] == 1 and j not in visited:
                    visited.append(j)
                    dfs(j)
        
        
        count = 0
        for i in range(n):
            #we append j in visited but check for i also
            if i not in visited:
                dfs(i)
                count += 1
        return count 
    