# Створіть граф за допомогою бібліотеки networkX для моделювання певної реальної мережі 
# (наприклад, транспортної мережі міста, соціальної мережі, інтернет-топології).
# Реальну мережу можна вибрати на свій розсуд, якщо немає можливості придумати свою мережу, 
# наближену до реальності.
# Візуалізуйте створений граф, проведіть аналіз основних характеристик (наприклад, 
# кількість вершин та ребер, ступінь вершин).

# Створено та візуалізовано граф — модель певної реальної мережі.
# Проведено аналіз основних характеристик.

import networkx as nx
import matplotlib.pyplot as plt

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E', 'F'],
    'D': ['B', 'C', 'F'],
    'E': ['C', 'F', 'G'],
    'F': ['C', 'D', 'E', 'G'],
    'G': ['E', 'F']
}

# Створення графа на основі списку суміжностей
G = nx.Graph(graph)

# Візуалізація графа
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=700)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos, font_size=14)
plt.title("Транспортна мережа міста")
plt.axis('off')
plt.show()

# Аналіз основних характеристик
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_dict = dict(G.degree())

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступінь вершин:", degree_dict)


