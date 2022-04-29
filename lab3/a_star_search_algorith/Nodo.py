# class that represents a node
class Nodo:

    # "key"  es el identificador del nodo
    # "forward_cost" es h(n) (costo de la heurística)
    # "forward_cost" se usa en el cálculo de la "búsqueda A*": f(n) = g(n) + h(n) donde
    # h(n) es el costo a futuro y g(n) es el costo atrasado
    def __init__(self, key, forward_cost):
        self.key = key
        self.forward_cost = forward_cost

    def getKey(self): # devuelve el identificador del nodo
        return self.key

    def getForwardCost(self):
        return self.forward_cost # devuelve el costo a futuro