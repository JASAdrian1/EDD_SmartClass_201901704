from nodo_avl import Nodo_avl

class Arbol_avl:
    def __init__(self):
        self.raiz = None


    def insertar(self,nuevo,id):
        nodo_nuevo = Nodo_avl(nuevo,id)
        if self.raiz is None:
            self.raiz = nodo_nuevo
        else:
            self.raiz = self.insertar_nodo_posicion(nodo_nuevo,id,self.raiz)

    def insertar_nodo_posicion(self,nuevo,id,raiz):
        if raiz is not None:
            if id>raiz.id:
                raiz.derecha = self.insertar_nodo_posicion(nuevo,id,raiz.derecha)
                return raiz
            elif id<raiz.id:
                raiz.izquierda = self.insertar_nodo_posicion(nuevo, id, raiz.izquierda)
                return raiz
        else:
            raiz = nuevo
            return raiz


    def preorden(self,raiz):
        if raiz is not None:
            print(raiz.id)
            self.preorden(raiz.izquierda)
            self.preorden(raiz.derecha)



    def graficar_arbol(self):
        print("Hola")
