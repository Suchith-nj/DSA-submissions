class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def dfs(isConnected,visited,i):
            for j in range(len(isConnected)):
                #since it is symetric matrix, if we have already visted [i][j]
                # we don't have to visit [j][i]
                #adding i and j will take care of this condition
                if isConnected[i][j] == 1 and j not in visited:
                    visited.append(j)
                    dfs(isConnected,visited,j)
        
        visited = []
        count = 0
        for i in range(len(isConnected)):
            #we append j in visited but check for i also
            if i not in visited:
                dfs(isConnected,visited,i)
                count += 1
        return count 
    