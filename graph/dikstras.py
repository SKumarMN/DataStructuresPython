import priority_dict

from graph import AdjacencyMatrixGraph



def build_dist_table(graph, source):

    dist_table={}

    for i in range(graph.numVertices):
        dist_table[i]=(None, None)
    
    dist_table[source]=(0,source)

    pq = priority_dict.priority_dict()

    pq[source] = 0

    while( len(pq.keys() )>0):

        cur_ver = pq.pop_smallest()

        cur_dist = dist_table[cur_ver][0]

        for neighbour in graph.get_adjacent_vertex(cur_ver):

            new_weight = cur_dist + int(graph.get_edge_weight(cur_ver,neighbour))
            distance = dist_table[neighbour][0]
            if  distance is None or distance > new_weight:
                pq[neighbour]=new_weight
                dist_table[neighbour]= (new_weight, cur_ver)

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


g = AdjacencyMatrixGraph(8, True)

g.add_edge(0,1,1)
g.add_edge(1,2,2)
g.add_edge(1,3,6)
g.add_edge(2,3,2)
g.add_edge(1,4,3)
g.add_edge(3,5,1)
g.add_edge(5,4,5)
g.add_edge(3,6,1)
g.add_edge(6,7,1)
g.add_edge(0,7,8)

shortest_path(g,0,6)
shortest_path(g,4,7)
shortest_path(g,7,0)