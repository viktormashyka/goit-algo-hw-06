# Напишіть програму, яка використовує алгоритми DFS і BFS для знаходження шляхів у графі, 
# який було розроблено у першому завданні.
# Далі порівняйте результати виконання обох алгоритмів для цього графа, висвітлить різницю 
# в отриманих шляхах. Поясніть, чому шляхи для алгоритмів саме такі.

# Програмно реалізовано алгоритми DFS і BFS для знаходження шляхів у графі, який було розроблено 
# у першому завданні.
# Здійснено порівняння результатів алгоритмів для цього графа, пояснено різницю в отриманих шляхах. 
# Обґрунтовано, чому шляхи для алгоритмів саме такі.
# Висновки оформлено у вигляді файлу readme.md домашнього завдання.

# Граф, який було розроблено у першому завданні
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E', 'F'],
    'D': ['B', 'C', 'F'],
    'E': ['C', 'F', 'G'],
    'F': ['C', 'D', 'E', 'G'],
    'G': ['E', 'F']
}

# Рекурсивна реалізація алгоритму DFS
def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ')  # Відвідуємо вершину
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# Виклик функції DFS
dfs_recursive(graph, 'A')

print('\n')

# Рекурсивна реалізація BFS
from collections import deque

def bfs_recursive(graph, queue, visited=None):
    # Перевіряємо, чи існує множина відвіданих вершин, якщо ні, то ініціалізуємо нову
    if visited is None:
        visited = set()
    # Якщо черга порожня, завершуємо рекурсію
    if not queue:
        return
    # Вилучаємо вершину з початку черги
    vertex = queue.popleft()
    # Перевіряємо, чи відвідували раніше дану вершину
    if vertex not in visited:
        # Якщо не відвідували, друкуємо вершину
        print(vertex, end=" ")
        # Додаємо вершину до множини відвіданих вершин.
        visited.add(vertex)
        # Додаємо невідвіданих сусідів даної вершини в кінець черги.
        queue.extend(set(graph[vertex]) - visited)
    # Рекурсивний виклик функції з тією ж чергою та множиною відвіданих вершин
    bfs_recursive(graph, queue, visited)

# Запуск рекурсивного алгоритму BFS
bfs_recursive(graph, deque(["A"]))
