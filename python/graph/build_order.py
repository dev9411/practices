# Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of projects, where the second project is dependent on the first project). All of a project's dependencies must be built before the project is. Find a build order that will allow the projects to be built. If there is no valid build order, return an error.
# EXAMPLE
# Input:
# projects: a, b, c, d, e, f
# dependencies: (a, d), (f, b), (b, d), (f, a), (d, c) Output: f, e, a, b, d, c

from collections import deque
from typing import Deque


class Project:
    def __init__(self, value: str, dependent_projects: list['Project'] | None = None) -> None:
        self.value: str = value
        self.dependent_projects: list['Project'] = dependent_projects or []
        
    def set_dependent_projects(self, dependent_projects: list['Project']) -> None:
        self.dependent_projects = dependent_projects

class DFS:
    def __init__(self) -> None:
        self.visited: dict[str, bool] = {}
        self.output_stack: Deque[str] = deque()
        self.is_cyclic = False
        self.cycle_tracker: dict[str, bool] = {}

    def run(self, node: Project):
        if node.value in self.visited and self.visited[node.value]:
            return
        
        self.visited[node.value] = True
        self.cycle_tracker[node.value] = True
        
        for project in node.dependent_projects:
            if project.value in self.cycle_tracker and self.cycle_tracker[project.value]:
                self.is_cyclic = True
                return
            if project.value not in self.visited or not self.visited[project.value]:
                self.run(project)
        
        self.cycle_tracker[node.value] = False
        self.output_stack.append(node.value)
    
    def get_output_stack(self) -> Deque[str]:
        return self.output_stack

def build_order(projects: list[Project]):
    dfs = DFS()
    for project in projects:
        dfs.run(project)
        
    if dfs.is_cyclic:
        print('Cannot sort a Cyclic Graph')
        return
    
    sorted_projects = list(dfs.get_output_stack())[::-1]
    print(sorted_projects)
    return sorted_projects
    
project_a = Project('a')
project_b = Project('b')
project_c = Project('c')
project_d = Project('d')
project_e = Project('e')
project_f = Project('f')

project_a.set_dependent_projects([project_d])
project_b.set_dependent_projects([project_d])
project_d.set_dependent_projects([project_c])
project_f.set_dependent_projects([project_a, project_b])

projects = [
    project_a,
    project_b,
    project_c,
    project_d,
    project_e,
    project_f,
]

print("Test case #1")
build_order(projects)

project_a = Project('a')
project_b = Project('b')
project_c = Project('c')

project_a.set_dependent_projects([project_b])
project_b.set_dependent_projects([project_c])
project_c.set_dependent_projects([project_a])

projects = [
    project_a,
    project_b,
    project_c,
]

print("Test case #2")
build_order(projects)