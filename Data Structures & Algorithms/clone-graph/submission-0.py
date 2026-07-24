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
            # If we have seen the node
            if node in seen:
                return seen[node]

            # Step 1: create a copy of the node
            copy = Node(node.val)
            # Step 2: add it to the map
            seen[node] = copy
            # Step 3: recurse into the neighbors
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))



            return copy
        
        return dfs(node) if node else None