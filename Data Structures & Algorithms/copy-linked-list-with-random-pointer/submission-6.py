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
            return head

        # create a new node and place inbetween old nodes
        curr = head
        while curr:
            newNode = Node(curr.val)
            next = curr.next
            curr.next = newNode
            newNode.next = next
            curr = curr.next.next
        print("Reached here 1")

        # link random pointers for new node with oldnode refernce
        curr = head
        while curr:
            random = curr.random
            curr.next.random = random.next if random else None
            curr = curr.next.next

        print("Reached here 2")
        # unlink new nodes and older nodes
        curr = head
        newHead = curr.next
        while curr:
            newNode = curr.next
            curr.next = newNode.next
            newNode.next = curr.next.next if curr.next else None
            curr = curr.next
        
        return newHead
       