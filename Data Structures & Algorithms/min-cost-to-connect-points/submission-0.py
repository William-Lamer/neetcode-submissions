class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dist = [float('inf')] * n
        dist[0] = 0
        in_tree = [False] * n
        total = 0

        for _ in range(n):
            u = -1
            for v in range(n):
                if not in_tree[v] and (u == -1 or dist[v] < dist[u]):
                    u = v
            in_tree[u] = True
            total += dist[u]

            x, y = points[u]

            for v in range(n):
                if not in_tree[v]:
                    d = abs(x - points[v][0]) + abs(y - points[v][1])
                    if d < dist[v]:
                        dist[v] = d
        
        return total
