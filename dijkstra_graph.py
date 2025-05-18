import heapq

def dijkstra(graph, start):
    queue = [(0, start)]
    distances = {v: float('inf') for v in graph}
    distances[start] = 0

    while queue:
        curr_distance, vertex = heapq.heappop(queue)

        if curr_distance > distances[vertex]:
            continue

        for neighbor, weight in graph[vertex].items():
            distance = curr_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances

# Example usage
graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
    'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
    'E': {'C': 8, 'D': 3},
    'F': {'D': 6}
}

if __name__ == "__main__":
    distances = dijkstra(graph, 'A')
    print(distances)
