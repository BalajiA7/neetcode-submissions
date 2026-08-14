# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(0, head)
        
        # find the mid prev
        slow = dummy
        fast = dummy

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # seperate the linked list and reverse the second block
        head1 = slow.next
        slow.next = None

        prevNode = None
        currNode = head1
        while currNode:
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
        
        # Join the two lists
        head1 = prevNode
        while head and head1:
            dummy.next = head
            head = head.next
            dummy = dummy.next
        
            dummy.next = head1
            head1 = head1.next
            dummy = dummy.next
        
        if head1:
            dummmy.next = head1
        elif head:
            dummy.next = head

        