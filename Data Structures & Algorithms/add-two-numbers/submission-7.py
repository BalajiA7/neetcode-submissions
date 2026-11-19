# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        carry = 0
        dummy = ListNode(-1)
        temp = dummy

        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            total = a + b + carry

            nodeVal = total % 10
            carry = total // 10

            temp.next = ListNode(nodeVal)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            temp = temp.next
        
        return dummy.next