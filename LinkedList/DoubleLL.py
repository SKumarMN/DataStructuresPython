#author: SKMN

class Node():

    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

    def __init__(self,data,prev,next):
        self.data = data
        self.prev = prev
        self.next = next

    def getNext(self):
        self.next

    def getPrev(self):
        self.prev
    
    def setNext(self,next):
        self.next = next

    def setPrev(self,prev):
        self.prev = prev

class DoubleLL():

    def __init__(self):
        
        self.head = None
        self.tail = None

    def addBeg(self,data):
        nNode = Node(data)
        if self.head == None:
            self.head = nNode
            self.tail = nNode
        else:
            nNode.setNext(self.head)
            self.head.setPrev(nNode)
            self.head = nNode

    
    def addEnd(self, data):
        nNode = Node(data)

        if self.head == None:
            self.head = nNode
            self.tail = nNode
        else:
            cur = self.head

            while(cur.getNext()!= None):
                cur = cur.getNext()
            cur.setNext(nNode)
            nNode.setPrev(cur)
            self.tail = nNode

    