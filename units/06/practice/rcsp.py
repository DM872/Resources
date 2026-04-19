import matplotlib.pyplot as plt
import networkx as nx
from networkx import DiGraph
from numpy import array

max_res, min_res = [4, 20], [1, 0]
# Create a DiGraph
G = DiGraph(directed=True, n_res=2)
G.add_edge("S", "A", res_cost=[8], weight=3)
G.add_edge("S", "B", res_cost=[5], weight=5)
G.add_edge("S", "C", res_cost=[12], weight=2)
G.add_edge("A", "D", res_cost=[4], weight=7)
G.add_edge("B", "D", res_cost=[2], weight=6)
G.add_edge("C", "D", res_cost=[4], weight=3)
G.add_edge("D", "E", res_cost=[3], weight=4)
G.add_edge("D", "F", res_cost=[5], weight=8)
G.add_edge("E", "T", res_cost=[4], weight=4)
G.add_edge("F", "T", res_cost=[3], weight=1)

# Draw the graph
plt.figure(figsize=(10, 7))

# Manually define coordinates for a left-to-right flow
pos = {
    "S": (0, 1),
    "A": (1, 2),
    "B": (1, 1),
    "C": (1, 0),
    "D": (2, 1),
    "E": (3, 1.5),
    "F": (3, 0.5),
    "T": (4, 1)
}

nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, font_weight='bold', arrowstyle='->', arrowsize=20)

# Add labels close to the nodes (e.g., [3,5]) by offsetting the y-coordinate
node_extra_labels = {node: "[3,5]" for node in G.nodes()}
node_extra_labels = {
    "S": "[0,0]",
    "A": "[6,14]",
    "B": "[9,12]",
    "C": "[8,12]",
    "D": "[9,15]",
    "E": "[13,14]",
    "F": "[13,18]",
    "T": "[15,20]"
}
pos_higher = {k: (v[0], v[1] + 0.12) for k, v in pos.items()}
nx.draw_networkx_labels(G, pos_higher, labels=node_extra_labels, font_size=10, font_color='darkgreen')

# Create custom labels for edges to show both weight and res_cost
edge_labels = {(u, v): f"c:{d['weight']}\nr:{d['res_cost']}" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=9)

plt.title("Resource Constrained Shortest Path Graph")
plt.show()


raise SystemError
from cspy import BiDirectional
# init algorithm
max_res, min_res = [4, 20], [1, 0]
bidirec = BiDirectional(G, max_res, min_res, direction="both")

# Call and query attributes
bidirec.run()
print(bidirec.path)
print(bidirec.total_cost)
print(bidirec.consumed_resources)