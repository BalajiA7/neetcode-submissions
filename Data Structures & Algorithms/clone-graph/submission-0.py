"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        clone = {}

        def bfs(root):
            queue = deque()
            queue.append(root)
            newNode = Node(root.val)
            clone[root] = newNode

            while queue:
                curr = queue.popleft()
                print(curr.val)

                for neighbors in curr.neighbors:
                    if neighbors not in clone:
                        clone[neighbors] = Node(neighbors.val)
                        queue.append(neighbors)
                    clone[curr].neighbors.append(clone[neighbors])
        
        bfs(node)
        return clone[node]

                

        