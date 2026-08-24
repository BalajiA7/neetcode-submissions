# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = root.val

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            currSum = max(root.val, root.val + max(left, right), root.val+left+right)
            self.maxSum = max(self.maxSum, currSum)
            return max(root.val, root.val + max(left, right))

        dfs(root)
        return self.maxSum