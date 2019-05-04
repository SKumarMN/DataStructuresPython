class Stack(object):
    def __init__(self, limit=5):
       self.data = []
       self.limit=5
    
    def is_empty(self):
        return len(self.data) <=0

    def push(self,item):
        if len(self.data ) >= self.limit:
            print("Stack overflow")
        else:
            self.data.append(item)
    
    def pop(self):
        if len(self.data ) <=0:
            print("Stack underflow")
        else:
            return self.data.pop()

    def peek(self):
        if len(self.data ) <=0:
            print("Stack underflow")
        else:
            return self.data[-1]
        
        