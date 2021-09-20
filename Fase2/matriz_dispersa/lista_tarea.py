from matriz_dispersa.nodo_tarea import nodo_tarea


class lista_tarea:
    def __init__(self):
        self.primero = None

    def insertar(self,tarea):
        nuevo_nodo = nodo_tarea(tarea)
        if self.primero is None:
            self.primero = nuevo_nodo
        else:
            tmp = self.primero
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo_nodo


    def imprimir_lista(self):
        tmp = self.primero
        if tmp is not None:
            print("--Nueva lista")
            while tmp is not None:
                print(tmp.tarea.materia)
                tmp = tmp.siguiente
        else:
            print("La lista para este estudiante esta vacia")