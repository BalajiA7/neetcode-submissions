# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxValue):
            if not root:
                return 0

            maxValue = max(maxValue, root.val)
            count = 0
            # Count good node only if root val greater 
            # than maxValue so far
            if root.val >= maxValue:
                count = 1 

            left = dfs(root.left, maxValue)
            right = dfs(root.right, maxValue)

            return count + left + right

        return dfs(root, float("-infinity"))
