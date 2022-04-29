import heapq # cola de prioridad
# clase que representa una cola de prioridad
class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    def insert(self, item, priority): # item es el nodo y priority es el costo a futuro
        heapq.heappush(self._queue, (priority, self._index, item)) # inserta en la cola de prioridad
        self._index += 1

    def remove(self):# devuelve el elemento de menor costo
        return heapq.heappop(self._queue)[-1] 

    def isEmpty(self):# verifica si la cola está vacía
        return len(self._queue) == 0 

    def getSize(self):# devuelve el tamaño de la cola
        return self._index