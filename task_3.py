# Реалізуйте алгоритм Дейкстри для знаходження найкоротшого шляху в розробленому графі: 
# додайте у граф ваги до ребер та знайдіть найкоротший шлях між всіма вершинами графа.

# У граф додано ваги ребер, програмно реалізовано алгоритм Дейкстри для знаходження найкоротшого 
# шляху в розробленому графі.

# Граф, який було розроблено у першому завданні, було доповнено вагами ребер.
graph = {
    'A': {'B': 5, 'C': 8},
    'B': {'A': 3, 'C': 6, 'D': 5},
    'C': {'A': 7, 'B': 4, 'D': 3, 'E': 5, 'F': 8},
    'D': {'B': 6, 'C': 4, 'F': 5},
    'E': {'C': 5, 'F': 6, 'G': 7},
    'F': {'C': 4, 'D': 8, 'E': 7, 'G': 6},
    'G': {'E': 6, 'F': 5}
}

def print_table(distances, visited):
    # Верхній рядок таблиці
    print("{:<10} {:<10} {:<10}".format("Вершина", "Відстань", "Перевірено"))
    print("-" * 30)
    
    # Вивід даних для кожної вершини
    for vertex in distances:
        distance = distances[vertex]
        if distance == float('infinity'):
            distance = "∞"
        else:
            distance = str(distance)
        
        status = "Так" if vertex in visited else "Ні"
        print("{:<10} {:<10} {:<10}".format(vertex, distance, status))
    print("\n")

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())
    visited = []

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        visited.append(current_vertex)
        unvisited.remove(current_vertex)
        
        # Вивід таблиці після кожного кроку
        print_table(distances, visited)

    return distances

# Виклик функції для вершини A
dijkstra(graph, 'A')

