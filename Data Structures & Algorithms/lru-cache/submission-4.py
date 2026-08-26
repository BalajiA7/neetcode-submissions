class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashMap = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def delNode(self,node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
    
    def insertNode(self,node):
        tail = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = tail
        tail.prev = node

    def get(self, key: int) -> int:
        if key in self.hashMap:
            node = self.hashMap[key]
            # delte node
            self.delNode(node)
            # insert node
            self.insertNode(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            # key already present update value and move to front
            node = self.hashMap[key]
            node.val = value
            self.delNode(node)
            self.insertNode(node)
        else:
            node = Node(key, value)
            self.hashMap[key] = node
            # insert to the head
            self.insertNode(node)

            # if the list reaches the capacity
            if len(self.hashMap) > self.capacity:
                # delte the LRU Node
                node = self.tail.prev
                del self.hashMap[node.key]
                self.delNode(node)

        
