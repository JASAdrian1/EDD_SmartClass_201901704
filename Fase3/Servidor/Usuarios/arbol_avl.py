from Usuarios.nodo_avl import Nodo_avl
from graphviz import Graph, Source

class Arbol_avl:
    def __init__(self):
        self.raiz = None
        self.validacion_login = None

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


    def login(self,usuario,password):
        self.validacion_login = None
        self.buscar_usuario(usuario,password,self.raiz)


    def buscar_usuario(self,id,password,raiz):
        if raiz is not None:
            #print((raiz.usuario.id)+" == "+ str(id)+"   "+str(raiz.usuario.password) + " == "+ str(password))
            if str(raiz.usuario.id) == str(id) and str(raiz.usuario.password) == str(password):
                print("id: "+str(id)+" se ha logeado")
                self.validacion_login = raiz.usuario   #Si se encuentra al usuario se retorna ese mismo usuario
                return raiz
            self.buscar_usuario(id,password, raiz.izquierda)
            self.buscar_usuario(id, password, raiz.derecha)


    def eliminar(self,id):
        self.eliminar_usuario(id,self.raiz)


    def eliminar_usuario(self,id,raiz):
        raiz_anterior = None
        if raiz is not None:
            if raiz.derecha is not None:
                #print(str(raiz.usuario.id)+" == "+ str(id))
                if str(raiz.derecha.usuario.id) == str(id):
                    tmp = raiz.derecha
                    if tmp.derecha is None and tmp.izquierda is None:
                        raiz.derecha = None
                        print("Se ha eliminado al usuario", raiz.usuario.id)
                        return
                    elif tmp.derecha is None and tmp.izquierda is not None:
                        raiz.derecha = tmp.izquierda
                        tmp.izquierda = None
                        print("Se ha eliminado al usuario", raiz.usuario.id)
                        return
                    elif tmp.izquierda is None and tmp.derecha is not None:
                        raiz.derecha = tmp.derecha
                        tmp.derecha = None
                        print("Se ha eliminado al usuario", raiz.usuario.id)
                        return
            if raiz.izquierda is not None:
                # print(str(raiz.usuario.id)+" == "+ str(id))
                if str(raiz.derecha.usuario.id) == str(id):
                    tmp = raiz.izquierda
                    if tmp.derecha is None and tmp.izquierda is None:
                        raiz.derecha = None
                        print("Se ha eliminado al usuario", raiz.usuario.id)
                        return
                    elif tmp.derecha is None and tmp.izquierda is not None:
                        raiz.derecha = tmp.izquierda
                        tmp.izquierda = None
                        print("Se ha eliminado al usuario", raiz.usuario.id)
                        return
                    elif tmp.izquierda is None and tmp.derecha is not None:
                        raiz.derecha = tmp.derecha
                        tmp.derecha = None
                        print("Se ha eliminado al usuario", raiz.usuario.id)
                        return
            self.eliminar_usuario(id, raiz.izquierda)
            self.eliminar_usuario(id, raiz.derecha)

    def modificar(self,nuevo_usuario):
        self.modifiar_usuario(nuevo_usuario.id,nuevo_usuario,self.raiz)



    def buscar_por_id(self,id,raiz):
        if raiz is not None:
            #print(str(raiz.usuario.id)+" == "+ str(id))
            if str(raiz.usuario.id) == str(id):
                print("id: "+str(id))
                return raiz
            self.buscar_por_id(id, raiz.izquierda)
            self.buscar_por_id(id, raiz.derecha)

    def modifiar_usuario(self,id,usuario,raiz):
        if raiz is not None:
            #print(str(raiz.usuario.id)+" == "+ str(id))
            if str(raiz.usuario.id) == str(id):
                raiz.usuario = usuario
                print("Se ha modificado al usuario")
                return raiz
            self.modifiar_usuario(id,usuario, raiz.izquierda)
            self.modifiar_usuario(id,usuario, raiz.derecha)

    #METODO PARA LA FUNCION GET DEL MAIN
    def get_informacion_usuario(self,id,raiz,info_usuario):
        if raiz is not None:
            #print(str(raiz.usuario.id)+" == "+ str(id))
            if str(raiz.usuario.id) == str(id):
                usuario = raiz.usuario
                informacion_usuario = {
                    "id": usuario.id,
                    "dpi":usuario.dpi,
                    "nombre":usuario.nombre,
                    "carrera":usuario.carrera,
                    "correo":usuario.correo,
                    "password":usuario.password,
                    "creditos":usuario.creditos,
                    "edad":usuario.edad
                }
                info_usuario.clear()
                info_usuario.append(informacion_usuario)
                #print(info_usuario)
                return informacion_usuario
            self.get_informacion_usuario(id, raiz.izquierda,info_usuario)
            self.get_informacion_usuario(id, raiz.derecha,info_usuario)



    def insertar_tarea(self,id,raiz,no_anio,no_mes, tarea,tipo_operacion=False,id_tarea=-1):
        if raiz is not None:
            #print(str(raiz.usuario.id)+" == "+ str(id))
            if str(raiz.usuario.id) == str(id):
                #print(tarea.materia)
                raiz.usuario.lista_de_anios.insertar_tarea(no_anio,no_mes,tarea,tipo_operacion,id_tarea)
            self.insertar_tarea(id, raiz.izquierda,no_anio,no_mes,tarea,tipo_operacion,id_tarea)
            self.insertar_tarea(id, raiz.derecha,no_anio,no_mes,tarea,tipo_operacion,id_tarea)



    def insertar_curso(self,id,raiz,no_anio,no_semestre,curso):
        if raiz is not None:
            #print(str(raiz.usuario.id)+" == "+ str(id))
            if str(raiz.usuario.id) == str(id):
                #print("Se inserto el semestre al usuario ",id)
                raiz.usuario.lista_de_anios.insertar_curso(no_anio,no_semestre,curso)
            self.insertar_curso(id, raiz.izquierda,no_anio,no_semestre,curso)
            self.insertar_curso(id, raiz.derecha,no_anio,no_semestre,curso)


    def graficar_arbol_cursos(self,id,raiz,no_anio,no_semestre):
        if raiz is not None:
            if str(raiz.usuario.id) == str(id):
                raiz.usuario.lista_de_anios.graficar_arbol_cursos(no_anio,no_semestre)
            self.graficar_arbol_cursos(id, raiz.izquierda,no_anio,no_semestre)
            self.graficar_arbol_cursos(id, raiz.derecha,no_anio,no_semestre)


    def imprimir_lista(self, raiz):
        if raiz is not None:
            print("-----------------------------------------------------------------")
            print(raiz.usuario.id)
            self.imprimir_lista(raiz.izquierda)
            self.imprimir_lista(raiz.derecha)