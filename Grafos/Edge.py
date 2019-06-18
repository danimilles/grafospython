from Vertex import *


class Edge(object):

    def __init__(self, args):
        self.source = Vertex.create(args);
        self.target = Vertex.create(args[1:]);
        self.weight = int(args[2]);

    def get_source(self):
        return self.source;

    def get_target(self):
        return self.target;

    def __str__(self):
        s = "(" + str(self.source) + ", " + str(self.target) + ")";
        return s;

    def __repr__(self):
        s = "(" + str(self.source) + ", " + str(self.target) + ", " + str(self.weight) + ")";
        return s;

    def __eq__(self, other):
        return self.source == other.source and self.target == other.target and self.weight == other.weight;

    def __hash__(self):
        return hash(str(self.source) + str(self.target) + str(self.weight));

    @staticmethod
    def create(args):
        return Edge(args);
