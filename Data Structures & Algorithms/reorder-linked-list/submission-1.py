# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = slow.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # mid 
        mid = slow
        head2 = mid.next
        mid.next = None

        # reverse second half
        prev = None
        curr = head2
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        head2 = prev
        # iterate both heads and merge it
        dummy = ListNode()
        temp = dummy
        while head and head2:
            temp.next = head
            head = head.next
            temp = temp.next

            temp.next = head2
            head2 = head2.next
            temp = temp.next
        
        if head:
            temp.next = head
        elif head2:
            temp.next = head2
        