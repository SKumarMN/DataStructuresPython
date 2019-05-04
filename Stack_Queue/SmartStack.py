class SmartStack():
    def __init__(self):
        self.data = []
        self.min=[]
    
    def stack_push(self,item):
        self.data.push(item)
        if not self.min or item <= self.min[-1]:
            self.min.append(item)
        else:
            self.min.append(self.min[-1])
    
    def stack_pop(self):
        x= self.data.pop()
        self.min.pop()
        return x
        
    