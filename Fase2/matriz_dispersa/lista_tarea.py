from matriz_dispersa.nodo_tarea import nodo_tarea


class lista_tarea:
    def __init__(self):
        self.primero = None

    def insertar(self,tarea):
        nuevo_nodo = nodo_tarea(tarea)