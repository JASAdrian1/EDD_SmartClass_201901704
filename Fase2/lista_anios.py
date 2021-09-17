
from nodo_anio import nodo_anio

class lista_anios:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def lista_vacia(self):
        if self.primero is None:
            return True
        else:
            return False


    def insertar(self,anio):
        nuevo_nodo = nodo_anio(anio)
        if self.lista_vacia():
            self.primero = nuevo_nodo

        else:
            tmp = self.primero
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo_nodo


    def imprimir_lista(self):
        tmp = self.primero
        if tmp is not None:
            while tmp is not None:
                print(tmp.anio.no_anio)
                tmp = tmp.siguiente
        else:
            print("La lista para este estudiante esta vacia")
