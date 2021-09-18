from nodo_avl import Nodo_avl

class Arbol_avl:
    def __init__(self):
        self.raiz = None


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
                return raiz
            elif id<raiz.id:
                raiz.izquierda = self.insertar_nodo_posicion(nuevo, id, raiz.izquierda)
                return raiz
        else:
            raiz = nuevo
            return raiz

    def buscar_por_carnet(self,carnet,raiz):
        if raiz is not None:
            #print(str(raiz.estudiante.carnet)+" == "+ str(carnet))
            if str(raiz.estudiante.carnet) == str(carnet):
                print("Carnet: "+str(carnet))
                return raiz
            self.buscar_por_carnet(carnet, raiz.izquierda)
            self.buscar_por_carnet(carnet, raiz.derecha)


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


    def imprimir_lista(self, raiz):
        if raiz is not None:
            print("-----------------------------------------------------------------")
            print(raiz.estudiante.carnet)
            #print("**************AÑO***************")
            #raiz.estudiante.lista_de_anios.imprimir_lista()
            #print("**************MESES***************")
            raiz.estudiante.lista_de_anios.imprimir_meses()
            self.imprimir_lista(raiz.izquierda)
            self.imprimir_lista(raiz.derecha)






    def graficar(self):
        cadena = "digraph arbol {\n"
        if (self.raiz != None):
            cadena += self.listar(self.raiz)
            cadena += "\n"
            cadena += self.enlazar(self.raiz)
        cadena += "}"
        Archivo = open("ejemplo.dot", "w+")
        Archivo.write(cadena)
        Archivo.close()

    def listar(self, raiz_actual):
        if raiz_actual:
            cadena = "n" + str(raiz_actual.estudiante.carnet) + "[label= \"" + str(raiz_actual.estudiante.carnet) + "\"];\n"
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
