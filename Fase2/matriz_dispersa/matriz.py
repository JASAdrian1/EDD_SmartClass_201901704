from matriz_dispersa.lista_cabecera import lista_cabecera

class matriz:
    def __init__(self):
        self.cabeceras_filas = lista_cabecera()
        self.cabeceras_columnas = lista_cabecera()


    def insertar(self,tarea,posx,posy):
        nodo_cabecera_x = None
        nodo_cabecera_y = None

        if self.cabeceras_filas and self.cabeceras_columnas:
            print("Hola")