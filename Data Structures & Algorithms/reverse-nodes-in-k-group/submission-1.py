# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseGroup(self, head):
        prevNode = None
        curr = head
        while curr:
            nextNode = curr.next
            curr.next = prevNode
            prevNode = curr
            curr = nextNode
        return prevNode

    def lengthofLinkedList(self, head):
        length = 0 
        curr = head
        while curr:
            length+=1
            curr = curr.next
        return length

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = self.lengthofLinkedList(head)
        curr = head
        prevGroupPrev = None
        i = 0

        while i < length:
            groupHead = curr
            currGroupPrev = None
            j = 0

            # Move to K nodes
            while j < k and groupHead:
                j+=1
                currGroupPrev = groupHead
                groupHead = groupHead.next

            # Disconnect current group
            currGroupPrev.next = None

            # if k nodes reverse it and add it to the result array
            if  j == k:
                reversedHead = self.reverseGroup(curr)
                if prevGroupPrev:
                    prevGroupPrev.next = reversedHead
                else:
                    head = reversedHead

                curr.next = groupHead
                prevGroupPrev = curr

            # Move to next group
            curr = groupHead
            i+=k
        
        return head
        

        

        