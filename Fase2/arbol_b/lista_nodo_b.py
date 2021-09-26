from arbol_b.nodo_b import nodo_b


class lista_nodo_b:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamanio = 0


    def insertar(self,nuevo_curso):
        nuevo_nodo = nuevo_curso
        if self.primero is None:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
            self.tamanio +=1
        else:
            if self.primero == self.ultimo:
                if nuevo_nodo.curso.codigo < self.primero.curso.codigo:
                    nuevo_nodo.siguiente = self.primero
                    self.primero.anterior = nuevo_nodo
                    self.primero.izquierda = nuevo_nodo.derecha
                    self.primero = nuevo_nodo
                    self.tamanio+=1
                    return True
                elif nuevo_nodo.curso.codigo > self.ultimo.curso.codigo:
                    self.ultimo.siguiente = nuevo_nodo
                    nuevo_nodo.anterior = self.ultimo
                    self.ultimo.derecha = nuevo_nodo.izquierda
                    self.ultimo = nuevo_nodo
                    self.tamanio+=1
                    return True
                else:
                    print("El codigo del curso ya se encuentra en la lista")
                    return False
            else:
                if nuevo_nodo.curso.codigo < self.primero.curso.codigo:
                    nuevo_nodo.siguiente = self.primero
                    self.primero.anterior = nuevo_nodo
                    self.primero.izquierda = nuevo_nodo.derecha
                    self.primero = nuevo_nodo
                    self.tamanio+=1
                    return True
                elif nuevo_nodo.curso.codigo > self.ultimo.curso.codigo:
                    self.ultimo.siguiente = nuevo_nodo
                    nuevo_nodo.anterior = self.ultimo
                    self.ultimo.derecha = nuevo_nodo.izquierda
                    self.ultimo = nuevo_nodo
                    self.tamanio+=1
                    return True
                else:
                    tmp = self.primero
                    while tmp is not None:
                        if nuevo_nodo.curso.codigo < tmp.curso.codigo:
                            nuevo_nodo.siguiente = tmp
                            nuevo_nodo.anterior = tmp.anterior

                            tmp.izquierda = nuevo_nodo.derecha
                            tmp.anterior.derecha = nuevo_nodo.izquierda

                            tmp.anterior.siguiente = nuevo_nodo
                            tmp.anterior = nuevo_nodo
                            self.tamanio+= 1
                            return True
                        elif nuevo_nodo.curso.codigo == tmp.curso.codigo:
                            print("El codigo del curso ya se encuentra en la lista")
                            return False
                        else:
                            tmp = tmp.siguiente
        return False

