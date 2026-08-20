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
        if not head:
            return None

        # create a new node and link it next to old node
        curr = head
        while curr:
            newNode = Node(curr.val)
            nextNode = curr.next
            # inserting new node between older nodes
            curr.next = newNode
            newNode.next = nextNode
            curr = nextNode

        # assign random pointers to new node
        curr = head
        while curr:
            oldRandomNode = curr.random
            # assinging random nodes
            if oldRandomNode:
                curr.next.random = oldRandomNode.next
            curr = curr.next.next

        # Dettach old node and new node
        curr = head
        newHead = curr.next
        while curr:
            newNode = curr.next
            nextOldNode = newNode.next
            if nextOldNode:
                newNode.next = nextOldNode.next
            curr.next = nextOldNode
            curr = nextOldNode
        
        return newHead

        