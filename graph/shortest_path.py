from queue import Queue

from graph_withset import *



def build_dist_table(graph, source):

    dist_table ={}

    for i in range(graph.numVertices):
        dist_table[i]=(None, None)

    dist_table[source]=(0,source)

    queue = Queue()
    queue.put(source)

    while not queue.empty():

        cur_vertex = queue.get()

        cur_dist = dist_table[cur_vertex][0]

        for i in graph.get_adjacent_vertices(cur_vertex):
            
            if dist_table[i][0] is None:
                queue.put(i)
                dist_table[i]= (cur_dist + 1, cur_vertex)

    return dist_table

def shortest_path(graph, source, destination):
    dist_table = build_dist_table(graph,source)
    path = [destination]

    prev_vertex = dist_table[destination][1]

    while prev_vertex is not None and prev_vertex != source:
        path= [prev_vertex] + path

        prev_vertex = dist_table[prev_vertex][1]

    if prev_vertex is None:
        print("No Path Exists")

    else:
        print("Path is ", [source]+ path)


g = AdjacencySetGraph(8, True)

g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(1,4)
g.add_edge(3,5)
g.add_edge(5,4)
g.add_edge(3,6)
g.add_edge(6,7)
g.add_edge(0,7)

shortest_path(g,0,5)
shortest_path(g,0,6)
shortest_path(g,7,4)



