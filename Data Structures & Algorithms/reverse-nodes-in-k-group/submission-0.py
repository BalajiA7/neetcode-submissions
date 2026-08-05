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
        i = 0
        nodes = []

        while i < length:
            temp = curr
            prev = None
            j = 0
            # pick k nodes
            while j < k and temp:
                j+=1
                prev = temp
                temp = temp.next
            prev.next = None

            # if k nodes reverse it and add it to the result array
            if  j == k:
                revHead = self.reverseGroup(curr)
                print(length, j, k, "revHead", revHead.val)
                nodes.append(revHead)
            #else nodes are < k so add it without reverse 
            else:
                print(length, j, k, "currHead", curr.val)
                nodes.append(curr)

            # temp becomes the next start node
            curr = temp
            i+=k
        
        # join the k reversed node
        for idx, node in enumerate(nodes):
            print(node, idx)
            # go to the last node in the nogroup
            lastNode = node
            while lastNode and lastNode.next != None:    
                print(lastNode.val)
                lastNode = lastNode.next
            print(lastNode)
            lastNode.next = nodes[idx+1] if (idx+1) < len(nodes) else None
        
        return nodes[0]

        

        

        