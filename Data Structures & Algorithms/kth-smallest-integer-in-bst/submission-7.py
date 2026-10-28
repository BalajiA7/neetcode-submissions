# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []
        
        def bst(root):
            if not root:
                return 
            
            left = bst(root.left)
            values.append(root.val)
            right = bst(root.right)
        
        bst(root)
        print(values)
        return values[k-1]
    

        