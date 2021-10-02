
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

    def insertar_tarea(self, no_anio, no_mes, tarea,tipo_operacion = None,id_tarea=None):
        tmp = self.primero
        while tmp is not None:
            if no_anio == tmp.anio.no_anio:
                tmp.meses.insertar_tarea(no_mes, tarea,tipo_operacion,id_tarea)
            tmp = tmp.siguiente

    def buscar_tarea(self, no_anio, no_mes, tarea):
        tmp = self.primero
        while tmp is not None:
            if no_anio == tmp.anio.no_anio:
                tmp.meses.buscar_tarea(no_mes, tarea)
            tmp = tmp.siguiente

    def graficar_matriz_dispersa(self, no_anio, no_mes):
        tmp = self.primero
        while tmp is not None:
            if no_anio == tmp.anio.no_anio:
                tmp.meses.graficar_matriz_dispersa(no_mes)
            tmp = tmp.siguiente

    def get_informacion_tareas(self, no_anio, no_mes,dia,hora):
        tmp = self.primero
        while tmp is not None:
            if no_anio == tmp.anio.no_anio:
                return tmp.meses.get_informacion_tareas(no_mes,dia,hora)
            tmp = tmp.siguiente
        print("No se ha encontrado la tarea (Funcion get_informacion_tareas -- lista_anios)")


    def eliminar_tarea(self, no_anio, no_mes,dia,hora,id):
        #print("Ingreso al metodo eliminar tarea en la lista de años")
        tmp = self.primero
        while tmp is not None:
            if no_anio == tmp.anio.no_anio:
                return tmp.meses.eliminar_tarea(no_mes,dia,hora,id)
            tmp = tmp.siguiente
        print("No se ha encontrado la tarea (Funcion get_informacion_tareas -- lista_anios)")

    def graficar_tareas(self, no_anio, no_mes,dia,hora):
        tmp = self.primero
        while tmp is not None:
            if no_anio == tmp.anio.no_anio:
                return tmp.meses.graficar_tareas(no_mes,dia,hora)
            tmp = tmp.siguiente

    def insertar_semestre(self, no_anio, no_semestre):
        # print("Año: "+no_anio+" Mes: "+no_mes)
        tmp = self.primero
        while tmp is not None:
            # print(no_anio + " == " + tmp.anio.no_anio)
            if no_anio == tmp.anio.no_anio:
                #print("Se inserto en el año ",no_anio)
                tmp.semestres.insertar(no_semestre)
            tmp = tmp.siguiente

    def insertar_curso(self, no_anio, no_semestre,curso):
        tmp = self.primero
        while tmp is not None:
            # print(no_anio + " == " + tmp.anio.no_anio)
            if no_anio == tmp.anio.no_anio:
                #print("Se inserto en el año ",no_anio)
                tmp.semestres.insertar_curso(no_semestre,curso)
            tmp = tmp.siguiente

    def graficar_arbol_cursos(self, no_anio, no_semestre):
        tmp = self.primero
        while tmp is not None:
            if no_anio == tmp.anio.no_anio:
                tmp.semestres.graficar_arbol_cursos(no_semestre)
                return
            tmp = tmp.siguiente
        print("No se ha podido graficar ya que no se ha encontrado el año")


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
