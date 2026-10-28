# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        while n > 0:
            fast = fast.next
            n-=1

        temp = ListNode(-1, head)
        slow = temp

        # move the node til the distance
        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return temp.next
        
 
        

        