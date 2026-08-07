# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def findDiameter( root):
            if not root:
                return 0

            leftHeight = findDiameter(root.left)
            rightHeight = findDiameter(root.right)

            self.diameter = max(self.diameter, leftHeight+rightHeight)
            
            return 1 + max(leftHeight, rightHeight)

        findDiameter(root)    
        return self.diameter