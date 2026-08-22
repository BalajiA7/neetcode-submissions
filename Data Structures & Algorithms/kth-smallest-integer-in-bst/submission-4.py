# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        idx = 0

        while curr or len(stack):
            while curr:
                stack.append(curr)
                curr = curr.left
            idx+=1
            node = stack.pop()
            if idx == k:
                return node.val
            curr = node.right
