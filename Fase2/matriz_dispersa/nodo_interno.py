from matriz_dispersa.lista_tarea import lista_tarea


class nodo_interno_matriz:
    def __init__(self,tarea,x,y):
        self.tareas = lista_tarea()
        self.siguiente = None
        self.posx = x
        self.posy = y
        self.anterior = None
        self.siguiente = None
        self.arriba = None
        self.abajo = None
        self.tareas.insertar(tarea)