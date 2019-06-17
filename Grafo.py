from enum import Enum


class Color(Enum):
    SIMPLE = 1;
    SIMPLEWIGHTED = 2;
    SIMPLEDIRECTED = 3;
    SIMPLEDIRECTEDWIGHTED = 4;


class Graph(object):

    def __init__(self, vertexes=None, edges=None):
        self.vertexes = isinstance(vertexes, list) or [];
        self.edges = isinstance(edges, list) or [];

    def add_vertex(self, vertex):
        self.vertexes.append(vertex);

    def add_edge(self, edge):
        self.edge.append(edge);

    @staticmethod
    def read_graph(file, vertexsupplier, edgesupplier):
        graph = Graph();

        try:
            with open(file, 'r') as f:
                f.read();
                lines = f.readlines();
                i = 0;

                for line in lines:
                    if i == 0:
                        if "#VERTEXES#" not in line:
                            raise ValueError("File format error");
                        i = 1;
                        continue;

                    if i == 1:
                        if "#EDGES#" in line:
                            i = 2;
                            continue;

                        values = line.split(',');
                        graph.add_vertex(vertexsupplier(values[0], values[1:]));

                    if i == 2:
                        values = line.split(',');
                        graph.add_edge(edgesupplier(values[0], values[1:]));

        except IOError:
            print("File does not exist");

        return graph;
