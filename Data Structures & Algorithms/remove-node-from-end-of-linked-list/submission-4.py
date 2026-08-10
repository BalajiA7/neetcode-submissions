# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        # move fast by n step ahead
        fast = head
        while n > 0:
            fast = fast.next
            n-=1
        
        # move each pointer by one
        dummy = ListNode(-1, head)
        slow = dummy
        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return dummy.next
        