class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size  # максимальное количество вершин
        self.m_adjacency = [[0] * size for _ in range(size)]  # матрица смежности
        self.vertex = [None] * size  # список вершин

    def AddVertex(self, v):
        if None in self.vertex:
            self.vertex[self.vertex.index(None)] = Vertex(v)
            return True
        return False
        # здесь и далее, параметры v -- индекс вершины

    def RemoveVertex(self, v):
        if v > self.max_vertex - 1 or self.vertex[v].Value is None:
            return False
        for i in range(len(self.m_adjacency[v])):
            self.RemoveEdge(v, i)
        self.vertex[v] = None
        return True

    def IsEdge(self, v1, v2):
        if v1 > self.max_vertex - 1 or v2 > self.max_vertex - 1:
            return False
        return self.m_adjacency[v1][v2] == 1 and self.m_adjacency[v2][v1] == 1

    def AddEdge(self, v1, v2):
        if v1 > self.max_vertex - 1 or v2 > self.max_vertex - 1:
            return False
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1
        return True

    def RemoveEdge(self, v1, v2):
        if v1 > self.max_vertex - 1 or v2 > self.max_vertex - 1:
            return False
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0
        return True

    def DepthFirstSearch(self, VFrom, VTo):
        if VFrom < 0 or VFrom > self.max_vertex - 1 or VTo < 0 or VTo > self.max_vertex - 1:
            return []
        stack_graph = []
        for v in self.vertex:
            v.Hit = False
        self.vertex[VFrom].Hit = True
        stack_graph.append(VFrom)
        while stack_graph != [] and stack_graph[-1] != VTo:
            xchange = False
            for i in range(self.max_vertex):
                if self.m_adjacency[stack_graph[-1]][i] == 1 and self.vertex[i].Hit is False:
                    stack_graph.append(i)
                    self.vertex[i].Hit = True
                    xchange = True
            if xchange is False:
                del stack_graph[-1]
        result = [self.vertex[i] for i in stack_graph]
        return result
