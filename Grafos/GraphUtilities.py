import Vertex
import Graph
import Edge

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