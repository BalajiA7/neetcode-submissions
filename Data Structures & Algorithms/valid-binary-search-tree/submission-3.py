# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# if not root:
#     return True
        
#     if not root.left and not root.right:
#         return True
    
#     leftTree = self.isValidBST(root.left)
#     rightTree = self.isValidBST(root.right)
    
#     isCurrentNodeBst = False
#     if not root.left:
#         isCurrentNodeBst = root.val < root.right.val
#     elif not root.right:
#         isCurrentNodeBst = root.left.val < root.val
#     else:
#         isCurrentNodeBst = root.left.val < root.val < root.right.val 

#     return leftTree and rightTree and isCurrentNodeBst


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, left, right):
            if not root:
                return True

            if not left < root.val < right:
                return False
                
            return dfs(root.left, left, root.val) and dfs(root.right, root.val, right)

        return dfs(root, float("-infinity"), float("infinity"))
        