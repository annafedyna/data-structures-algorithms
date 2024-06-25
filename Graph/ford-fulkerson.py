'''
The Ford-Fulkerson algorithm works by looking for a path with available capacity 
from the source to the sink (called an augmented path), and then sends as much flow as possible through that path.
Time Complexity: O(max flow * Edges)
'''
from collections import defaultdict


class FordFulkerson:

    def __init__(self, graph):
        self.graph = graph

    def add_edge(self, from_v, to_v, capacity):
        self.graph[from_v].append(
            {'to': to_v, 'capacity': capacity, 'flow': 0})

    def bfs(self, source, sink, visited):
        # Return a path from source to sink in residual graph. Stores the path.
        queue = [source]

        min_capacity = float('inf')
        while queue:
            from_vertex = queue.pop(0)
            for edge in graph[from_vertex]:
                if edge['flow'] < edge['capacity'] and edge['to'] not in visited:
                    min_capacity = min(min_capacity, edge['capacity'] - edge['flow'])
                    queue.append(edge['to'])
                    visited.append(edge['to'])
                    break    
                    
        return min_capacity if sink in visited else False

    def ford_fulkerson(self, graph, source, sink):
        max_flow = 0
        
        while True:
            visited = [source]
            path_flow = self.bfs(source, sink, visited)
            
            if not path_flow:
                break
            
            max_flow += path_flow
        # Updating the residual values of edges
            for i in range(len(visited)-1):
                for next_node in graph[visited[i]]: 
                    if next_node['to'] == visited[i+1]:
                        next_node['capacity'] -= path_flow
                        next_node['flow'] += path_flow
        
        return max_flow


# S A B C D T

if __name__ == "__main__":
    graph = defaultdict(list)

    fordfulkerson = FordFulkerson(graph)

    fordfulkerson.add_edge('S', 'A', 8)
    fordfulkerson.add_edge('S', 'B', 3)
    fordfulkerson.add_edge('A', 'B', 9)
    fordfulkerson.add_edge('B', 'D', 7)
    fordfulkerson.add_edge('B', 'T', 2)
    fordfulkerson.add_edge('C', 'T', 5)
    fordfulkerson.add_edge('D', 'B', 7)
    fordfulkerson.add_edge('D', 'C', 4)

    source = 'S'
    sink = 'T'

    print(fordfulkerson.ford_fulkerson(graph, source, sink))
