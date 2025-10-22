# Build Order: You are given a list of projects and a list of dependencies 
# (which is a list of pairs of projects, where the second project is dependent 
# on the first project). All of a project's dependencies must be built before the project is. Find a build order that will allow the projects to be built. If there is no valid build order, return an error.
# EXAMPLE
# Input:
# projects: a, b, c, d, e, f
# dependencies: (a, d), (f, b), (b, d), (f, a), (d, c) Output: f, e, a, b, d, c

from collections import deque

def construct_adjacency_list(
    nodes: list[str], 
    dependencies: list[list[str]]
) -> dict[str, list[str]]:
    adj: dict[str, list[str]] = {node: [] for node in nodes}
    for u, v in dependencies:
        adj[u].append(v)
    return adj

def get_indegree(nodes: list[str], adj: dict[str, list[str]]) -> dict[str, int]:
    indegree: dict[str, int] = {node: 0 for node in nodes}
    for deps in adj.values():
        for node in deps:
            indegree[node] += 1
    return indegree

def topological_sort(
    nodes: list[str],
    dependencies: list[list[str]]
) -> list[str]:
    adj = construct_adjacency_list(nodes, dependencies)
    indegree: dict[str, int] = get_indegree(nodes, adj)
    
    q = deque()
    order = []
    
    for node, degree in indegree.items():
        if degree == 0:
            q.append(node)
        
    while q:
        node = q.popleft()
        order.append(node)
        for d_node in adj[node]:
            indegree[d_node] -= 1
            if indegree[d_node] == 0:
                q.append(d_node)
    
    if len(order) != len(nodes):
        raise ValueError("The input graph is cyclic")
    
    return order


if __name__ == "__main__":
    nodes = ['a', 'b', 'c', 'd', 'e', 'f']
    edges = [['a', 'd'], ['f', 'b'], ['b', 'd'], ['f', 'a'], ['d', 'c']]

    result = topological_sort(nodes, edges)
    if result:
        print("Topological Order:", result)