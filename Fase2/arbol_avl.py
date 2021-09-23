from nodo_avl import Nodo_avl
from graphviz import Graph, Source

class Arbol_avl:
    def __init__(self):
        self.raiz = None

    def altura(self,nodo):
        if nodo is not None:
            return nodo.altura
        else:
            return -1

    def max(self,a,b):
        if a>b:
            return a
        else:
            return b


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
                if (self.altura(raiz.derecha)-self.altura(raiz.izquierda) == 2):
                    if nuevo.id > raiz.derecha.id:
                        raiz = self.rotacion_derecha(raiz)
                    else:
                        raiz = self.rotacion_derecha_izquierda(raiz)

            elif id<raiz.id:
                raiz.izquierda = self.insertar_nodo_posicion(nuevo,id,raiz.izquierda)
                if (self.altura(raiz.derecha) - self.altura(raiz.izquierda) == -2):
                    if nuevo.id < raiz.izquierda.id:
                        raiz = self.rotacion_izquierda(raiz)
                    else:
                        raiz = self.rotacion_izquierda_derecha(raiz)

            raiz.altura = self.max(self.altura(raiz.derecha),self.altura(raiz.izquierda))+1
            return raiz
        else:
            raiz = nuevo
            return raiz

#Rotaciones
    def rotacion_derecha(self,nodo):
        tmp = nodo.derecha
        nodo.derecha = tmp.izquierda
        tmp.izquierda = nodo
        nodo.altura = self.max(self.altura(nodo.derecha),self.altura(nodo.izquierda)) +1
        tmp.altura = self.max(nodo.altura,self.altura(nodo.derecha))+1
        return tmp

    def rotacion_izquierda(self,nodo):
        tmp = nodo.izquierda
        nodo.izquierda = tmp.derecha
        tmp.derecha = nodo
        nodo.altura = self.max(self.altura(nodo.derecha),self.altura(nodo.izquierda)) +1
        tmp.altura = self.max(nodo.altura,self.altura(nodo.izquierda))+1
        return tmp

    def rotacion_izquierda_derecha(self,nodo):
        nodo.izquierda = self.rotacion_derecha(nodo.izquierda)
        tmp = self.rotacion_izquierda(nodo)
        return tmp

    def rotacion_derecha_izquierda(self,nodo):
        nodo.derecha = self.rotacion_izquierda(nodo.derecha)
        tmp = self.rotacion_derecha(nodo)
        return tmp


    def eliminar(self,carnet):
        self.eliminar_estudiante(carnet,self.raiz)


    def eliminar_estudiante(self,carnet,raiz):
        if raiz is not None:
            #print(str(raiz.estudiante.carnet)+" == "+ str(carnet))
            if str(raiz.estudiante.carnet) == str(carnet):
                if raiz.derecha is None and raiz.izquierda is None:
                    print(raiz.estudiante.carnet)
                    raiz = None
                    print("Se ha eliminado al usuario")
                    return raiz
                elif raiz.derecha is None and raiz.izquierda is not None:
                    raiz = raiz.izquierda
                    raiz.izquierda = None
                    print("Se ha modificado al usuario")
                    return raiz
                elif raiz.izquierda is None and raiz.derecha is not None:
                    raiz = raiz.derecha
                    raiz.derecha = None
                    print("Se ha modificado al usuario")
                    return raiz
            self.eliminar_estudiante(carnet, raiz.izquierda)
            self.eliminar_estudiante(carnet, raiz.derecha)

    def modificar(self,nuevo_estudiante):
        self.modifiar_estudiante(nuevo_estudiante.carnet,nuevo_estudiante,self.raiz)



    def buscar_por_carnet(self,carnet,raiz):
        if raiz is not None:
            #print(str(raiz.estudiante.carnet)+" == "+ str(carnet))
            if str(raiz.estudiante.carnet) == str(carnet):
                print("Carnet: "+str(carnet))
                return raiz
            self.buscar_por_carnet(carnet, raiz.izquierda)
            self.buscar_por_carnet(carnet, raiz.derecha)

    def modifiar_estudiante(self,carnet,estudiante,raiz):
        if raiz is not None:
            #print(str(raiz.estudiante.carnet)+" == "+ str(carnet))
            if str(raiz.estudiante.carnet) == str(carnet):
                raiz.estudiante = estudiante
                print("Se ha modificado al usuario")
                return raiz
            self.modifiar_estudiante(carnet,estudiante, raiz.izquierda)
            self.modifiar_estudiante(carnet,estudiante, raiz.derecha)

    #METODO PARA LA FUNCION GET DEL MAIN
    def get_informacion_estudiante(self,carnet,raiz,info_estudiante):
        if raiz is not None:
            #print(str(raiz.estudiante.carnet)+" == "+ str(carnet))
            if str(raiz.estudiante.carnet) == str(carnet):
                estudiante = raiz.estudiante
                informacion_estudiante = {
                    "carnet": estudiante.carnet,
                    "dpi":estudiante.dpi,
                    "nombre":estudiante.nombre,
                    "carrera":estudiante.carrera,
                    "correo":estudiante.correo,
                    "password":estudiante.password,
                    "creditos":estudiante.creditos,
                    "edad":estudiante.edad
                }
                info_estudiante.clear()
                info_estudiante.append(informacion_estudiante)
                #print(info_estudiante)
                return informacion_estudiante
            self.get_informacion_estudiante(carnet, raiz.izquierda,info_estudiante)
            self.get_informacion_estudiante(carnet, raiz.derecha,info_estudiante)


    def insertar_anio(self,carnet,raiz,no_anio):
        if raiz is not None:
            #print(str(raiz.estudiante.carnet)+" == "+ str(carnet))
            if str(raiz.estudiante.carnet) == str(carnet):
                raiz.estudiante.lista_de_anios.insertar(no_anio)
            self.insertar_anio(carnet, raiz.izquierda,no_anio)
            self.insertar_anio(carnet, raiz.derecha,no_anio)


    def insertar_mes(self,carnet,raiz,no_anio,no_mes):
        if raiz is not None:
            #print(str(raiz.estudiante.carnet)+" == "+ str(carnet))
            if str(raiz.estudiante.carnet) == str(carnet):
                raiz.estudiante.lista_de_anios.insertar_mes(no_anio,no_mes)
            self.insertar_mes(carnet, raiz.izquierda,no_anio,no_mes)
            self.insertar_mes(carnet, raiz.derecha,no_anio,no_mes)

    def insertar_tarea(self,carnet,raiz,no_anio,no_mes, tarea):
        if raiz is not None:
            #print(str(raiz.estudiante.carnet)+" == "+ str(carnet))
            if str(raiz.estudiante.carnet) == str(carnet):
                #print(tarea.materia)
                raiz.estudiante.lista_de_anios.insertar_tarea(no_anio,no_mes,tarea)
            self.insertar_tarea(carnet, raiz.izquierda,no_anio,no_mes,tarea)
            self.insertar_tarea(carnet, raiz.derecha,no_anio,no_mes,tarea)



    def buscar_tarea(self, carnet, raiz, no_anio, no_mes, tarea):
        if raiz is not None:
            # print(str(raiz.estudiante.carnet)+" == "+ str(carnet))
            if str(raiz.estudiante.carnet) == str(carnet):
                # print(tarea.materia)
                raiz.estudiante.lista_de_anios.insertar_tarea(no_anio, no_mes, tarea)
            self.buscar_tarea(carnet, raiz.izquierda, no_anio, no_mes, tarea)
            self.buscar_tarea(carnet, raiz.derecha, no_anio, no_mes, tarea)


    def graficar_matriz_dispersa(self, carnet, raiz, no_anio, no_mes):
        if raiz is not None:
            # print(str(raiz.estudiante.carnet)+" == "+ str(carnet))
            if str(raiz.estudiante.carnet) == str(carnet):
                # print(tarea.materia)
                raiz.estudiante.lista_de_anios.graficar_matriz_dispersa(no_anio, no_mes)
            self.graficar_matriz_dispersa(carnet, raiz.izquierda, no_anio, no_mes)
            self.graficar_matriz_dispersa(carnet, raiz.derecha, no_anio, no_mes)

    def get_informacion_tareas(self, carnet, raiz, no_anio, no_mes,dia,hora,lista_tareas):
        if raiz is not None:
            # print(str(raiz.estudiante.carnet)+" == "+ str(carnet))
            if str(raiz.estudiante.carnet) == str(carnet):
                # print(tarea.materia)
                print(raiz.estudiante.lista_de_anios.get_informacion_tareas(no_anio, no_mes,dia,hora))
                lista_tareas.append(raiz.estudiante.lista_de_anios.get_informacion_tareas(no_anio, no_mes,dia,hora))
                print(lista_tareas)
            self.get_informacion_tareas(carnet, raiz.izquierda, no_anio, no_mes,dia,hora,lista_tareas)
            self.get_informacion_tareas(carnet, raiz.derecha, no_anio, no_mes,dia,hora,lista_tareas)


    def graficar_tareas(self, carnet, raiz, no_anio, no_mes,dia,hora):
        if raiz is not None:
            if str(raiz.estudiante.carnet) == str(carnet):
                raiz.estudiante.lista_de_anios.graficar_tareas(no_anio, no_mes, dia, hora)
            self.graficar_tareas(carnet, raiz.izquierda, no_anio, no_mes,dia,hora)
            self.graficar_tareas(carnet, raiz.derecha, no_anio, no_mes,dia,hora)


    def imprimir_lista(self, raiz):
        if raiz is not None:
            print("-----------------------------------------------------------------")
            print(raiz.estudiante.carnet)
            #print("**************AÑO***************")
            #raiz.estudiante.lista_de_anios.imprimir_lista()
            #print("**************MESES***************")
            #raiz.estudiante.lista_de_anios.imprimir_meses()
            raiz.estudiante.lista_de_anios.imprimir_tareas()
            self.imprimir_lista(raiz.izquierda)
            self.imprimir_lista(raiz.derecha)


    def graficar(self):
        cadena = "digraph arbol {\n"
        if (self.raiz != None):
            cadena += self.listar(self.raiz)
            cadena += "\n"
            cadena += self.enlazar(self.raiz)
        cadena += "}"
        nombre_archivo = r'C:\Users\Adrian Aguilar\Desktop\Reportes_F2\grafica_estudiantes.dot'
        Archivo = open(nombre_archivo, "w+")
        Archivo.write(cadena)
        Archivo.close()
        try:
            s = Source.from_file(nombre_archivo)
            s.view()
        except:
            print("Por favor cierre el archivo de la grafica y vuelva a realizar la peticion")

    def listar(self, raiz_actual):
        if raiz_actual:
            cadena = "n" + str(raiz_actual.estudiante.carnet) + "[label= \"" + str(raiz_actual.estudiante.get_informacion()) + "\" shape=\"rectangle\"];\n"
            cadena += self.listar(raiz_actual.izquierda)
            cadena += self.listar(raiz_actual.derecha)
            return cadena
        else:
            return ""

    def enlazar(self, raiz_actual):
        cadena = ""
        if raiz_actual:
            if raiz_actual.izquierda:
                cadena += "n" + str(raiz_actual.estudiante.carnet) + " -> n" + str(raiz_actual.izquierda.estudiante.carnet) + "\n"
            if raiz_actual.derecha:
                cadena += "n" + str(raiz_actual.estudiante.carnet) + " -> n" + str(raiz_actual.derecha.estudiante.carnet) + "\n"

            cadena += self.enlazar(raiz_actual.izquierda)
            cadena += self.enlazar(raiz_actual.derecha)

        return cadena
