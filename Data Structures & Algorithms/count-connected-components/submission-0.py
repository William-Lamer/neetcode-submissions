class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # Build adjency map
        adj = { i:[] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()

        def dfs(node):
            if node in visit:
                return False
            visit.add(node)
            for nei in adj[node]:
                dfs(nei)

            return True




        res = 0
        for i in range(n):
            if dfs(i):
                res += 1

        return res