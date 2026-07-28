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
        dummy = Node(0)
        temp = dummy
        curr = head
        nodeMapping = {}

        while curr:
            newNode = Node(curr.val)
            nodeMapping[curr] = newNode
            temp.next = newNode
            temp = temp.next
            curr = curr.next
        
        print(nodeMapping)
        
        head1 = head
        head2 = dummy.next

        while head1:
            newRandomNode = nodeMapping[head1.random] if head1.random else None
            head2.random = newRandomNode
            head1 = head1.next
            head2 = head2.next
        
        return dummy.next

        