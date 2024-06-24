'''
Bellman-Ford's algorithm  
An algorithm that computes shortest paths from a single source vertex to all of the other vertices in a weighted digraph.
Weights can be negative.
'''

def bellman_ford(graph, start):
    unvisited = list(graph.keys())
    
    shortest_path = {}
    
    for vertex in graph.keys():
        shortest_path[vertex] = float('inf')
        
    shortest_path[start] = 0
    
    # Relax edges v - 1 times 
    for _ in range(len(graph)-1):
        for node in unvisited:
            for edge in graph[node]:
                if shortest_path[node] + edge[0] < shortest_path[edge[1]]:
                    shortest_path[edge[1]] = shortest_path[node] + edge[0]
                    
    # Nodes in a negative cycle
    
    negative_cycle = set()
    for _ in range(len(graph)-1):
        for node in unvisited:
            for edge in graph[node]:
                if shortest_path[node] + edge[0] < shortest_path[edge[1]]:
                    shortest_path[edge[1]] = -float('inf')
                    negative_cycle.add(edge[1])
    
    return shortest_path, negative_cycle

graph = { 'A0':[(5, 'A1')],
         'A1': [(60, 'F6'),(20, 'B2'),(30, 'E5')],
         'B2': [(10, 'C3'), (75, 'D4')],
         'C3': [(-15, 'B2')],
         'D4': [(100, 'J9')],
         'E5': [(25, 'D4'),(50, 'H8'),(5, 'F6')],
         'F6': [(-50, 'G7')],
         'G7': [(-10, 'H8')],
         'H8': [],
         'J9': []
         }

print(bellman_ford(graph,'A0'))