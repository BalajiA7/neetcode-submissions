# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head

        while curr:
            curr = curr.next
            length+=1
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        targetIdx,currIdx = length - n, 0
        curr = head
        print("length", length,targetIdx)
        
        while curr:
            print("currIdx", currIdx)
            if currIdx == targetIdx:
                # if prev:
                    print("Prev", prev.val, curr.val)
                    prev.next = curr.next
                    # curr.next = None
                # else:
                #     temp = curr
                #     curr = curr.next
                #     temp.next = None
                    break
            prev = curr
            curr = curr.next
            currIdx+=1
        
        return dummy.next

