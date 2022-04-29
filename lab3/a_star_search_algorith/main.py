from Nodo import *
from PriorityQueue import *
from a_star import *

# tests ...

""" # Ejemplo1 
# creando los nodos
nodeS = Nodo('Trebol_Ini', 6)
nodeA = Nodo('Morro', 2)
nodeB = Nodo('Estadio', 1)
nodeD = Nodo('Campesino', 2)
nodeG = Nodo('Terminal', 0)

# creando el grafo
graph = Graph()

# Uniendo los nodos
graph.addEdge(nodeS, nodeA, 4)
graph.addEdge(nodeS, nodeB, 2)
graph.addEdge(nodeS, nodeD, 2)
graph.addEdge(nodeA, nodeG, 2)
graph.addEdge(nodeB, nodeG, 3)
graph.addEdge(nodeD, nodeG, 1)

total_cost = graph.executeAStar(nodeS, nodeG) # ejecutar el algoritmo A*
path = graph.getPath() # obtiene camino
if total_cost:
    print('Costo Total: %s. Ruta: %s' % (total_cost, ' -> '.join(path)))
else:
    print('no llego a la meta!')  """


# Ejemplo2
# surtidor trebol a la Facultad de tecnologia
nodeS = Nodo('Trebol_Inicio', 6)
nodeA = Nodo('Hospital_Uni', 5)
nodeB = Nodo('P.Mariscal', 6)
nodeC = Nodo('Univalle', 7)
nodeE = Nodo('M_Campesino', 1)
nodeD = Nodo('EstadioP', 2)
nodeG = Nodo('Tegnologia', 0)
# creando el grafo
graph2 = Graph()
# Uniendo los nodos
graph2.addEdge(nodeS, nodeA, 1)
graph2.addEdge(nodeA, nodeB, 1)
graph2.addEdge(nodeB, nodeC, 1)
graph2.addEdge(nodeA, nodeE, 8)
graph2.addEdge(nodeA, nodeD, 3)
graph2.addEdge(nodeE, nodeD, 1)
graph2.addEdge(nodeD, nodeG, 2)

total_cost = graph2.executeAStar(nodeS, nodeG)
path = graph2.getPath()
if total_cost:
    print('Costo Total: %s. Ruta: %s' % (total_cost, ' -> '.join(path))) 
else:
    print('no llego a la meta!')