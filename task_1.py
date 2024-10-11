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

# Створення графа
G = nx.Graph()

# Додавання вершин (зупинок)
stops = ['A', 'B', 'C', 'D', 'E', 'F']
G.add_nodes_from(stops)

# Додавання ребер (маршрутів між зупинками)
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'C'),
    ('B', 'D'),
    ('C', 'D'),
    ('C', 'E'),
    ('C', 'F'),
    ('D', 'F'),
    ('E', 'F'),
    ('E', 'G'),
    ('F', 'G')
]
G.add_edges_from(edges)

# Візуалізація графа
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)  # позиції для всіх вершин
nx.draw_networkx_nodes(G, pos, node_size=700)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos, font_size=14)
plt.title("Транспортна мережа міста")
plt.axis('off')  # вимкнення осей
plt.show()

# Аналіз основних характеристик
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_dict = dict(G.degree())

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступінь вершин:", degree_dict)


