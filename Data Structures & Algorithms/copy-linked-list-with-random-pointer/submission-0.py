"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copied = {}

        def copy(node):
            if not node:
                return None
            if node in copied:
                return copied[node]
            
            # Create a copy
            node_copy = Node(node.val)

            # Add it to the copied dict
            copied[node] = node_copy

            # Create its next pointer
            node_copy.next = copy(node.next)

            # Create its random pointer
            node_copy.random = copy(node.random)


            return node_copy



        return copy(head)
