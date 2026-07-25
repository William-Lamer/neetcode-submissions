"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = {}

        def dfs(node):
            if node in seen:
                return seen[node]

            #create a copy
            copied = Node(node.val)
            ## add it to seen
            seen[node] = copied

            for neighbor in node.neighbors:
                copied.neighbors.append(dfs(neighbor))
            
            return copied
        
        return dfs(node) if node else None