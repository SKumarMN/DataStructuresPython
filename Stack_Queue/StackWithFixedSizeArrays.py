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
        
our_stack = Stack(5)
our_stack.push("1")
our_stack.push("21")
our_stack.push("14")
our_stack.push("11")
our_stack.push("31")
our_stack.push("14")
our_stack.push("15")
our_stack.push("19")
our_stack.push("3")
our_stack.push("99")
our_stack.push("9")
print( our_stack.peek())
print(our_stack.pop())
print (our_stack.peek())
print (our_stack.pop())