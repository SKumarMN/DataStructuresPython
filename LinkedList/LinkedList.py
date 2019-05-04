#author: SKMN

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    def getNext(self):
        return self.next
    def setNext(self,next):
        self.next = next



class LinkedList(object):

    def __init__(self):
        self.length = 0
        self.head = None

    def addBeg(self, data):
        node = Node(data)
        
        if self.length == 0:
            self.head = node
        else:
            node.setNext(self.head)
            self.head = node
        self.length +=1

    def addEnd(self,data):
        node = Node(data)

        curr = self.head
        while( curr.getNext() != None):
            curr = curr.getNext()
        curr.setNext(node)
        self.length +=1

    def addAtPos( self, data,pos):
        if pos > self.length or pos < 0:
            return None
        else:
            if pos ==0:
                self.addBeg(data)
            elif pos == self.length:
                 self.addEnd(data)
            else:
                cur = self.head
                node = Node(data)
                count = 1
                while count< pos:
                    count +=1
                    cur = cur.getNext()
                node.setNext(cur.getNext())
                cur.setNext(node)
                self.length +=1
                

    def delBeg(self):
        if self.length ==0:
            return None
        self.head = self.head.getNext()
        self.length -=1

    def delEnd(self):
        if self.length ==0:
            return None
        else:
            cur = self.head
            prev = self.head
            while cur.getNext() != None:
                prev = cur
                cur = cur.getNext()
            prev.setNext(None)
            self.length -=1

    def delAtPos(self,pos):
        if pos > self.length or pos < 0:
            return None
        else:
            if pos ==0:
                 self.delBeg()
            elif pos == self.length:
                 self.delEnd()
            else:
                cur = self.head
                count = 1
                while count < pos:
                    count +=1
                    cur = cur.getNext()
                cur.setNext(cur.getNext().getNext())

    def printList(self):

        cur = self.head

        while( cur != None):
            print(cur.data)
            cur = cur.getNext()

    def delNthNodeFromLast(self, n):
        if n < 0:
            return None

        temp = self.head

        count =1
        while count < n and None != temp:
            count +=1
            temp= temp.getNext()
        
        if count < n or None == temp:
            return None
        
        nth= self.head

        while temp.next != None:
            temp = temp.next
            nth = nth.next
        return nth.data
    def detect_cycle(self):
        slow = self.head
        fast = self.head

        while( slow and fast ):
            fast = fast.getNext()
            if slow == fast:
                return True
            if fast == None:
                return False

            fast = fast.getNext()
            if slow == fast:
                print(slow.data)
                return True   
            slow = slow.getNext()
    def orderInsert(self, data):
        cur = self.head
        prev = None

        while cur!= None and cur.data < data:
            prev = cur
            cur = cur.getNext()

        node = Node(data)
        if prev == None:
            self.head = node
            node.setNext(cur)
        else:
            prev.setNext(node)
            node.setNext(cur)
        
        
    
if __name__ == "__main__":

    ll = LinkedList()
    #ll.addBeg(1)
    #ll.addEnd(2)

    #ll.addEnd(4)
    #ll.addEnd(5)
    #ll.addEnd(6)
    #ll.addAtPos(0,0)
    #ll.addAtPos(7,6)
    #ll.addAtPos(3,3)
    ll.orderInsert(0)
    ll.orderInsert(3)
    ll.printList()
    ll.delBeg()
    ll.delEnd()
    ll.delAtPos(1)
    ll.printList()
    print(ll.delNthNodeFromLast(2))
    print(ll.detect_cycle())

    ll2 = LinkedList()
    ll2.addBeg(1)
    ll2.addEnd(2)
    ll2.addEnd(3)
    ll2.addEnd(4)
    ll2.head.next.next.next.next=ll2.head
    print(ll2.detect_cycle())


        