class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        seen = set()
        def dfs(node, prev):
            if node in seen:
                return False
            
            seen.add(node)

            for neighbor in adj[node]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor, node):
                    return False

            return True




        return dfs(0, -1) and n == len(seen)
