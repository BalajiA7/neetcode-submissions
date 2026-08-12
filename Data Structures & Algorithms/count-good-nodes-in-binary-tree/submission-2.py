# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def getPathofNode(root, maxValue):
            if not root:
                return 0
            
            maxValue = max(maxValue, root.val)
            leftTree = getPathofNode(root.left, maxValue)
            rightTree = getPathofNode(root.right, maxValue)
            current = 1 if maxValue == root.val else 0

            return current + leftTree + rightTree

        return getPathofNode(root, float('-infinity'))


         