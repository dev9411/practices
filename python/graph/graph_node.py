class GraphNode:
    def __init__(self, value: str):
        self.value = value
        self.adjacent_nodes: list[GraphNode] = []
        self.visited = False

    def visit(self):
        print('->', self.value)
        self.visited = True

    def append_to_adjacent_nodes(self, node: 'GraphNode') -> None:
        self.adjacent_nodes.append(node)