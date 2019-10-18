class Graph(object):
    WHITE, GRAY, BLACk = range(3)

    def __init__(self):
        self.color = Graph.WHITE
        self.edges = list()

    def has_cycle(self, src):
        if src.color == Graph.GRAY:
            return True
        src.color = Graph.GRAY

        if any(v.color != Graph.BLACk and self.has_cycle(v) for v in src.edges):
            return True
        src.color = Graph.BLACk
        return False

    def is_cyclic(self, graph):
        return any(v.color == Graph.WHITE and self.has_cycle(v) for v in graph)


if __name__ == '__main__':
    n = 3
    G = [Graph() for i in range(n)]

    G[0].edges.append(G[1])
    G[0].edges.append(G[2])
    G[2].edges.append(G[1])
    G[1].edges.append(G[2])

    #
    # for i in range(1, n):
    #     G[i - 1].edges.append(G[i])
    #     print(G[i - 1].color)

    print(Graph().is_cyclic(G))
