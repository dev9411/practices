import unittest

from graph.graph import Graph
from graph.graph_builder import GraphBuilder


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph_builder = GraphBuilder()
        
    def test_graph_builder(self):
        graph_list = {
            '1': ['2', '3', '7'],
            '2': ['3'],
            '3': ['4', '6'],
            '4': [],
            '5': [],
            '6': ['5'],
            '7': []
        }
        graph = self.graph_builder.build(graph_list)
        graph.depth_first_traverse()
        
    def test_graph_depth_first_search(self):
        graph_list = {
            '1': ['2', '3', '7'],
            '2': ['3'],
            '3': ['4', '6'],
            '4': [],
            '5': [],
            '6': ['5'],
            '7': []
        }
        graph = self._build_new_graph(graph_list)
        self.assertTrue(graph.depth_first_search('7'))
        graph = self._build_new_graph(graph_list)
        self.assertTrue(graph.depth_first_search('6'))
        graph = self._build_new_graph(graph_list)
        self.assertTrue(graph.depth_first_search('5'))
        graph = self._build_new_graph(graph_list)
        self.assertTrue(graph.depth_first_search('4'))
        graph = self._build_new_graph(graph_list)
        self.assertTrue(graph.depth_first_search('3'))
        graph = self._build_new_graph(graph_list)
        self.assertTrue(graph.depth_first_search('2'))
        graph = self._build_new_graph(graph_list)
        self.assertTrue(graph.depth_first_search('1'))
        graph = self._build_new_graph(graph_list)
        self.assertFalse(graph.depth_first_search(''))
        graph = self._build_new_graph(graph_list)
        self.assertFalse(graph.depth_first_search('12'))
        graph = self._build_new_graph(graph_list)
        self.assertFalse(graph.depth_first_search('8'))
        graph = self._build_new_graph(graph_list)
        self.assertFalse(graph.depth_first_search('-1'))
        graph = self._build_new_graph(graph_list)
        self.assertFalse(graph.depth_first_search('qwe'))
        graph = self._build_new_graph(graph_list)
        self.assertFalse(graph.depth_first_search('11'))

    def _build_new_graph(self, graph_list: dict) -> Graph:
        self.graph_builder = GraphBuilder()
        return self.graph_builder.build(graph_list)
