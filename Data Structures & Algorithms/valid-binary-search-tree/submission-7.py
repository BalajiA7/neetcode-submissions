# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validBST(root, leftBoundary, rightBoundary):
            if not root:
                return True

            if not (leftBoundary < root.val < rightBoundary):
                return False
            
            return validBST(root.left, leftBoundary, root.val) and validBST(root.right, root.val, rightBoundary)
        
        return validBST(root, float("-infinity"), float("infinity"))
