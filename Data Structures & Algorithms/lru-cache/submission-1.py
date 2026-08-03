class Node:
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.hashMap = {}
        self.capacity = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def delNode(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

    def insertAtHead(self, node):
        headNext = self.head.next
        #inserting node at head
        self.head.next = node
        node.prev = self.head
        node.next = headNext
        headNext.prev = node

    def get(self, key: int) -> int:
        if key in self.hashMap:
            node = self.hashMap[key]
            # recently used so move to head
            self.delNode(node)
            self.insertAtHead(node)
            return node.value
        else:
            return -1
       

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            node = self.hashMap[key]
            node.value = value
            # recently used so move to head
            self.delNode(node)
            self.insertAtHead(node)
        else:
            if len(self.hashMap) == self.capacity:
                # remove Least used node from hashmap and list
                node = self.tail.prev
                self.delNode(node)
                del self.hashMap[node.key]
            
            node = Node(key, value)
            self.hashMap[key] = node
            #Insert at head
            self.insertAtHead(node)


        

        
