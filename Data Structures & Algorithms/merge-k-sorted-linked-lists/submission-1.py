# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeList(self, l1:ListNode,l2:ListNode):
        dummy = ListNode()
        temp = dummy

        while l1 and l2:
            if l1 and l2:
                if l1.val <= l2.val:
                    temp.next = l1
                    l1 = l1.next
                else:
                    temp.next = l2
                    l2 = l2.next
                temp = temp.next
                
        if l1:
            temp.next = l1
        else:
            temp.next = l2

        return dummy.next    

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        for i in range(1, len(lists)):
            sortedList = self.mergeList(lists[i-1], lists[i])
            lists[i] = sortedList
        
        return lists[-1] if len(lists) else None




        