# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def mergeLists(head1, head2):
            dummy = ListNode(-1)
            temp = dummy

            while head1 and head2:
                if head1.val < head2.val:
                    temp.next = head1
                    head1 = head1.next
                else:
                    temp.next = head2
                    head2 = head2.next
                temp = temp.next
            
            if head1:
                temp.next = head1
            elif head2:
                temp.next = head2
            
            return dummy.next
        
        while len(lists) > 1:
            res = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                res.append(mergeLists(l1,l2))
            lists = res
            
        return lists[0]




         