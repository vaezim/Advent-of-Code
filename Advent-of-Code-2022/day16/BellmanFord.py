
class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.edges = [] # List of edges

    # Add edges
    def add_edge(self, s, t, w):
        self.edges.append([s, t, w])

    def bellman_ford(self, src, verbose=False):
        # Step 1: fill the distance array and predecessor array
        dist = [float("inf")] * self.V
        # Mark the source vertex
        dist[src] = 0

        # Step 2: relax edges |V| - 1 times
        for _ in range(self.V - 1):
            for s, d, w in self.edges:
                if dist[s] != float("inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w

        # Step 3: detect negative cycle
        # if value changes then we have a negative cycle in the graph
        # and we cannot find the shortest distances
        for s, d, w in self.edges:
            if dist[s] != float("inf") and dist[s] + w < dist[d]:
                print("Graph contains negative weight cycle!")
                return

        if verbose: self.print_solution(dist)
        return dist

    # Print the distances from the source
    def print_solution(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print(f"{i}\t\t{dist[i]}")

if __name__ == "__main__":

    g = Graph(5)
    g.add_edge(0, 1, 5)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 3, 3)
    g.add_edge(2, 1, 6)
    g.add_edge(3, 2, 2)

    g.bellman_ford(0)
    