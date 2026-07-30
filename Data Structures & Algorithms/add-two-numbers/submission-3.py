# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseLinkedList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next     
        return prev
    
    def extractNumber(self, head:ListNode) -> Number:
        num = 0
        curr = head
        while curr:
            num = num * 10 + curr.val
            curr = curr.next
        return num
    
    def extractNumCarry(self, carry, num1, num2):
        total = carry + curr1.val + curr2.val
        num = total % 10
        carry = total // 10
        return [num, carry]


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        curr1, curr2 = l1,l2
        dummy = ListNode()
        temp = dummy

        while curr1 and curr2:
            total = carry + curr1.val + curr2.val
            num = total % 10
            carry = total // 10

            temp.next = ListNode(num)
            curr1 = curr1.next
            curr2 = curr2.next
            temp = temp.next
        
        while curr1:
            total = carry + curr1.val
            num = total % 10
            carry = total // 10

            temp.next = ListNode(num)
            curr1 = curr1.next
            temp = temp.next
        
        while curr2:
            total = carry + curr2.val
            num = total % 10
            carry = total // 10

            temp.next = ListNode(num)
            curr2 = curr2.next
            temp = temp.next
        
        if carry:
            temp.next = ListNode(carry)

        return dummy.next      



        