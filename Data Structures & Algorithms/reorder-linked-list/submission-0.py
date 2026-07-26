# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        # Finding Mid Pointer
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second section
        second = slow.next
        slow.next = None

        prev = None
        curr = second
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        head2 = prev
        dummy = ListNode()
        prev = dummy

        while head and head2:
            prev.next = head
            head = head.next
            prev = prev.next

            prev.next = head2
            head2 = head2.next
            prev = prev.next
        
        if head:
            prev.next = head