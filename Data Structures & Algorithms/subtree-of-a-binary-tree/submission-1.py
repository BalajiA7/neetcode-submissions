# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def merkle(self, root):
        if not root:
            return "#"
        leftTree = self.merkle(root.left)
        rightTree = self.merkle(root.right)
        root.merkle = leftTree + str(root.val) + rightTree
        return root.merkle

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.merkle(root)
        self.merkle(subRoot)

        def dfs(root):
            if not root:
                return False
            return (root.merkle == subRoot.merkle) or dfs(root.left) or dfs(root.right)
        
        return dfs(root)

    # def isSameTree(self, root1, root2):
    #     if not root1 and not root2:
    #         return True

    #     if not root1 or not root2 or (root1.val != root2.val):
    #         return False

    #     return self.isSameTree(root1.left, root2.left) and self.isSameTree(root1.right, root2.right)

    # def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    #     if not root: 
    #         return False

    #     if not subRoot: 
    #         return True
        
    #     if self.isSameTree(root, subRoot):
    #         return True

    #     return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right, subRoot)
        