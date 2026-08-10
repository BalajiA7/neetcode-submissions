class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        # inital setup of doubly linked list
        self.dummyLeft = Node(0,0)
        self.dummyRight = Node(0,0)
        self.dummyLeft.next = self.dummyRight
        self.dummyRight.prev = self.dummyLeft
        self.capacity = capacity
        self.hashMap = {}
    
    def deleteNode(self, node):
        # get prev and next 
        prevNode = node.prev
        nextNode = node.next
        # change pointers
        prevNode.next = nextNode
        nextNode.prev = prevNode
    
    def addNode(self, node):
        # add to the right
        lastNode = self.dummyRight.prev
        lastNode.next = node
        node.prev = lastNode
        #link node right to dummyRight
        node.next = self.dummyRight
        self.dummyRight.prev = node

    def get(self, key: int) -> int:
        if key in self.hashMap:
            self.deleteNode(self.hashMap[key])
            self.addNode(self.hashMap[key])
            return self.hashMap[key].value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.hashMap:
            newNode = Node(key, value)
            self.hashMap[key] = newNode
            self.addNode(newNode)
        else:
            self.hashMap[key].value = value
            self.deleteNode(self.hashMap[key])
            self.addNode(self.hashMap[key])

        if len(self.hashMap) > self.capacity:
            # delete from the left
            delNode = self.dummyLeft.next
            print(delNode.key, self.hashMap)
            del self.hashMap[delNode.key]
            self.deleteNode(delNode)


        
