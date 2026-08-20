# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root, res):
            if not root:
                return None
            dfs(root.left, res)
            res.append(root.val)
            dfs(root.right, res)

            return res
        
        arr = dfs(root, [])
        print(arr)
        return arr[k-1]
        
            
        