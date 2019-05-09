from queue import Queue

from graph import *


def topo_sort(graph):

    indegree ={}
    visited =[]
    queue = Queue()

    for i in range(graph.numVertices):
        indegree[i]= graph.get_indegree(i)

        if indegree[i] ==0:
            queue.put(i)

    while  not queue.empty():
        vertex = queue.get()
        visited.append(vertex)

        for v in graph.get_adjacent_vertex(vertex):
            indegree[v] -= 1
            if indegree[v] ==0:
                queue.put(v)

    if(len(visited) != graph.numVertices):
        raise ValueError("Graph has cycle")
    
    print(visited)



g = AdjacencyMatrixGraph(9,True)

g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(2,7)
g.add_edge(2,3)
g.add_edge(2,4)

g.add_edge(1,5)
g.add_edge(5,6)
g.add_edge(3,6)
g.add_edge(3,4)
g.add_edge(6,8)
topo_sort(g)
#g.display()      
