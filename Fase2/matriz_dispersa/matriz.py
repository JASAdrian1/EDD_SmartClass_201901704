from matriz_dispersa.lista_cabecera import lista_cabecera
from matriz_dispersa.nodo_cabecera import nodo_cabecera

class matriz:
    def __init__(self):
        self.cabeceras_filas = lista_cabecera()
        self.cabeceras_columnas = lista_cabecera()


    def insertar(self,tarea,posx,posy):
        if self.cabeceras_filas is not None and self.cabeceras_columnas is not None:
            nodo_cabecera_x = self.cabeceras_filas.buscarEncabezado(posx)
            nodo_cabecera_y = self.cabeceras_columnas.buscarEncabezado(posy)

        if nodo_cabecera_x == None:
            nodo_cabecera_x = nodo_cabecera(posx)
            self.cabeceras_filas.insertar(nodo_cabecera_x)

        if nodo_cabecera_y == None:
            nodo_cabecera_y = nodo_cabecera(posy)
            self.cabeceras_columnas.insertar(nodo_cabecera_y)

        nodo_cabecera_x.lista_interna.insertarx(tarea,posx,posy)
        nodo_cabecera_y.lista_interna.insertary(tarea, posx, posy)

    def imprimir_matriz(self):
        print("**************HORAS*************")
        tmp = self.cabeceras_filas.primero
        while tmp is not None:
            print(">>HORA: ",tmp.id)
            subtmp = tmp.lista_interna.primero  #Se accede a lista interna dentro del nodo cabecera
            while subtmp is not None:
                subtmp.tareas.imprimir_lista()
                subtmp = subtmp.siguiente
            tmp = tmp.siguiente


        print("**************DIAS*************")
        tmp = self.cabeceras_columnas.primero
        while tmp is not None:
            print(">>DIA: ",tmp.id)
            subtmp = tmp.lista_interna.primero  #Se accede a lista interna dentro del nodo cabecera
            while subtmp is not None:
                subtmp.tareas.imprimir_lista()
                subtmp = subtmp.abajo
            tmp = tmp.siguiente



