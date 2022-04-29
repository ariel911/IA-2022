#! usr/bin/env python3.5
"""
BFS For cannibals / missionaries. A little long for one file but I didn't feel like breaking it up 

"""
gMISSIONARIES = 3
gCANNIBALS = 3
gBOATSIZE = 2


class State (object):
    def __init__(self, lmiss, rmiss, lcann, rcann, boatloc):
        self.lMissionary = lmiss
        self.rMissionary = rmiss
        self.lCannibal = lcann
        self.rCannibal = rcann
        self.boat = boatloc

    #ver si hemos terminado
    def finished(self):
        if (self.rCannibal == gCANNIBALS and self.rMissionary == gMISSIONARIES): #si se logro llegar al estado final
            return True
        return False

    #comprobar si el estado es válido según la descripción del problema
    def isValid(self):

        #comprobando si los misioneres o canibales no sobrepase el tatal de los mismos
        if(self.lMissionary + self.rMissionary > gMISSIONARIES or self.lCannibal+self.rCannibal > gCANNIBALS): 
            return False


        if(self.rMissionary < 0 or self.lMissionary < 0 or self.rCannibal < 0 or self.lCannibal < 0):
            return False

        #Necesito tener misioneros >= caníbales en un lado dado
        if(self.rCannibal > self.rMissionary and self.rMissionary > 0):
            return False

        if(self.lCannibal > self.lMissionary and self.lMissionary > 0):
            return False

        return True 

#para salida de impresión
    def __str__(self):
        list = []
        list.append('C' * self.lCannibal)
        list.append(' ')
        list.append('M' * self.lMissionary)
        if (self.boat == 'l'):#si el bote esta en el lado izquierdo
            list.append("_\__/_______________")
        else:#si el bote esta en el lado derecho
            list.append("_______________\__/_")
        list.append('C' * self.rCannibal)
        list.append(' ')
        list.append('M' * self.rMissionary)
        s = ''.join(list) #convirtiendo a cadena
        return s


class Node(object):
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent

#Expandir un nodo a todos los movimientos posibles
    def getNeighbors(self):
        retList = [] 
        if self.state.boat == 'r': #comprueba si el bote esta en la derecha
            #1 Missionary
            newState = State(self.state.lMissionary+1, self.state.rMissionary-1, self.state.lCannibal, self.state.rCannibal, 'l')
            #enviamos el nuevo estado y cambiamos la direcion del bote a la izquierda
            newNode = Node(newState, self)
            if newNode.state.isValid(): #se comprueba que el nuevo estado es valido
                retList.append(newNode)

            #1 Cannibal
            #enviamos el nuevo estado y cambiamos la direcion del bote a la izquierda
            newState = State(self.state.lMissionary, self.state.rMissionary, self.state.lCannibal+1, self.state.rCannibal-1, 'l')
            newNode = Node(newState, self)
            if newNode.state.isValid():#se comprueba que el nuevo estado es valido
                retList.append(newNode)

            #1 Missionary 1 Cannibal
            newState = State(self.state.lMissionary+1, self.state.rMissionary-1, self.state.lCannibal+1, self.state.rCannibal-1, 'l')
            newNode = Node(newState, self)
            if newNode.state.isValid():#se comprueba que el nuevo estado es valido
                retList.append(newNode)

            #2 Missionaries
            newState = State(self.state.lMissionary+2, self.state.rMissionary-2, self.state.lCannibal, self.state.rCannibal, 'l')
            newNode = Node(newState, self)
            if newNode.state.isValid():#se comprueba que el nuevo estado es valido
                retList.append(newNode)

            #2 Cannibals
            newState = State(self.state.lMissionary, self.state.rMissionary, self.state.lCannibal+2, self.state.rCannibal-2, 'l')
            newNode = Node(newState, self)
            if newNode.state.isValid():#se comprueba que el nuevo estado es valido
                retList.append(newNode)

        else:
            # 1 Missionary
            newState = State(self.state.lMissionary - 1, self.state.rMissionary + 1, self.state.lCannibal, self.state.rCannibal, 'r')
            newNode = Node(newState, self)
            if newNode.state.isValid():#se comprueba que el nuevo estado es valido
                retList.append(newNode)

            # 1 Cannibal
            newState = State(self.state.lMissionary, self.state.rMissionary, self.state.lCannibal - 1, self.state.rCannibal + 1, 'r')
            newNode = Node(newState, self)
            if newNode.state.isValid():#se comprueba que el nuevo estado es valido
                retList.append(newNode)

            # 1 Missionary 1 Cannibal
            newState = State(self.state.lMissionary - 1, self.state.rMissionary + 1, self.state.lCannibal - 1, self.state.rCannibal + 1, 'r')
            newNode = Node(newState, self)
            if newNode.state.isValid():#se comprueba que el nuevo estado es valido
                retList.append(newNode)

            # 2 Missionaries
            newState = State(self.state.lMissionary - 2, self.state.rMissionary + 2, self.state.lCannibal, self.state.rCannibal, 'r')
            newNode = Node(newState, self)
            if newNode.state.isValid():
                retList.append(newNode)

            # 2 Cannibals
            newState = State(self.state.lMissionary, self.state.rMissionary, self.state.lCannibal - 2, self.state.rCannibal + 2, 'r')
            newNode = Node(newState, self)
            if newNode.state.isValid():
                retList.append(newNode)

        return retList
    
#encontrar la ruta tomada al nodo objetivo, ordenarla correctamente
    def rollback(self):
        path = []
        pNode = self
        while pNode.parent != None:#mientras el nodo tenga padre
            path.append(pNode.state)#se añade el estado del nodo al camino
            pNode = pNode.parent #se cambia el nodo padre
        path.reverse() #se invierte el camino
        for p in path:#se imprime el camino
            print(p)
            print()


#busqueda Primero en Anchura
def mySearch():

    exset = set()#creando un conjunto vacío
    start = State(gMISSIONARIES, 0, gCANNIBALS, 0, 'l') #estado inicial
    print("  ")
    root = Node(start, None)#creando el nodo raíz
    frontier = []
    frontier.append(root)#añadiendo el nodo raíz a la lista de nodos a explorar
    while frontier:
        newnode = frontier.pop(0)#sacamos el primer elemento de la lista y sera el nuevo nodo
        if newnode.state.finished():# verificamos si el estado es el objetivo o no
            newnode.rollback()#encontrar la ruta tomada al nodo objetivo
            exit(0)
        exset.add(newnode) #añadimos el nodo al conjunto de nodos explorados
        neighbors = newnode.getNeighbors()# expandir el padre en movimientos posibles y retorna una lista de nodos
        for n in neighbors:
            if (n not in exset) or (n not in frontier): #si el nodo no esta en el conjunto de nodos explorados o en la lista de nodos a explorar
                frontier.append(n)#añadimos el nodo a la lista de nodos a explorar


def main():
    mySearch()

#iniciamos el programa
if __name__ == "__main__":
    print("Estado Inicial: CCC MMM_\__/_______________")
    print("Estado Final:   _______________\__/_CCC MMM" )
    main()
