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
            
            left, right = None, None
            if p.val < root.val and q.val < root.val:
                left = dfs(root.left, p, q)
            elif p.val > root.val and q.val > root.val:
                right = dfs(root.right, p, q)
            
            return left or right or root
        
        return dfs(root, p, q)