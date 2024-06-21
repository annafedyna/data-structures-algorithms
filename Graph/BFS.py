# The breadth-first tree obtained by running a BFS on German cities starting from Frankfurt:
# Time complexity: O(V+E)
graph = {
    'Frankfurt': ['Mannheim', 'Würzburg', 'Kassel'],
    'Mannheim': ['Karlsruhe'],
    'Würzburg': ['Erfurt', 'Nürnberg'],
    'Kassel': ['Munich'],
    'Karlsruhe': ['Augsburg'],
    'Erfurt': [],
    'Nürnberg': ['Stuttgart', 'Munich'],
    'Munich': [],
    'Augsburg': ['Munich'],
    'Stuttgart': []
}


def bfs(graph, root):
    queue = []
    visited = []

    queue.append(root)
    visited.append(root)

    while queue:
        vertex = queue.pop(0)
        for node in graph[vertex]:
            if node not in visited:
                queue.append(node)
                visited.append(node)

    return visited


print(bfs(graph, 'Frankfurt'))
