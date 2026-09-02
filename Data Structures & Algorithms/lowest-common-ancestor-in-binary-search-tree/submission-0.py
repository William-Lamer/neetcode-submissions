# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        if not root: 
            return 0

        def lca(node):
            # If p and q are to the left
            if max(p.val, q.val) < node.val:
                # Traverse left
                return lca(node.left)
            elif min(p.val, q.val) > node.val:
                # Traverse right
                return lca(node.right)
            else:
                # Node is either in between or one of them. Its the LCA.
                return node
            
        
        return lca(root)