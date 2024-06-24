'''
The Ford-Fulkerson algorithm works by looking for a path with available capacity 
from the source to the sink (called an augmented path), and then sends as much flow as possible through that path.
Time Complexity: O(max flow * Edges)
'''
def dfs():
    # Returns true if there is a path from source to sink in residual graph. Stores the path.
    pass

def ford_fulkerson():
    # Finding minimum flow from the path
    # Adding the path flows
    # Updating the residual values of edges
    pass



# S A B C D T 
graph = [[0, 8, 0, 0, 3, 0],
         [0, 0, 9, 0, 0, 0],
         [0, 0, 0, 0, 7, 2],
         [0, 0, 0, 0, 0, 5],
         [0, 0, 7, 4, 0, 0],
         [0, 0, 0, 0, 0, 0]]
