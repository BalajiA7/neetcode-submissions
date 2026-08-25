# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        #dfs to encode string
        def dfs(root):
            if not root:
                res.append("N")
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        print(res)
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i +=1
                return None

            root = TreeNode(int(vals[self.i]))
            self.i+=1
            root.left = dfs()
            root.right = dfs()
            return root
        
        return dfs()


        
        # root = TreeNode(data[0])
        # stk = []
        # stk.append(root)
        # i = 1

        # while i < len(data):
        #     while i < len(data) and data[i] != "N":
        #         top = stk[-1]
        #         node = TreeNode(data[i])
        #         stk.append(node)
        #         if not top.left:
        #             top.left = node
        #         else:
        #             top.right = node
        #         i+=1
            
        #     count = 0
        #     while i < len(data) and data[i] == "N":
        #         count+=1
        #         if count == 2:
        #             stk.pop()
        #             count = 0
        #         i+=1
        #     if count == 1:
        #         stk.pop()
        
        # return root




