# encoding:utf-8

# A* o "A star" es la combinación de Uniform-cost y Greedy
# Uniform-cost ordenes por costo de ruta o costo atrasado - g(n)
# Greedy Ordena por proximidad a la meta o costo adelantado - h(n)
# A* Search Ordena por la suma: f(n) = g(n) + h(n)
from Nodo import *
from PriorityQueue import *
from collections import defaultdict # diccionario de listas
# clase que representa un grafo
class Graph:

    def __init__(self):
        self.nodes = {} # diccionario de los nodos
        self.edges = [] # lista de 3 tuplas(source, destination, weight)
        self.path = [] 

        # diccionario con las listas de sucesores de cada nodo, más rápido para obtener los sucesores
        # cada elemento de la lista es una tupla de 2: (destination, weight)
        self.successors = defaultdict(list)


    # function that adds edges
    def addEdge(self, source, destination, weight):
        edge = (source, destination, weight) #crea una tupla (tupla de 3)
        if not self.existsEdge(edge): # agrega edge si no existe
            self.nodes[source], self.nodes[destination] = source, destination # agrega los nodos
            self.edges.append(edge) # agrega edge
            self.successors[source.getKey()].append((destination, weight)) # agrega sucesor
        else:
            print('Error: edge (%s -> %s with weight %s) already exists!!' \
                % (edge[0].getKey(), edge[1].getKey(), edge[2]))


    #función que comprueba si existe borde
    def existsEdge(self, edge):
        for e in self.edges: # recorre la lista de edges
            # compara la clave de origen, la clave de destino y el peso del borde
            if e[0].getKey() == edge[0].getKey() and \
                e[1].getKey() == edge[1].getKey() and e[2] == edge[2]: 
                return True
        return False


    # función que devuelve la ruta
    def getPath(self):
        return self.path


    # función que ejecuta el algoritmo "A*"
    def executeAStar(self, initial_node, goal_node): # inicial_node es el nodo inicial y goal_node es el nodo objetivo
        if not self.edges:
            print('Error: graph not contains edges!!')
        else:
            # comprueba si ambos nodos existen
            if initial_node in self.nodes and goal_node in self.nodes:
                if initial_node == goal_node: # comprueba si son los mismos nodos
                    return 0

                queue = PriorityQueue() # crea una cola de prioridad (min heap)

                # "distance_vector" and "antecessors"  se utilizan para reconstruir la ruta
                distance_vector, antecessors = {}, {}
                for node in self.nodes: 
                    distance_vector[node.getKey()] = None # inicializa con None
                    antecessors[node.getKey()] = None # inicializa con None
                distance_vector[initial_node.getKey()] = 0 

                # calculates costs
                g_cost, h_cost = 0, initial_node.getForwardCost() # g(n) = 0, h(n) = h(n)
                f_cost = g_cost + h_cost
                
                queue.insert((initial_node, g_cost, h_cost), f_cost) # inserta el nodo inicial en la cola de prioridad
                total_cost = None

                while True: # mientras la cola no esté vacía

                    # un elemento de la cola es una tupla de 3: (current_node, g_cost, h_cost)
                    current_node, g_cost, h_cost = queue.remove()
                    #print('g_cost_{} + h_cost{}'.format(g_cost,h_cost))
                    successors = self.successors[current_node.getKey()] # obtiene los sucesores de "current_node"
        

                    for successor in successors: # para cada sucesor
                        destination, weight = successor # Desempacar sucesora de 2 tuplas

                        # calcular costo 
                        new_g_cost = g_cost + weight 
                        print('{} + {} = new_g_cost: {}'.format(g_cost,weight,new_g_cost))
                        h_cost = destination.getForwardCost() #devuelve el costo a futuro
                        f_cost = new_g_cost + h_cost # f(n) = g(n) + h(n)
                        
                        queue.insert((destination, new_g_cost, h_cost), f_cost)# inserta en la cola de prioridad
                        
                        # actualizar "distance_vector"
                        if distance_vector[destination.getKey()]:# si ya existe en "distance_vector"
                            print(distance_vector[destination.getKey()],">",new_g_cost) 
                            if distance_vector[destination.getKey()] > new_g_cost:# si el costo actual es menor que el anterior
                                distance_vector[destination.getKey()] = new_g_cost # actualiza el costo
                                antecessors[destination.getKey()] = current_node.getKey() # actualiza el antecesor
                        else:
                            distance_vector[destination.getKey()] = new_g_cost  # si no existe, lo agrega
                            antecessors[destination.getKey()] = current_node.getKey() # actualiza el antecesor


                        # verifica que alcanzó la meta
                        
                        if destination.getKey() == goal_node.getKey(): 
                            # actualizar "total_cost"
                            #print('f_cost: {} < total_cost: {}'.format(f_cost,total_cost))
                            if not total_cost:
                                total_cost = f_cost
                            elif f_cost < total_cost: # si el costo actual es menor que el anterior
                                total_cost = f_cost

                    if queue.isEmpty(): # verifica si la cola está vacía
                        # reconstruir el camino
                        curr_node = goal_node.getKey() # obtiene la clave del nodo final
                        while curr_node: # mientras el nodo no sea None
                            self.path.append(curr_node)
                            curr_node = antecessors[curr_node] # actualiza el nodo actual
                        self.path = self.path[::-1] # invierte el camino
                        return total_cost
                    print("---------------")
            else:
                print('Error: los nodos no existen en el gráfico!!')


