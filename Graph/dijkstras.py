'''
Dijkstra's Algorithm  - an algorithm for finding the shortest paths between nodes in a weighted graph
'''
def dijkstras(graph, start):

    unvisited = list(graph.keys())

    shortest_path = {}

    for vertex in unvisited:
        shortest_path[vertex] = float('inf')

    shortest_path[start] = 0

    while unvisited:
        # take vertex whth minimum way from unvisited 
        min_path = min([val for key, val in shortest_path.items() if key in unvisited])
        new_v = None
        for key, value in shortest_path.items():
            if value == min_path:
                new_v = key

        unvisited.remove(new_v)

        # edges of new vertex + table change 
        for edge in graph[new_v]:
            if edge[1] in unvisited:
                if shortest_path[new_v] + edge[0] < shortest_path[edge[1]]:
                    shortest_path[edge[1]] = shortest_path[new_v] + edge[0]

    return shortest_path


graph = {'A': [(2, 'B'), (8, 'D')],
         'B': [(5, 'D'), (6, 'E')],
         'C': [],
         'D': [(2, 'F'), (3, 'E')],
         'E': [(1, 'F'), (9, 'C')],
         'F': [(3, 'C')]
         }


print(dijkstras(graph, 'A'))
