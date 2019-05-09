import abc

class Graph(abc.ABC):

    def __init__(self, numVertices, directed=False):
        self.numVertices = numVertices
        self.directed = directed

    @abc.abstractmethod
    def add_edge(self, v1, v2, weight=1):
        pass

    @abc.abstractmethod
    def get_adjacent_vertices(self, v):
        pass
    
    @abc.abstractmethod
    def get_indegree(self,v):
        pass
    
    @abc.abstractmethod
    def display(self):
        pass



class Node:
    def __init__(self, vertexId):
        self.vertexId = vertexId
        self.adjaceny_set = set()

    def add_edge(self, vertexId):
        if self.vertexId !=vertexId:
            self.adjaceny_set.add(vertexId)
        else:
            raise ValueError("You cannot pass the same vertex")

    def get_adjacent_vertices(self):
        return sorted(self.adjaceny_set)


        



class AdjacencySetGraph(Graph):

    def __init__(self, numVertices, directed=False):
        super().__init__(numVertices, directed=directed)

        self.vertices = []
        for i in range(self.numVertices):
            self.vertices.append(Node(i))    
    
    def add_edge(self, v1, v2, weight=1):
        if(v1 >= self.numVertices or v2 >=self.numVertices or v1 <0 or v2 <0):
            raise ValueError("Invalid vertices")

        if(weight != 1):
            raise ValueError("Invalid weight")     

        self.vertices[v1].add_edge(v2)

        if self.directed ==False:
            self.vertices[v2].add_edge(v1)


    def get_adjacent_vertices(self, v):
        return self.vertices[v].get_adjacent_vertices()

    
    def get_indegree(self, v):
        
        count=0

        for i in range(self.numVertices):
            if v in self.get_adjacent_vertices(i):
                count +=1
        return count

    def display(self):
        
        for i in range(self.numVertices):
            for v in self.get_adjacent_vertices(i):
                print(i ," -- >", v)


g = AdjacencySetGraph(4,True)

g.add_edge(0,1)

g.add_edge(0,2)
g.add_edge(2,3)
print(g.get_indegree(0))
g.display()