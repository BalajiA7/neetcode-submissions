# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(root, p, q):
            if not root:
                return None
            if root == p or root == q:
                return root
                
            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)

            if left and right:
                return root
            
            return left or right
        
        return dfs(root, p, q)