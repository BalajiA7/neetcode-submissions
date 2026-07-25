# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr = []

        curr = list1
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        curr = list2
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        print(arr)
        
        head,curr = None, None
        for value in sorted(arr):
            node = ListNode(value)
            if head:
                curr.next = node
                curr = curr.next
            else:
                head = node
                curr = head

        return head




        