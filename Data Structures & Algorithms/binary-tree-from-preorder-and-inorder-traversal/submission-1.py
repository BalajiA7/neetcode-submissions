# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashMap = {val:idx for idx, val in enumerate(inorder)}

        def dfs(preLeft, preRight, inLeft, inRight):
            if preLeft > preRight:
                return None
            root = TreeNode(preorder[preLeft])
            mid = hashMap[preorder[preLeft]]
            leftSize = mid - inLeft
            root.left = dfs(preLeft+1, preLeft+leftSize, inLeft, mid-1)
            root.right = dfs(preLeft+leftSize+1, preRight, mid+1, inRight)
            return root
        
        return dfs(0,len(preorder)-1, 0, len(inorder)-1)

        # if not preorder or not inorder:
        #     return None
        
        # root = TreeNode(preorder[0])
        # mid = inorder.index(preorder[0])
        # root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        # root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        # return root
        