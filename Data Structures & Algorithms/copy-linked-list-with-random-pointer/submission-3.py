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

        curr = head
        # map new nodes next to old nodes
        while curr:
            newNode = Node(curr.val)
            nextNode = curr.next

            curr.next = newNode
            newNode.next = nextNode

            curr = nextNode
        
        # create random pointer connection to new nodes
        curr = head
        while curr:
            random = curr.random
            if random:
                curr.next.random = random.next 
            curr = curr.next.next
        
        #remove old nodes in the final list
        copyHead = head.next
        curr = head
        while curr:
            copyNode = curr.next
            nextOriginal = copyNode.next

            #restore original node
            curr.next = nextOriginal

            if nextOriginal:
                copyNode.next = nextOriginal.next
            else:
                copyNode.next = None

            curr = nextOriginal

        
        return copyHead



        