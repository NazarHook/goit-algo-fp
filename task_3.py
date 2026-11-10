import heapq


def dijkstra(graph, start):
    """Найкоротші відстані від start до всіх вершин. Бінарна купа через heapq."""
    distances = {vertex: float("inf") for vertex in graph}
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)

        # застарілий запис у купі, вершину вже опрацьовано з меншою відстанню
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances


def main():
    graph = {
        "A": {"B": 5, "C": 10},
        "B": {"A": 5, "D": 3},
        "C": {"A": 10, "D": 2},
        "D": {"B": 3, "C": 2, "E": 4},
        "E": {"D": 4},
    }

    start = "A"
    distances = dijkstra(graph, start)
    print(f"Найкоротші відстані від вершини {start}:")
    for vertex, distance in distances.items():
        print(f"  {vertex}: {distance}")


if __name__ == "__main__":
    main()
