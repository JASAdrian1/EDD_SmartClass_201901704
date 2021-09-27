from graphviz import Source

from arbol_b.nodo_b import nodo_b
from arbol_b.pagina import Pagina

class Arbol_B:
    def __init__(self):
        self.raiz = None
        self.orden = None
        self.altura = 0


    def insertar(self,curso):
        nuevo_nodo = nodo_b(curso)
        if self.raiz is None:
            self.raiz = Pagina()
            self.raiz.raiz = True
            self.raiz = self.raiz.insertar_pagina(nuevo_nodo)
            print("Se ha insertado ", nuevo_nodo.curso.codigo)
        else:
            if self.altura == 0:
                respuesta = self.raiz.insertar_pagina(nuevo_nodo)
                if type(respuesta) == Pagina:
                    print("Se ha insertado ",nuevo_nodo.curso.codigo)
                    self.raiz = respuesta
                elif type(respuesta) == nodo_b:
                    self.altura+=1
                    self.raiz = Pagina()
                    nueva_raiz = respuesta
                    self.raiz = self.raiz.insertar_pagina(nueva_raiz)

            else:
                respuesta = self.insertar_en_posicion(nuevo_nodo,self.raiz)
                if type(respuesta) == nodo_b:
                    self.altura+=1
                    self.raiz = Pagina()
                    self.raiz.insertar_pagina(respuesta)
                else:
                    self.raiz = respuesta



    def insertar_en_posicion(self,nuevo_nodo, raiz):
        if raiz.es_hoja(raiz):
            respuesta = raiz.insertar_pagina(nuevo_nodo)
            return respuesta
        else:
            if nuevo_nodo.curso.codigo < raiz.claves.primero.curso.codigo:
                respuesta = self.insertar_en_posicion(nuevo_nodo,raiz.claves.primero.izquierda)
                if type(respuesta) == nodo_b:
                    return raiz.insertar_pagina(respuesta)
                else:
                    raiz.claves.primero.izquierda = respuesta
                    return raiz
            elif nuevo_nodo.curso.codigo > raiz.claves.ultimo.curso.codigo:
                respuesta = self.insertar_en_posicion(nuevo_nodo,raiz.claves.ultimo.derecha)
                if type(respuesta) == nodo_b:
                    return raiz.insertar_pagina(respuesta)
                else:
                    raiz.claves.ultimo.derecha = respuesta
                    return raiz
            else:
                tmp = raiz.claves.primero
                while tmp is not None:
                    if nuevo_nodo.curso.codigo < tmp.curso.codigo:
                        respuesta = self.insertar_en_posicion(nuevo_nodo,tmp.izquierda)
                        if type(respuesta) == nodo_b:
                            return raiz.insertar_pagina(respuesta)
                        else:
                            tmp.izquierda = respuesta
                            tmp.anterior.derecha = respuesta
                            return raiz
                    elif nuevo_nodo.curso.codigo == tmp.curso.codigo:
                        return raiz
                    else:
                        tmp = tmp.siguiente
        return self


    def graficar(self):
        cadena = 'digraph arbol_b{\n'
        cadena+= 'rankdir ="TB"\n'
        cadena+= 'node [shape =box]'
        cadena+= self.graficar_nodos(self.raiz)
        cadena+= self.graficar_enlaces(self.raiz)
        cadena+="\n}"
        nombre_archivo = r'C:\Users\Adrian Aguilar\Desktop\Reportes_F2\graficar_cursos.dot'
        Archivo = open(nombre_archivo, "w+")
        Archivo.write(cadena)
        Archivo.close()
        try:
            s = Source.from_file(nombre_archivo)
            s.view()
        except Exception as e:
            print(e)


    def graficar_nodos(self, raiz):
        if raiz.es_hoja(raiz):
            nodos = 'node[shape=record label="<p0>'
            contador = 0
            tmp = raiz.claves.primero
            while tmp is not None:
                contador+=1
                nodos+='|{'+str(tmp.curso.codigo)+"\\n"+tmp.curso.nombre+'}|<p'+str(contador)+'> '
                tmp = tmp.siguiente
            nodos+= '"]'+str(raiz.claves.primero.curso.codigo)+'; \n'
            return nodos
        else:
            nodos = 'node[shape=record label="<p0>'
            contador = 0
            tmp = raiz.claves.primero
            while tmp is not None:
                contador+=1
                nodos+= '|{'+str(tmp.curso.codigo)+"\\n"+tmp.curso.nombre+'}|<p'+str(contador)+'> '
                tmp = tmp.siguiente
            nodos+= '"]'+str(raiz.claves.primero.curso.codigo)+'; \n'

            tmp = raiz.claves.primero
            contador = 0
            while tmp is not None:
                aux = ""
                aux+= self.graficar_nodos(tmp.izquierda)
                nodos+=aux
                contador+=1
                tmp = tmp.siguiente
            nodos+= self.graficar_nodos(raiz.claves.ultimo.derecha)
            return nodos


    def graficar_enlaces(self,raiz):
        if raiz.es_hoja(raiz):
            return str(raiz.claves.primero.curso.codigo)+";"
        else:
            enlaces = str(raiz.claves.primero.curso.codigo)+";"
            tmp = raiz.claves.primero
            contador = 0
            r_actual = raiz.claves.primero.curso.codigo
            while tmp is not None:
                enlaces+= "\n"+str(r_actual)+":p"+str(contador)+"->"+self.graficar_enlaces(tmp.izquierda)
                contador+=1
                tmp = tmp.siguiente
            enlaces+= "\n"+str(r_actual)+":p"+str(contador)+"->"+self.graficar_enlaces(raiz.claves.ultimo.derecha)
            return enlaces