# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inorderMap = {val:idx for idx,val in enumerate(inorder)}
        
        def dfs(preStart, preEnd, inStart, inEnd):
            if preStart > preEnd:
                return None
            
            root = TreeNode(preorder[preStart])
            mid = inorderMap[root.val]
            leftValue = mid - inStart

            root.left = dfs(preStart+1, preStart+leftValue, inStart, mid-1)
            root.right = dfs(preStart+leftValue+1, preEnd, mid+1, inEnd)

            return root

        return dfs(0, len(preorder)-1, 0, len(inorder)-1)