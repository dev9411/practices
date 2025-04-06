from graph.graph_node import GraphNode


class Graph:
    def __init__(self, nodes: list[GraphNode]) -> None:
        self.nodes: list[GraphNode] = nodes
        
    def depth_first_traverse(self) -> None:
        for node in self.nodes:
            self._depth_traverse(node)
    
    def depth_first_search(self, key: str) -> bool:
        for node in self.nodes:
            if self._depth_search(node, key):
                return True
        return False

    def _depth_traverse(self, node: GraphNode) -> None:
        if node.visited:
            return
        node.visit()
        for next_node in node.adjacent_nodes:
            self._depth_traverse(next_node)

    def _depth_search(self, node: GraphNode, key: str) -> bool:
        if node.visited:
            return False
        if key == node.value:
            return True
        node.visit()
        for next_node in node.adjacent_nodes:
            if self._depth_search(next_node, key):
                return True
        return False
