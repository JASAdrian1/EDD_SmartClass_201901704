from graphviz import Source

from matriz_dispersa.nodo_tarea import nodo_tarea


class lista_tarea:
    def __init__(self):
        self.primero = None

    def insertar(self,tarea):
        nuevo_nodo = nodo_tarea(tarea)
        if self.primero is None:
            self.primero = nuevo_nodo
        else:
            tmp = self.primero
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo_nodo

    def longitud(self):
        contador = 0
        tmp = self.primero
        if tmp is not None:
            while tmp is not None:
                contador+=1
                tmp = tmp.siguiente
            return contador
        else:
            print("La lista para este estudiante esta vacia")

    def imprimir_lista(self):
        tmp = self.primero
        if tmp is not None:
            print("--Nueva lista")
            while tmp is not None:
                print(tmp.tarea.materia)
                tmp = tmp.siguiente
        else:
            print("La lista para este estudiante esta vacia")

    def get_reporte_tareas(self):
        lista_tareas = []
        tmp = self.primero
        if tmp is not None:
            while tmp is not None:
                tarea = {
                    "Nombre":tmp.tarea.nombre,
                    "Descripcion":tmp.tarea.descripcion,
                    "Materia":tmp.tarea.materia,
                    "Fecha":tmp.tarea.fecha,
                    "Hora":tmp.tarea.hora,
                    "Estado": tmp.tarea.estado
                }
                lista_tareas.append(tarea)
                tmp = tmp.siguiente
            return lista_tareas


    def graficar(self):
        cadena = "digraph arbol {\n"
        cadena += "rankdir=LR\n"
        if (self.primero != None):
            cadena += self.rellenar_graficar()
        cadena += "}"
        nombre_archivo = r'C:\Users\Adrian Aguilar\Desktop\Reportes_F2\grafica_tareas.dot'
        Archivo = open(nombre_archivo, "w+")
        Archivo.write(cadena)
        Archivo.close()
        try:
            s = Source.from_file(nombre_archivo)
            s.view()
        except:
            print("Por favor cierre el archivo de la grafica y vuelva a realizar la peticion")


    def rellenar_graficar(self):
        cadena = ""
        tmp = self.primero
        contador = 0
        lista_nodos = []
        while tmp is not None:
            cadena += "n" + str(contador) + "[label= \"" + tmp.tarea.materia+"\\n"+tmp.tarea.descripcion+"\\n"+tmp.tarea.estado+ "\" shape=\"rectangle\"];\n"
            lista_nodos.append("n" + str(contador))
            contador+=1
            tmp = tmp.siguiente
        if len(lista_nodos)>1:
            cadena+=lista_nodos[0]+" -> "+lista_nodos[1]+"\n"
            for i in range(2,len(lista_nodos),1):
                cadena+="->"+lista_nodos[i]+"\n"
        else:
            cadena += lista_nodos[0]
        return cadena

