# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.findMaxDepth(root)
    
    def findMaxDepth(self, root):
        if not root:
            return 0

        leftHeight = self.findMaxDepth(root.left)
        rightHeight = self.findMaxDepth(root.right)

        return 1 + max(leftHeight, rightHeight)
        

        