# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle of the linked list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow

        # split and reverse the second half
        curr = mid.next
        mid.next = None
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        # merge both halfs
        l1 = head
        l2 = prev
        dummy = ListNode(-1)
        temp = dummy
        while l1 and l2:
            temp.next = l1
            l1 = l1.next
            temp = temp.next

            temp.next = l2
            l2 = l2.next
            temp = temp.next
        
        if l1:
            temp.next = l1
        elif l2:
            temp.next = l2
