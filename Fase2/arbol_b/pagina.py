from arbol_b.lista_nodo_b import lista_nodo_b

class Pagina:
    def __init__(self):
        self.claves = lista_nodo_b()
        self.raiz = False
        self.claves_max = 4
        self.claves_min = 2
        self.tamanio = 0


    def insertar_pagina(self,nuevo_nodo):
        if self.claves.insertar(nuevo_nodo):
            self.tamanio=self.claves.tamanio

        if self.tamanio<5:
            return self
        elif self.tamanio == 5:
            return self.dividir_pagina(self)


    def dividir_pagina(self,pagina):
        tmp = pagina.claves.primero
        for i in range(0,2,1):
            tmp = tmp.siguiente

        primero = pagina.claves.primero
        segundo = pagina.claves.primero.siguiente
        tercero = tmp.siguiente
        cuarto = pagina.claves.ultimo

        primero.siguiente = None
        primero.anterior = None
        segundo.siguiente = None
        segundo.anterior = None
        tercero.siguiente = None
        tercero.anterior = None
        cuarto.siguiente = None
        cuarto.anterior = None
        tmp.siguiente = None
        tmp.anterior = None

        izquierda = Pagina()
        izquierda.insertar_pagina(primero)
        izquierda.insertar_pagina(segundo)
        derecha = Pagina()
        derecha.insertar_pagina(tercero)
        derecha.insertar_pagina(cuarto)
        tmp.izquierda = izquierda
        tmp.derecha = derecha

        print("Se dividio la pagina")
        return tmp


    def es_hoja(self,pagina):
        if pagina.claves.primero.izquierda == None:
            return True
        else:
            return False

