from graph.graph import Graph
from graph.graph_node import GraphNode


class GraphBuilder:
    def __init__(self):
        self.node_list: dict[str, GraphNode] = dict()
        
    def build(self, graph: dict) -> Graph:
        for key, values in graph.items():
            if not key in self.node_list:
                self.node_list[key] = GraphNode(key)
            for value in values:
                if not value in self.node_list:
                    self.node_list[value] = GraphNode(value)
                self.node_list[key].append_to_adjacent_nodes(self.node_list[value])
        return Graph(self.node_list.values())