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


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        reversedL1 = self.reverseLinkedList(l1)
        reversedL2 = self.reverseLinkedList(l2)

        num1 = self.extractNumber(reversedL1)
        num2 = self.extractNumber(reversedL2)
        total = num1 + num2

        if total == 0:
            return ListNode(0)

        dummy = ListNode(0)
        temp = dummy

        while total:
            nodeValue = total % 10
            temp.next = ListNode(nodeValue)
            total = total // 10
            temp = temp.next

        return dummy.next

        