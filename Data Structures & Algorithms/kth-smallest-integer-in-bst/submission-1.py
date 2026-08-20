# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.idx = 1

        def dfs(root):
            if not root:
                return None

            left = dfs(root.left)
            if left:
                return left

            # count here you are at which node
            if self.idx == k:
                return root.val
            self.idx +=1
            
            right = dfs(root.right)
            if right:
                return right

            return left or right
        
        return dfs(root)
            
        