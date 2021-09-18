#from tarea import tarea

class nodo_tarea:
    def __init__(self,tarea):
        self.tarea = tarea
        self.siguiente = None
        self.anterior = None