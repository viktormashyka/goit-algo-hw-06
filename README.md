# goit-algo-hw-06

# Висновки до Завдання 2

# Порівняння DFS та BFS на прикладі графа

### Вихідний граф:

graph = { 'A': ['B', 'C'], 'B': ['A', 'C', 'D'], 'C': ['A', 'B', 'D', 'E', 'F'], 'D': ['B', 'C', 'F'], 'E': ['C', 'F', 'G'], 'F': ['C', 'D', 'E', 'G'], 'G': ['E', 'F'] }

### Результати:

- **DFS (глибина):** `A → B → C → D → F → E → G`
- **BFS (ширина):** `A → B → C → D → E → F → G`

### Висновки:

- **DFS** досліджує глибину графа, іде вглиб кожної гілки перед поверненням до попереднього рівня.
- **BFS** досліджує всі сусіди кожної вершини, перш ніж іти на наступний рівень.

Різниця в шляхах обумовлена природою алгоритмів: DFS орієнтований на глибину, BFS — на ширину.
