from queue import Queue
from graph import *


def bfs(graph, start=0):
    queue = Queue()
    queue.put(start)
    visited = set()
    while not queue.empty():
        node = queue.get()

        if node in visited:
            continue

        print("Vertex", node)
        visited.add(node)

        for v in graph.get_adjacent_vertex(node):
            if v not in visited:
                queue.put(v)

def dfs(graph,visited,current=0):
    if(visited[current]==1):
        return
    
    visited[current]=1

    print(current)

    for v in graph.get_adjacent_vertex(current):
        dfs(graph,visited,v)

g = AdjacencyMatrixGraph(6,False)

g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(2,3)
g.add_edge(2,1)
g.add_edge(1,4)
g.add_edge(4,5)
g.add_edge(3,5)


g.display()
bfs(g,5)
visited = [0]*6
dfs(g,visited)