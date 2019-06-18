from enum import Enum


class Color(Enum):
    SIMPLE = 1;
    SIMPLEWIGHTED = 2;
    SIMPLEDIRECTED = 3;
    SIMPLEDIRECTEDWIGHTED = 4;


class Graph(object):

    def __init__(self, vertexes=None, edges=None):
        self.vertexes = isinstance(vertexes, set) or set([]);
        self.edges = isinstance(edges, set) or set([]);

    def add_vertex(self, vertex):
        self.vertexes.add(vertex);

    def add_edge(self, edge):
        self.edges.add(edge);

    def remove_edge(self, edge):
        self.edges.remove(edge);

    def remove_vertex(self, vertex):
        self.edges.remove(vertex);

    def vertex_list(self):
        return list(self.vertexes);

    def edge_list(self):
        return list(self.edges);

    def neighbours_list(self, vertex):
        return list(self.neighbours_set(vertex));

    def neighbours_set(self, vertex):
        s = set([]);
        for e in self.edges:
            if vertex == e.get_source():
                s.add(e.get_target());
            if vertex == e.get_target():
                s.add(e.get_source());
        return s;

    def degree_of(self, vertex):
        l = [];
        for e in self.edges:
            if vertex == e.get_source() or vertex == e.get_target():
                l.append(e);
        return len(l);

    def contains_edge(self, edge):
        for e in self.edges:
            if e == edge:
                return True;
        return False;

    def contains_vertex(self, vertex):
        for v in self.vertexes:
            if v == vertex:
                return True;
        return False;

    def remove_edge(self, edge):
        if self.contains_edge(edge):
            self.edges.remove(edge);

    def remove_vertex(self, vertex):
        if self.contains_vertex(vertex):
            self.vertexes.remove(vertex);

    @staticmethod
    def read_graph(file, vertexsupplier, edgesupplier):
        graph = Graph();

        try:
            with open(file, 'r') as f:
                lines = f.readlines();
                i = 0;

                for line in lines:
                    line = line.strip();

                    if i == 0:
                        if "#VERTEX#" not in line:
                            raise ValueError("File format error");
                        i = 1;
                        continue;

                    if i == 1:
                        if "#EDGE#" in line:
                            i = 2;
                            continue;

                        values = line.split(',');
                        graph.add_vertex(vertexsupplier(values));

                    if i == 2:
                        values = line.split(',');
                        graph.add_edge(edgesupplier(values));

        except IOError:
            print("File does not exist");

        return graph;
