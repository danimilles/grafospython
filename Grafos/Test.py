from Graph import *;
from Vertex import *;
from Edge import *

def aslist(args):
    return frozenset(args);


graph1 = Graph.read_graph("testgraph.txt",Vertex.create,Edge.create)
print(graph1.vertexes)
print(graph1.edges)
print(graph1.remove_vertex(Vertex.create(['Sitio5'])));
print(graph1.vertexes)
