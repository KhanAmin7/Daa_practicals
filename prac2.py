from heapq import heappush, heappop

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]  # Adjacency list

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))  # (neighbor, weight)

    def dijkstra(self, src):
        dist = [float('inf')] * self.V  # Initialize distances
        dist[src] = 0  # Distance of source from itself is 0
        pq = [(0, src)]  # Priority queue: (distance, vertex)
        while pq:
            current_dist, u = heappop(pq) #extracts the minimum distance
            if current_dist > dist[u]:
                continue  # Skip if already processed vertex

            for neighbor, weight in self.graph[u]:
                new_dist = current_dist + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heappush(pq, (new_dist, neighbor))

        return dist  # Return distances from source to all vertices

# Example usage
g = Graph(6)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 2)
g.add_edge(1, 2, 1)
g.add_edge(1, 3, 5)
g.add_edge(2, 4, 10)
g.add_edge(3, 4, 2)
g.add_edge(3, 5, 6)
g.add_edge(4, 5, 5)

distances = g.dijkstra(0)

for i in range(g.V):
    print(f"Distance from source (0) to vertex {i} is {distances[i]}")
