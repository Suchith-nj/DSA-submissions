class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        currList = []

        def findPath(node):
            if node == len(graph)-1:
                result.append(currList.copy())
                return

            for i in graph[node]:
                currList.append(i)
                findPath(i)
                currList.pop()
        
        #we are just checking path from one source
        #so there won't be any duplicated, 1 src all neighbours
        currList.append(0)
        findPath(0)
        return result
         