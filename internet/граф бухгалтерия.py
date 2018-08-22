import networkx as nx
import matplotlib.pyplot as plt

# добавляем вершины
G = nx.Graph()
G.add_node("Лупа")
G.add_node("Пупа")
G.add_node("Бухгалтерия")

# добавляем ребра
G.add_edge("Лупа", "Бухгалтерия")
G.add_edge("Пупа", "Бухгалтерия")

# смотрим на степени вершин
for node in G.nodes():
    print("Степень вершины {} - {}".format(node, G.degree(node)))
print(G.edges())

# можно сохранить в файл и открыть в Gephi
nx.write_gexf(G, 'lupa.gexf')

# рисуем
pos=nx.spectral_layout(G)

nx.draw_networkx_nodes(G, pos, node_color='red', node_size=50)
nx.draw_networkx_edges(G, pos, edge_color='green')
nx.draw_networkx_labels(G, pos, font_size=11, font_family='Arial')
plt.axis('off')
plt.show()
