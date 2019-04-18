class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, source, destination):
        if source not in self.adjacency_list:
            self.adjacency_list[source] = []
        self.adjacency_list[source].append(destination)

    def dfs_util(self, source, destination, visited, path):
        visited.add(source)
        path.append(source)
        if source == destination:
            print(path)
        else:
            for neighbour in self.adjacency_list[source]:
                if neighbour not in visited:
                    self.dfs_util(neighbour, destination, visited, path)
        path.pop()
        visited.remove(source)

    def print_paths(self, source, destination):
        visited = set()
        path = []
        self.dfs_util(source, destination, visited, path)


graph = Graph()
graph.add_node('A', 'B')
graph.add_node('B', 'C')
graph.add_node('A', 'D')
graph.add_node('C', 'D')
graph.add_node('B', 'D')
print(graph.adjacency_list)
graph.print_paths('B', 'D')






