

class lista_cabecera:
    def __init__(self):
        self.primero = None


    def insertar(self, nuevo_nodo):
        if self.primero is None:
            self.primero = nuevo_nodo
        else:
            if nuevo_nodo.id < self.primero.id:
                nuevo_nodo.siguiente = self.primero
                self.primero.anterior = nuevo_nodo
                self.primero = nuevo_nodo
            else:
                tmp = self.primero
                while tmp is not None:
                    if nuevo_nodo.id<tmp.id:
                        nuevo_nodo.siguiente = tmp
                        nuevo_nodo.anterior = tmp.anterior
                        tmp.anterior.siguiente = nuevo_nodo
                        tmp.anterior = nuevo_nodo
                        break
                    aux = tmp
                    tmp = tmp.siguiente


                if aux.siguiente == None:
                    #print(">" + str(nuevo_nodo.id))
                    aux.siguiente = nuevo_nodo
                    nuevo_nodo.anterior = aux



    def buscarEncabezado(self,id):
        tmp=self.primero
        while tmp is not None:
            if tmp.id==id:
                return tmp
            tmp=tmp.siguiente
        return None


    def imprimir_encabezado(self):
        tmp=self.primero
        while tmp is not None:
            print(tmp.id)
            tmp=tmp.siguiente
        return None
