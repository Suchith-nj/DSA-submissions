class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if not edges:
            return True
        adj = defaultdict(list)
        for v, e in edges:
            adj[v].append(e)
            adj[e].append(v)
        
        visited = set()
        def dfs(node):
            if node  == destination:
                return True
            
            if node not in visited:
                visited.add(node)
                
                for nei in adj[node]:
                    if dfs(nei) == True:
                        return True
            return False
        
        return dfs(source)
            