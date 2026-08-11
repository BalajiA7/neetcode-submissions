# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, node, path):
        if not root:
            return False

        path.append(root)

        if root.val == node.val:
            return True
        
        if node.val < root.val:
            found = self.dfs(root.left, node, path)
        else:
            found = self.dfs(root.right, node, path)
        
        if found:
            return True

        path.pop()
        return False

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pathA = []
        pathB = []
        self.dfs(root, p, pathA)
        self.dfs(root, q, pathB)

        length = max(len(pathA), len(pathB)) - 1
        while length >= 0:
            if length < len(pathA) and length < len(pathB):
                if pathA[length].val == pathB[length].val:
                    return pathA[length]
            length-=1

        return None
        