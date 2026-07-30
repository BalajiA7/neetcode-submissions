# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        curr1, curr2 = l1,l2
        dummy = ListNode()
        temp = dummy

        while curr1 or curr2 or carry:
            v1 = curr1.val if curr1 else 0
            v2 = curr2.val if curr2 else 0

            total = carry + v1 + v2
            num = total % 10
            carry = total // 10

            temp.next = ListNode(num)

            temp = temp.next
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None

        return dummy.next      



        