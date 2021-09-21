from matriz_dispersa.lista_cabecera import lista_cabecera
from matriz_dispersa.nodo_cabecera import nodo_cabecera
from graphviz import Graph, Digraph, Source


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

    def buscar_dato(self,posx,posy):
        tmp = self.cabeceras_filas.primero
        while tmp is not None:
            tmp_dato = tmp.lista_interna.primero
            while tmp_dato is not None:
                if tmp_dato.posx == posx and tmp_dato.posy:
                    tmp_tareas = tmp_dato.tareas.primero
                    #while tmp_tareas is not None:
                        #print(tmp_tareas.tarea.materia)
                        #tmp_tareas = tmp_tareas.siguiente
                    return tmp_dato
                tmp_dato = tmp_dato.siguiente
            tmp = tmp.siguiente

    def cantidad_datos(self):
        tmp = self.cabeceras_filas.primero
        contador = 0
        while tmp is not None:
            tmp_dato = tmp.lista_interna.primero
            while tmp_dato is not None:
                contador+=1
                tmp_dato = tmp_dato.siguiente
            tmp = tmp.siguiente

    def graficar_matriz(self):
        cadena = "digraph matriz{\n"
        cadena+= self.rellenar_grafica()
        cadena+="}"
        nombre_archivo = r'C:\Users\Adrian Aguilar\Desktop\Reportes_F2\grafica_matriz_tareas.dot'
        Archivo = open(nombre_archivo, "w+")
        Archivo.write(cadena)
        Archivo.close()
        s = Source.from_file(nombre_archivo)
        s.view()

    def rellenar_grafica(self):
        cadena = ""
        cadena+='rankdir ="LR"'
        nodo_cabecera_fila = self.cabeceras_filas.primero
        nodo_cabecera_columna = self.cabeceras_columnas.primero
        while nodo_cabecera_fila is not None:
            cadena+="f"+str(nodo_cabecera_fila.id)+'[label="'+str(nodo_cabecera_fila.id)+'"]\n'
            nodo_cabecera_fila = nodo_cabecera_fila.siguiente

        while nodo_cabecera_columna is not None:
            cadena += "c" + str(nodo_cabecera_columna.id) + '[label="' + str(nodo_cabecera_columna.id) + '"]\n'
            nodo_cabecera_columna = nodo_cabecera_columna.siguiente

        nodo_cabecera_fila =self.cabeceras_filas.primero
        #cadena+="rankdir='LR'\n"
        cadena+="subgraph cabecera_fila{\n"
        cadena+='rank="same";\n'
        cadena += '"" -> f' + str(nodo_cabecera_fila.id) + "\n"
        while nodo_cabecera_fila is not None:
            if nodo_cabecera_fila.siguiente is None:
                cadena += 'f' + str(nodo_cabecera_fila.id)
            else:
                cadena += 'f' + str(nodo_cabecera_fila.id) + '->'
            nodo_cabecera_fila = nodo_cabecera_fila.siguiente
        cadena+=";\n}\n"

        cadena += "subgraph cabecera_columna{\n"
        cadena += 'rankdir="LR";\n'
        nodo_cabecera_columna = self.cabeceras_columnas.primero
        while nodo_cabecera_columna.siguiente is not None:
            cadena += 'c' + str(nodo_cabecera_columna.id) + '-> c' + str(nodo_cabecera_columna.siguiente.id) + "\n"
            nodo_cabecera_columna = nodo_cabecera_columna.siguiente
        cadena+="\n}\n"

        nodo_cabecera_fila = self.cabeceras_filas.primero
        lista_nodo_internos = []
        while nodo_cabecera_fila is not None:
            tmp_dato_interno = nodo_cabecera_fila.lista_interna.primero
            while tmp_dato_interno is not None:
                cadena += "ni" + str(tmp_dato_interno.posx) +str(tmp_dato_interno.posy) + '[label="' + str(tmp_dato_interno.tareas.primero.tarea.materia)+'"]\n'
                lista_nodo_internos.append(("ni" + str(tmp_dato_interno.posx) +str(tmp_dato_interno.posy),tmp_dato_interno.posx,tmp_dato_interno.posy))
                #print(tmp_dato_interno.posx,", ",tmp_dato_interno.posy)
                tmp_dato_interno = tmp_dato_interno.siguiente
            nodo_cabecera_fila = nodo_cabecera_fila.siguiente

        nodo_cabecera_fila = self.cabeceras_filas.primero
        nodo_cabecera_columna = self.cabeceras_columnas.primero
        cadena += '"" -> c' + str(nodo_cabecera_columna.id) + "[rank = same]\n"

        contador = 0
        ultimo_nodo = ""
        cerrar_grafo = False
        for j in range(0,24,1):
            for i in range(0,30,1):
                for k in range(0, len(lista_nodo_internos)):
                    if lista_nodo_internos[k][1] == i and lista_nodo_internos[k][2] == j:
                        if contador == 0: #Contador para ver si se debe conenctar con la cabecera o no
                            cadena += "\nsubgraph dato_columna" + str(j) + "{\n"
                            cadena += 'rankdir="TB"\n'
                            cadena += "rank=same\n"
                            cadena+="c"+str(j)+" -> "+lista_nodo_internos[k][0]+"[rank=\"same\"]\n"
                            ultimo_nodo = lista_nodo_internos[k][0]
                            cerrar_grafo = True
                            contador+=1
                        else:
                            if contador == 1:
                                cadena+=ultimo_nodo+"->"+lista_nodo_internos[k][0]+""
                                contador+=1
                            else:
                                cadena+="->"+lista_nodo_internos[k][0]
                        #cadena+="c"+str(j)+" -> "+lista_nodo_internos[k][0]+"\n"
            if cerrar_grafo == True:
                cadena+="}\n"
                cerrar_grafo = False
            ultimo_nodo = ""
            contador = 0

        for i in range(0,24,1):
            for j in range(0,30,1):
                for k in range(0, len(lista_nodo_internos)):
                    if lista_nodo_internos[k][1] == i and lista_nodo_internos[k][2] == j:
                        if contador == 0: #Contador para ver si se debe conenctar con la cabecera o no
                            cadena+="f"+str(i)+" -> "+lista_nodo_internos[k][0]+"\n"
                            ultimo_nodo = lista_nodo_internos[k][0]
                            contador+=1
                        else:
                            cadena+=ultimo_nodo+"->"+lista_nodo_internos[k][0]+"\n"
                        #cadena+="c"+str(j)+" -> "+lista_nodo_internos[k][0]+"\n"
            ultimo_nodo = ""
            contador = 0

        return cadena


    def get_posx(self,elemento):
        return elemento[1]

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



