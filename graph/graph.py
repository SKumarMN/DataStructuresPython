import abc
import numpy as np


class Graph(abc.ABC):

    def __init__(self, numVertices, directed= False):
        self.numVertices = numVertices
        self.directed = directed
    
    @abc.abstractmethod
    def add_edge( self, v1, v2, weight=1):
        pass

    @abc.abstractmethod
    def get_adjacent_vertex(self, v):
        pass

    @abc.abstractmethod
    def get_indegree(self, v):
        pass

    @abc.abstractmethod
    def get_edge_weight(self, v1, v2):
        pass

    @abc.abstractmethod
    def display(self):
        pass


class AdjacencyMatrixGraph(Graph):

    def __init__(self, numVertices, directed=False):
        super().__init__(numVertices, directed=directed)
        self.matrix = np.zeros((numVertices,numVertices))

    def add_edge(self, v1, v2, weight=1):

        if(v1 >= self.numVertices or v2 >=self.numVertices or v1 <0 or v2 <0):
            raise ValueError("Invalid vertices")
        

        if(weight < 1):
            raise ValueError("Invalid weight")

        self.matrix[v1][v2] = weight
        if(self.directed) ==False:   
            self.matrix[v2][v1] = weight

        
    def get_adjacent_vertex(self, v):
        
        if(v >=self.numVertices or v <0 ):
           raise ValueError("Invalid vertex %d" % v )

        adjacent_vertices=[]

        for i in range(self.numVertices):
            if self.matrix[v][i] >0:
                adjacent_vertices.append(i)

        return adjacent_vertices

    
    def get_indegree(self, v):
        
        if(v >=self.numVertices or v <0 ):
           raise ValueError("Invalid vertex %d" % v )

        count =0
        for i in range(self.numVertices):
            if self.matrix[i][v]>0:
                count +=1

        return count

    def get_edge_weight(self, v1, v2):
        return self.matrix[v1][v2]

    def display(self):
        
        for i in range(self.numVertices):
            for v in self.get_adjacent_vertex(i):
                print(i, "-->", v)

   
if __name__=='main':
    g = AdjacencyMatrixGraph(4,True)

    g.add_edge(0,1)
    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(2,3)

    g.display()
    