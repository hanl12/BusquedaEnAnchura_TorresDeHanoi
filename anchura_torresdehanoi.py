from copy import deepcopy
import sys
from time import time
sys.setrecursionlimit(1000000)

#Declarar objeto nodo
class Nodo:
        def __init__(self):
            self.estado = [[],[],[]]
            self.numeronodo = 0
            self.padre = None
            self.hijo = []

#Funcion mover nodos
def Mover(est1,est2):

    e1 = est1[:]
    e2 = est2[:]

    if len(e1) > 0:

        Cima = e1[len(e1) - 1]
        Ultimoe2 = len(e2) - 1

        if len(e2) == 0 or e2[Ultimoe2] > Cima:
            e2.append(Cima)
            e1.pop()

            return e1,e2
        else:
            return None
    else:
        return None

#Funcion mover discos,procesar siguientes nodos
def MoverDisco(n):

    global Torres 

    Pilas = []

    for x in range(0, 3):

        for y in range(0, 3):
    
            Pilas = Mover(n.estado[x],n.estado[y])

            if Pilas != None:

                SiguienteNodo = Nodo()
                SiguienteNodo = deepcopy(n)
                SiguienteNodo.estado[x] = deepcopy(Pilas[0])
                SiguienteNodo.estado[y] = deepcopy(Pilas[1])

                if SiguienteNodo.estado in Estados:
                    DarValorAIf = 1
                else:
                    NoDeNodo = SiguienteNodo.numeronodo
                    Estados.append(SiguienteNodo.estado)
                    return SiguienteNodo
    return None

    
#Mostrar camino de solucion
def MostrarCamino(nodo):
    global Total, TiempoInicial
    print("CAMINO DE LA SOLUCION")
    Orden = []
    while True:
        print("Nodo no. ", nodo.numeronodo, " Estado ", nodo.estado)
        Orden.append(nodo.numeronodo)
        if nodo.padre != None:
            nodo = nodo.padre            
        else:
            print("\nRecorrido a la solucion: \n")
            for x in range(1,len(Orden) + 1):
                if len(Orden) - x < 1:
                    print(Orden[len(Orden) - x])
                    print("Nodos totales del camino de la solución: ", len(Orden))
                else:
                    print(Orden[len(Orden) - x], end=" -> ")                
            TiempoFinal = time()
            TiempoTotal = TiempoFinal - TiempoInicial
            print("\nTiempo transcurrido: ",round(TiempoTotal,2), " Segundos")
            print("\nNodos totales: ", Total, "\n")
            exit()
            break

#Funcion principal de Busqueda en Anchura
def BusquedaEnAnchura(nodo):

    global ListaPadre,NoDeNodo,ListaHijo,SolucionEncontrada,Paso,Total 

    Paso = Paso + 1 

    for nodo in ListaPadre:
        if SolucionEncontrada == False: 
            print("\nNodo padre No. ", nodo.numeronodo, " Estado ", nodo.estado) 

            Agotado = False

            Padre = deepcopy(nodo)
            
            i = 1

            while Agotado == False:

                i+=1
                NodoHijo = MoverDisco(nodo)

                if NodoHijo != None:
                    NoDeNodo+=1
                    NodoHijo.numeronodo = NoDeNodo
                    NodoHijo.padre = nodo
                    Padre.hijo.append(NodoHijo)
                    ListaHijo.append(NodoHijo)
                    print("\tNodo hijo No. ", NodoHijo.numeronodo, " Estado ", NodoHijo.estado, end="")

                    if NodoHijo.estado == EstadoFinal:
                        print ("\nSolución encontrada\n")
                        Total = NodoHijo.numeronodo
                        MostrarCamino(NodoHijo)
                        SolucionEncontrada = True
                else:
                    Agotado = True
    ListaPadre = deepcopy(ListaHijo)
    ListaHijo = []
    if SolucionEncontrada == False:
        BusquedaEnAnchura(ListaPadre)

#Funcion main
TiempoInicial = time()
Torres = 3
EstadoInicial = [[7, 6, 5, 4, 3, 2, 1], [], []]
EstadoFinal = [[], [], [7, 6, 5, 4, 3, 2, 1]]

Estados = []
Estados = [EstadoInicial]
NoDeNodo = 1
SolucionEncontrada = False
Total = 0

nodo = Nodo()
nodo.estado = EstadoInicial
nodo.numeronodo = NoDeNodo
ListaPadre = [nodo]
ListaHijo = []
SolucionEncontrada = False

Paso = 1
ListaPadre = [nodo]
ListaHijo = []
BusquedaEnAnchura(nodo)