
from nodo_anio import nodo_anio
from matriz_dispersa.mes import mes

class lista_anios:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def lista_vacia(self):
        if self.primero is None:
            return True
        else:
            return False


    def insertar(self,anio):
        nuevo_nodo = nodo_anio(anio)
        if self.lista_vacia():
            self.primero = nuevo_nodo
        else:
            tmp = self.primero
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            if self.verificar_anio_repetido(nuevo_nodo.anio.no_anio) is False:
                tmp.siguiente = nuevo_nodo

    def insertar_mes(self,no_anio,no_mes):
        #print("Año: "+no_anio+" Mes: "+no_mes)
        tmp = self.primero
        nuevo_mes = mes(no_mes)
        while tmp is not None:
            #print(no_anio + " == " + tmp.anio.no_anio)
            if no_anio == tmp.anio.no_anio:
                tmp.meses.insertar(nuevo_mes)
            tmp = tmp.siguiente

    def insertar_tarea(self, no_anio, no_mes, tarea):
        tmp = self.primero
        while tmp is not None:
            if no_anio == tmp.anio.no_anio:
                tmp.meses.insertar_tarea(no_mes, tarea)
            tmp = tmp.siguiente

    def verificar_anio_repetido(self,anio):
        tmp = self.primero
        if tmp is not None:
            while tmp is not None:
                if anio == tmp.anio.no_anio:
                    return True
                tmp = tmp.siguiente
            return False
        else:
            return False
        return False


    def imprimir_lista(self):
        tmp = self.primero
        if tmp is not None:
            while tmp is not None:
                print(tmp.anio.no_anio)
                tmp = tmp.siguiente
        else:
            print("La lista para este estudiante esta vacia")

    def imprimir_meses(self):
        tmp = self.primero
        if tmp is not None:
            while tmp is not None:
                print("**************AÑO***************")
                print(tmp.anio.no_anio)
                print("**************MESES***************")
                tmp.meses.imprimir_meses()
                tmp = tmp.siguiente
        else:
            print("La lista para este estudiante esta vacia")

    def imprimir_tareas(self):
        tmp = self.primero
        if tmp is not None:
            while tmp is not None:
                tmp.meses.imprimir_tareas()
                tmp = tmp.siguiente
        else:
            print("La lista para este estudiante esta vacia")

    def tamanio_lista(self):
        contador = 0
        tmp = self.primero
        if tmp is not None:
            while tmp is not None:
                contador+=1
                tmp = tmp.siguiente
            return contador
        else:
            print("La lista para este estudiante esta vacia")
