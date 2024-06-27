'''
Kruskal's algorithm is a minimum spanning tree algorithm that takes a graph as input
Time Complexity - O(E log E)

Using Union Find Data Structure - works with numbers not letters but this implementation is suitable 
'''
from collections import defaultdict


class Kruskals:
    def __init__(self):
        self.graph = defaultdict(list)
        self.graph_edges = []

    def add_edge(self, from_vertex, to_vertex, weight):
        self.graph[from_vertex].append((weight, to_vertex, from_vertex))

    def sort_edges(self):
        for edges in self.graph.values():
            self.graph_edges.extend(edges)
        self.graph_edges.sort()

    def conv_char(self, char):
        return ord(char) - 65

    # Finds to which component a element belongs to
    def find(self, parent_index, i):
        if parent_index[i] == i:
            return i
        return self.find(parent_index, parent_index[i])

    # Unite two components
    def union(self, parent_index, rank, element1, element2):
        if rank[self.conv_char(element1)] < rank[self.conv_char(element2)]:
            parent_index[self.conv_char(element1)] = self.conv_char(element2)
        elif rank[self.conv_char(element1)] > rank[self.conv_char(element2)]:
            parent_index[self.conv_char(element2)] = self.conv_char(element1)
        else:
            parent_index[self.conv_char(element2)] = self.conv_char(element1)
            rank[self.conv_char(element1)] += 1

    def kruskals(self):
        mst = []
        num_edges = 0
        i = 0

        # Sort edges once
        self.sort_edges()

        parent_index = [i for i in range(len(self.graph))]
        rank = [0 for _ in range(len(self.graph))]

        while num_edges < len(self.graph)-1:
            weight, vertex2, vertex1 = self.graph_edges[i]

            if self.find(parent_index, self.conv_char(vertex1)) != self.find(parent_index, self.conv_char(vertex2)):
                self.union(parent_index, rank, vertex1, vertex2)
                num_edges += 1
                mst.append((vertex1, vertex2, weight))
            i += 1

        return mst


if __name__ == "__main__":
    k = Kruskals()
    k.add_edge('A', 'B', 2)
    k.add_edge('A', 'D', 1)
    k.add_edge('A', 'C', 4)
    k.add_edge('B', 'D', 5)
    k.add_edge('D', 'D', float('inf'))
    k.add_edge('C', 'D', 3)

    print(k.kruskals())
