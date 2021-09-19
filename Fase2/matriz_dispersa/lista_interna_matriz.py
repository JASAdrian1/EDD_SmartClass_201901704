from matriz_dispersa.nodo_interno import nodo_interno_matriz

class lista_interna_matriz:
    def __init__(self):
        self.primero = None

    def insertarx(self,tarea,x,y):
        nuevo_nodo = nodo_interno_matriz(tarea,x,y)
        if self.primero is not None:
            if nuevo_nodo.posy< self.primero.posy:
                #print("Se inserto ", tarea.materia)
                nuevo_nodo.siguiente = self.primero
                self.primero.anterior = nuevo_nodo
                self.primero = nuevo_nodo
            else:
                #ARREGLAR ESTA SECCION
                tmp = self.primero
                while tmp is not None:
                    if nuevo_nodo.posy < tmp.posy:
                        print("Se inserto ", tarea.materia)
                        nuevo_nodo.siguiente = tmp
                        nuevo_nodo.anterior = tmp.anterior
                        tmp.anterior.siguinte = nuevo_nodo
                        tmp.anterior = nuevo_nodo
                        break
                    #Si el nodo ya existe únicamente se inserta la tarea dentro de la lista de
                    #tareas del nodo existente
                    elif nuevo_nodo.posx == tmp.posx and nuevo_nodo.posy == tmp.posy:
                        #print("Se inserto ", tarea.materia)
                        tmp.tareas.insertar(tarea)
                        break
                    else:
                        if tmp.siguiente == None:
                            #print("Se inserto ", tarea.materia)
                            tmp.siguiente = nuevo_nodo
                            nuevo_nodo.anterior = tmp
                            break
                        else:
                            tmp = tmp.siguiente

        else:
            #print("Se inserto ", tarea.materia)
            self.primero = nuevo_nodo

    def insertary(self, tarea, x, y):
        nuevo_nodo = nodo_interno_matriz(tarea, x, y)
        if self.primero is not None:
            if nuevo_nodo.posx < self.primero.posx:
                nuevo_nodo.abajo = self.primero
                self.primero.arriba = nuevo_nodo
                self.primero = nuevo_nodo
            else:
                tmp = self.primero
                while tmp is not None:
                    if nuevo_nodo.posx < tmp.posx:
                        nuevo_nodo.abajo = tmp
                        nuevo_nodo.arriba = tmp.arriba
                        tmp.arriba.abajo = nuevo_nodo
                        tmp.arriba = nuevo_nodo
                        break
                    # Si el nodo ya existe únicamente se inserta la tarea dentro de la lista de
                    # tareas del nodo existente
                    elif nuevo_nodo.posx == tmp.posx and nuevo_nodo.posy == tmp.posy:
                        tmp.tareas.insertar(tarea)
                        break
                    else:
                        if tmp.abajo == None:
                            tmp.abajo = nuevo_nodo
                            nuevo_nodo.arriba = tmp
                            break
                        else:
                            tmp = tmp.siguiente

        else:
            self.primero = nuevo_nodo
