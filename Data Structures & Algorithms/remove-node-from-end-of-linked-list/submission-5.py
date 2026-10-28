# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find the length of the LL
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length+=1

        # distance
        distance = length - n
        temp = ListNode(-1, head)
        prev, curr = temp, head

        # move the node til the distance
        while distance:
            prev = curr
            curr = curr.next
            distance -=1
        
        prev.next = curr.next
        curr.next = None

        return temp.next
        
 
        

        