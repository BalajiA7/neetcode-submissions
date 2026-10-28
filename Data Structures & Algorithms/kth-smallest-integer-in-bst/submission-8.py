# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # values = []
        self.k = k
        self.val = root.val
        
        def bst(root):
            if not root:
                return
            
            left = bst(root.left)
            # I can access the sorted elements
            self.k -= 1
            if self.k == 0:
                self.val = root.val
                return
            right = bst(root.right)
        
        bst(root)
        return self.val
    

        