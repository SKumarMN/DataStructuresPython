class PriorityQueue(object):

    def __init__(self, items =[]):
        self.items =[]

        for index in items:
            self.items.append(index)
            self.__floatUp(index)

    pass