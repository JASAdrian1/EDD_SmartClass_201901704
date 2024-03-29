
from matriz_dispersa.nodo_mes import nodo_mes
from matriz_dispersa.nodo_tarea import nodo_tarea

class lista_mes:
    def __init__(self):
        self.primero = None

    def lista_vacia(self):
        if self.primero is None:
            return True
        return False

    def insertar(self,nuevo_mes):
        nuevo_nodo = nodo_mes(nuevo_mes)
        if self.lista_vacia():
            self.primero = nuevo_nodo
        else:
            tmp = self.primero
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            if self.verificar_mes_repetido(nuevo_mes.no_mes) is False:
                aux = tmp
                tmp.siguiente = nuevo_nodo
                tmp.anterior = aux

    def insertar_tarea(self,mes,tarea,tipo_operacion=None,id_tarea=None):
        tmp = self.primero
        while tmp is not None:
            if mes == tmp.mes.no_mes:
                #print(tarea.materia)
                tmp.matriz_tareas.insertar(tarea,tarea.hora,tarea.dia,tipo_operacion,id_tarea)
            tmp = tmp.siguiente

    def graficar_matriz_dispersa(self,mes):
        tmp = self.primero
        while tmp is not None:
            if str(mes) == tmp.mes.no_mes:
                tmp.matriz_tareas.graficar_matriz()
            tmp = tmp.siguiente

    def get_informacion_tareas(self,mes,dia,hora):
        tmp = self.primero
        while tmp is not None:
            if str(mes) == tmp.mes.no_mes:
                return tmp.matriz_tareas.get_informacion_tareas(dia,hora)
            tmp = tmp.siguiente

    def eliminar_tarea(self,mes,hora,dia,id):
        tmp = self.primero
        while tmp is not None:
            if str(mes) == tmp.mes.no_mes:
                return tmp.matriz_tareas.eliminar(dia,hora,id)
            tmp = tmp.siguiente

    def graficar_tareas(self,mes,dia,hora):
        tmp = self.primero
        while tmp is not None:
            if str(mes) == tmp.mes.no_mes:
                return tmp.matriz_tareas.graficar_tareas(dia,hora)
            tmp = tmp.siguiente

    def buscar_tarea(self,mes,tarea):
        tmp = self.primero
        while tmp is not None:
            if mes == tmp.mes.no_mes:
                print(tarea.materia)
                tmp.matriz_tareas.buscar_tarea(tarea.hora,tarea.dia)
            tmp = tmp.siguiente


    def imprimir_meses(self):
        tmp = self.primero
        if tmp is not None:
            while tmp is not None:
                print(tmp.mes.no_mes)
                tmp = tmp.siguiente
        else:
            print("La lista para este estudiante esta vacia")

    def imprimir_tareas(self):
        tmp = self.primero
        if tmp is not None:
            while tmp is not None:
                tmp.matriz_tareas.imprimir_matriz()
                tmp = tmp.siguiente
        else:
            print("La lista para este estudiante esta vacia")


    def verificar_mes_repetido(self,mes):
        tmp = self.primero
        if tmp is not None:
            while tmp is not None:
                if mes == tmp.mes.no_mes:
                    return True
                tmp = tmp.siguiente
            return False
        else:
            return False
        return False
