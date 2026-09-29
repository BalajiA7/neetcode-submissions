# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # self.diameter = 0
        def dfs(root):
            if not root:
                return [0,0]

            leftHeight, leftValue = dfs(root.left)
            rightHeight, rightValue = dfs(root.right)
            # self.diameter = max(self.diameter, left + right)
            return [1 + max(leftHeight, rightHeight), max(leftHeight + rightHeight, leftValue + rightValue)] 
        
        return dfs(root)[1]
        