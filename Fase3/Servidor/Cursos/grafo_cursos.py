import os

from Cursos.nodo_grafo import Nodo_grafo

class Grafos_cursos:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def insertar(self,id,curso):
        nuevo_nodo = Nodo_grafo(id, curso)
        if self.primero == None:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo

    def asociar_nodo(self,id,adyacente,curso_adyacente):
        nodo = self.buscar_nodo(id)
        nodo_adyacente = self.buscar_nodo(adyacente)
        if nodo_adyacente is None:
            self.insertar(adyacente,curso_adyacente)

        if nodo is not None:
            lista_adyacente = nodo.lista_adyacentes
            lista_adyacente.insertar(adyacente,curso_adyacente)


    def buscar_nodo(self,id):
        tmp = self.primero
        while tmp is not None:
            if (tmp.id == id):
                return tmp
            tmp = tmp.siguiente


    def graficar_grafo(self):
        texto = "digraph arbol {\n rankdir=\"LR\""
        tmp = self.primero
        while tmp is not None:
            texto+= "n"+str(tmp.id)+'[label="'+str(tmp.id)+' - '+str(tmp.curso)+'"];\n'
            tmp = tmp.siguiente
        tmp = self.primero
        while tmp is not None:
            subtmp = tmp.lista_adyacentes.primero
            while subtmp is not None:
                print("AAAAAAAAAAAAaa")
                texto += "n" + str(tmp.id) + " -> n" + str(subtmp.id) + "\n"
                subtmp = subtmp.siguiente
            tmp = tmp.siguiente
        texto += "}"
        archivo = open("grafica_cusos.dot", "w+")
        archivo.write(texto)
        archivo.close()
        os.system("fdp -Tpng -o graph-g.png ejemplo.dot")
