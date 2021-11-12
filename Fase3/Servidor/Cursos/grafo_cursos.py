import os

from graphviz import Source

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
            #print(tmp.id," == ",id)
            if (str(tmp.id) == str(id)):
                return tmp
            tmp = tmp.siguiente
        return None

    def buscar_nodo_en_pensum(self,id,grafo_pensum):
        tmp = grafo_pensum.primero
        while tmp is not None:
            #print(tmp.id," == ",id)
            if (str(tmp.id) == str(id)):
                return tmp
            tmp = tmp.siguiente
        return None

    def verificar_curso_existe(self,id):
        tmp = self.primero
        while tmp is not None:
            if (str(tmp.id) == str(id)):
                return True
            tmp = tmp.siguiente
        return False


    def buscar_prerequisitos(self,id,grafo_pensum):
        print("---------------------------------")
        print("Codigo: ",id)
        curso = self.buscar_nodo_en_pensum(id,grafo_pensum)
        print("Curso: ",curso.curso.nombre)
        print("PREREQUISITOS: ")
        for prerequisito in curso.curso.prerre.split(","):
            print(prerequisito)
            if prerequisito != "":
                if self.buscar_nodo_en_pensum(prerequisito,grafo_pensum) != None:
                    print("Hola?")
                    if self.verificar_curso_existe(prerequisito) is False:
                        self.insertar(prerequisito, self.buscar_nodo_en_pensum(prerequisito, grafo_pensum).curso)
                    self.buscar_prerequisitos(prerequisito,grafo_pensum)


    def graficar_grafo(self):
        texto = "digraph arbol {\n rankdir=\"LR\""
        tmp = self.primero
        while tmp is not None:
            texto+= "n"+str(tmp.id)+'[label="'+str(tmp.id)+' - '+str(tmp.curso.nombre)+'"];\n'
            tmp = tmp.siguiente
        tmp = self.primero
        while tmp is not None:
            subtmp = tmp.lista_adyacentes.primero
            while subtmp is not None:
                texto += "n" + str(tmp.id) + " -> n" + str(subtmp.id) + "\n"
                subtmp = subtmp.siguiente
            tmp = tmp.siguiente
        texto += "}"
        return texto

    #METODO PARA GRAFICAR LOS ARBOLES NECESARIOS PARA UN SOLO CURSO
    def graficar_curso(self,id):
        curso = self.buscar_nodo(id)
        texto = "digraph arbol {\n rankdir=\"LR\""
        tmp = self.primero
        while tmp is not None:
            texto+= "n"+str(tmp.id)+'[label="'+str(tmp.id)+' - '+str(tmp.curso.nombre)+'"];\n'
            tmp = tmp.siguiente
        tmp = self.primero
        while tmp is not None:
            subtmp = tmp.lista_adyacentes.primero
            while subtmp is not None:
                texto += "n" + str(tmp.id) + " -> n" + str(subtmp.id) + "\n"
                subtmp = subtmp.siguiente
            tmp = tmp.siguiente
        texto += "}"
        return texto
