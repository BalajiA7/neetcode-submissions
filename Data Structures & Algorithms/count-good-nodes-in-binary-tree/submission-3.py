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
            
            count = 1 if root.val >= maxValue else 0
            maxValue = max(maxValue, root.val)
            count += getPathofNode(root.left, maxValue)
            count += getPathofNode(root.right, maxValue)

            return count

        return getPathofNode(root, root.val)


         