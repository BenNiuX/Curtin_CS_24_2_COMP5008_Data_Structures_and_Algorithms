import unittest

from DSAGraph import DSAGraph


class TestGraph(unittest.TestCase):
    """
    Test the graph class.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test(self):
        """
        Function to test the graph class.
        """
        graph = DSAGraph()
        graph.displayAsList()
        graph.displayAsMatrix()
        self.assertEqual(graph.getVertexCount(), 0)
        self.assertEqual(graph.getEdgeCount(), 0)
        graph.addVertex("A")
        graph.addVertex("B")
        graph.displayAsList()
        graph.displayAsMatrix()
        self.assertIsNotNone(graph.getVertex("A"))
        self.assertIsNotNone(graph.getVertex("B"))
        self.assertEqual(graph.getVertexCount(), 2)
        self.assertFalse(graph.isPath("A", "B"))
        graph.addEdge("A", "B", 10)
        graph.displayAsList()
        graph.displayAsMatrix()
        self.assertEqual(graph.getEdgeCount(), 1)
        self.assertTrue(graph.isPath("A", "B"))
        graph.addEdge("A", "C", 20)
        graph.displayAsList()
        graph.displayAsMatrix()
        self.assertTrue(graph.isPath("A", "C"))
        self.assertTrue(graph.isPath("C", "B"))
        self.assertTrue(graph.getVertexCount(), 3)
        self.assertTrue(graph.getEdgeCount(), 2)
        self.assertIsNotNone(graph.getVertex("C"))
        graph.addEdge("B", "C", 30)
        graph.displayAsList()
        graph.displayAsMatrix()
        self.assertEqual(graph.getEdgeCount(), 3)
        self.assertTrue(graph.isPath("C", "B"))
        graph.deleteEdge("B", "C")
        graph.displayAsList()
        graph.displayAsMatrix()
        self.assertEqual(graph.getEdgeCount(), 2)
        self.assertTrue(graph.isPath("C", "B"))
        graph.deleteVertex("C")
        graph.displayAsList()
        graph.displayAsMatrix()
        self.assertEqual(graph.getVertexCount(), 2)
        self.assertEqual(graph.getEdgeCount(), 1)
        graph.sort()
        graph.depthFirstSearch()
        graph.breadthFirstSearch()


if __name__ == '__main__':
    unittest.main()
