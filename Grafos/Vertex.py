class Vertex(object):

    def __init__(self, args):
        self.name = str(args[0]);

    def __str__(self):
        s = str(self.name);
        return s;

    def __repr__(self):
        s = str(self.name);
        return s;

    def __eq__(self, other):
        return self.name == other.name;

    def __hash__(self):
        return hash(self.name);

    @staticmethod
    def create(args):
        return Vertex(args);
