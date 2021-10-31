

class Lista_adyacente:
    def __init__(self):
        self.primero = None
        self.ultimo = None


    def insertar(self,id,curso):
        from Cursos.nodo_grafo import Nodo_grafo
        nuevo_nodo = Nodo_grafo(id,curso)
        if self.primero == None:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo
