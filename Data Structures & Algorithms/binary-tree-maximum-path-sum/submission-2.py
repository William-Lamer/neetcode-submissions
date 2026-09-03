# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        maxSum = root.val
        def dfs(node):
            nonlocal maxSum
            if node is None:
                return 0

            leftGain = max(dfs(node.left), 0)
            rightGain = max(dfs(node.right), 0)

            sum = node.val + max(leftGain, rightGain)
            end = node.val + leftGain + rightGain
            maxSum = max(maxSum, sum, end)
            return sum


        dfs(root)
        return maxSum