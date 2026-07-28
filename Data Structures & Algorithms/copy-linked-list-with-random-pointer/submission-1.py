"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        nodeMapping = {None: None}

        while curr:
            nodeMapping[curr] =  Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            nodeMapping[curr].next = nodeMapping[curr.next]
            nodeMapping[curr].random = nodeMapping[curr.random]
            curr = curr.next
        
        return nodeMapping[head]

        