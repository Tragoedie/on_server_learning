import unittest
from on_server_learning.algorithms_1.trees.simple_graph import *


class Test_SimpleTree(unittest.TestCase):

    def test_all(self):
        graph = SimpleGraph(5)
        self.assertEqual(graph.max_vertex, 5)
        m_adj = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        self.assertEqual(graph.m_adjacency, m_adj)
        self.assertEqual(graph.vertex, [None, None, None, None, None])
        self.assertTrue(graph.AddVertex(1))
        self.assertEqual(graph.m_adjacency, m_adj)
        self.assertEqual(graph.vertex[0].Value, 1)
        self.assertTrue(graph.AddVertex(2))
        self.assertFalse(graph.IsEdge(0, 1))
        self.assertTrue(graph.AddEdge(0, 1))
        m_adj_1_2 = [[0, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        self.assertTrue(graph.IsEdge(0, 1))
        self.assertEqual(graph.m_adjacency, m_adj_1_2)
        self.assertTrue(graph.AddVertex(3))
        self.assertTrue(graph.AddVertex(4))
        self.assertTrue(graph.AddVertex(5))
        self.assertFalse(graph.AddVertex(6))
        self.assertTrue(graph.AddEdge(0, 0))
        self.assertTrue(graph.AddEdge(0, 2))
        self.assertTrue(graph.AddEdge(0, 3))
        self.assertTrue(graph.AddEdge(0, 4))
        self.assertFalse(graph.AddEdge(0, 5))
        m_adj_1_all = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]]
        self.assertEqual(graph.m_adjacency, m_adj_1_all)
        self.assertTrue(graph.AddEdge(2, 4))
        self.assertTrue(graph.AddEdge(4, 1))
        self.assertTrue(graph.AddEdge(3, 2))
        m_adj_1_other = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 1, 1], [1, 0, 1, 0, 0], [1, 1, 1, 0, 0]]
        self.assertEqual(graph.m_adjacency, m_adj_1_other)
        self.assertTrue(graph.RemoveVertex(0))
        self.assertEqual(graph.vertex[0], None)
        m_adj_1_del = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 1, 1], [0, 0, 1, 0, 0], [0, 1, 1, 0, 0]]
        self.assertEqual(graph.m_adjacency, m_adj_1_del)
        self.assertFalse(graph.IsEdge(0, 1))
        self.assertTrue(graph.IsEdge(2, 4))
        self.assertTrue(graph.RemoveEdge(2, 4))
        self.assertFalse(graph.IsEdge(2, 4))
        self.assertTrue(graph.RemoveVertex(1))
        self.assertTrue(graph.RemoveVertex(2))
        self.assertTrue(graph.RemoveVertex(3))
        self.assertTrue(graph.RemoveVertex(4))
        self.assertEqual(graph.m_adjacency, m_adj)
        self.assertEqual(graph.vertex, [None, None, None, None, None])


if __name__ == '__main__':
    unittest.main()
