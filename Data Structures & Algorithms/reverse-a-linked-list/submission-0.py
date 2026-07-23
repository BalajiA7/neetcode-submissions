# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []

        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
        
        # reverse the list and iterate to form a new linkedlist
        head, curr = None, None
        for val in reversed(values):
            node = ListNode(val)

            if not head:
                head = node
                curr = node
            else:
                curr.next = node
                curr = curr.next
        
        return head

        