import heapq

def prims(graph, start = 'A'):
    unvisited = list(graph.keys())
    visited = []
    total_cost = 0
    mst = []
    
    unvisited.remove(start)
    visited.append(start)
    
    heap = []
    for edge in graph[start]:
        heapq.heappush(heap, edge)
        
    while unvisited:
        (cost, v2, v1) = heapq.heappop(heap)
        new_v = None
        
        if v1 in unvisited and v2 in visited:
           new_v = v1
           mst .append(v1, v2, cost)
           
        elif v2 in unvisited and v1 in visited:
            new_v = v2
            mst .append((v2, v1, cost))
        
        if new_v:
            total_cost += cost
            
            unvisited.remove(new_v)
            visited.append(new_v)

            for vertex in graph[new_v]:
                heapq.heappush(heap, vertex)
            
    return mst, total_cost


graph = {
        'A': [(3, 'D', 'A'), (3, 'C', 'A'), (2, 'B', 'A')],
        'B': [(2, 'A', 'B'), (4, 'C', 'B'), (3, 'E', 'B')],
        'C': [(3, 'A', 'C'), (5, 'D', 'C'), (6, 'F', 'C'), (1, 'E', 'C'), (4, 'B', 'C')],
        'D': [(3, 'A', 'D'), (5, 'C', 'D'), (7, 'F', 'D')],
        'E': [(8, 'F', 'E'), (1, 'C', 'E'), (3, 'B', 'E')],
        'F': [(9, 'G', 'F'), (8, 'E', 'F'), (6, 'C', 'F'), (7, 'D', 'F')],
        'G': [(9, 'F', 'G')],
    }

mst, total_cost = prims(graph, 'A')
print(f'Minimum spanning tree: {mst}')
print(total_cost)