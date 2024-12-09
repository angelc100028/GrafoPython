import networkx as nx 
import matplotlib.pyplot as plt 

# Crear un grafo
G = nx.Graph()

# Agregar nodos y aristas
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4)])

# Dibujar el grafo 
nx.draw(G, with_labels=True, font_weight='bold') 
plt.show() 

