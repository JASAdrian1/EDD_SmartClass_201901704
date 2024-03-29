from matriz_dispersa.lista_cabecera import lista_cabecera
from matriz_dispersa.nodo_cabecera import nodo_cabecera
from graphviz import Graph, Digraph, Source
from operator import itemgetter


class matriz:
    def __init__(self):
        self.cabeceras_filas = lista_cabecera()
        self.cabeceras_columnas = lista_cabecera()


    def insertar(self,tarea,posx,posy,tipo_operacion=None,id_tarea=None):
        #Validacion hecha para determinar si la operacion es insercion o modificacion
        if tipo_operacion is True:
            self.modificar_tarea(tarea,posx,posy,id_tarea)
        else:
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

    def eliminar(self,posx,posy,id):
        print("Se elimino tarea en dia: ",posy," y hora: ",posx)
        tmp = self.cabeceras_filas.primero
        while tmp is not None:
            print(posx, " == ",tmp.id)
            #print(type(posx),type(tmp.id),sep="\n")
            if str(posx) == tmp.id:
                tmp_dato = tmp.lista_interna.primero
                while tmp_dato is not None:
                    print(posy," == ",tmp_dato.posy)
                    if str(tmp_dato.posy) == str(posy):
                        tmp_dato.tareas.eliminar(id)
                        return
                    tmp_dato = tmp_dato.siguiente
            tmp = tmp.siguiente
        print("No se ha encontrado la fecha especificada (eliminar - matriz)")


    def modificar_tarea(self,tarea,posx,posy,id):
        print("Se modifico la tarea en dia: ", posy, " y hora: ", posx)
        tmp = self.cabeceras_filas.primero
        while tmp is not None:
            # print(type(posx),type(tmp.id),sep="\n")
            if str(posx) == tmp.id:
                tmp_dato = tmp.lista_interna.primero
                while tmp_dato is not None:
                    #print(posy, " == ", tmp_dato.posy)
                    if str(tmp_dato.posy) == str(posy):
                        tmp_dato.tareas.modificar(tarea,id)
                        return
                    tmp_dato = tmp_dato.siguiente
            tmp = tmp.siguiente
        print("No se ha encontrado la fecha especificada (modificar_tarea - matriz)")

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

        #SE GRAFICAN LA CABECERA DE LAS FILAS
        nodo_cabecera_fila =self.cabeceras_filas.primero
        cadena+="subgraph cabecera_fila{\n"
        cadena+='rank="same";\n'
        #SE CONECTA EL NODO RAIZ CON LA CABECERA FILA
        cadena += '"" -> f' + str(nodo_cabecera_fila.id) + "\n"
        # SE GRAFICAN LA UNION DE LA CABECERA DE LAS FILAS
        while nodo_cabecera_fila is not None:
            if nodo_cabecera_fila.siguiente is None:
                cadena += 'f' + str(nodo_cabecera_fila.id)
            else:
                cadena += 'f' + str(nodo_cabecera_fila.id) + '->'
            nodo_cabecera_fila = nodo_cabecera_fila.siguiente
        cadena+=";\n}\n"

        #SE GRAFICAN LA UNION DE LA CABECERA DE LAS COLUMNAS
        cadena += "subgraph cabecera_columna{\n"
        cadena += 'rankdir="LR";\n'
        nodo_cabecera_columna = self.cabeceras_columnas.primero
        while nodo_cabecera_columna.siguiente is not None:
            cadena += 'c' + str(nodo_cabecera_columna.id) + '-> c' + str(nodo_cabecera_columna.siguiente.id) + "\n"
            nodo_cabecera_columna = nodo_cabecera_columna.siguiente
        cadena+="\n}\n"

        #CREACION DE LOS NODOS INTERNOS DE LA MATRIZ
        nodo_cabecera_fila = self.cabeceras_filas.primero
        lista_nodo_internos = [] #LISTA PARA GUARDAR TODOS LOS NODOS PARA RECORRER POSTERIORMENTE
        while nodo_cabecera_fila is not None:
            tmp_dato_interno = nodo_cabecera_fila.lista_interna.primero
            while tmp_dato_interno is not None:
                cadena += "ni" + str(tmp_dato_interno.posx) +str(tmp_dato_interno.posy) + '[label="' + str(tmp_dato_interno.tareas.longitud())+'"]\n'
                lista_nodo_internos.append(["ni" + str(tmp_dato_interno.posx) +str(tmp_dato_interno.posy),tmp_dato_interno.posx,tmp_dato_interno.posy])
                #print(tmp_dato_interno.posx,", ",tmp_dato_interno.posy)
                tmp_dato_interno = tmp_dato_interno.siguiente
            nodo_cabecera_fila = nodo_cabecera_fila.siguiente

        # SE CONECTA EL NODO RAIZ CON LA CABECERA COLUMNA
        nodo_cabecera_columna = self.cabeceras_columnas.primero
        cadena += '"" -> c' + str(nodo_cabecera_columna.id) + "[rank = same]\n"

        contador = 0
        ultimo_nodo = ""
        cerrar_grafo = False
        print(lista_nodo_internos)
        #RECORRIDO PARA GRAFICAR LOS NODOS VERTICALEMTE
        for j in range(0,31,1):
            for i in range(0,24,1):
                for k in range(0, len(lista_nodo_internos)):
                    if(type(lista_nodo_internos[k][1]) == str):
                        lista_nodo_internos[k][1] =int(lista_nodo_internos[k][1])
                    if (type(lista_nodo_internos[k][2]) == str):
                        lista_nodo_internos[k][2] = int(lista_nodo_internos[k][2])
                    #print(type(lista_nodo_internos[k][2]))
                    #print(lista_nodo_internos[k][1]," == ",i," ---- ",lista_nodo_internos[k][2]," == ",j)
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

        # RECORRIDO PARA GRAFICAR LOS NODOS HOLRIZONTALMENTE
        for i in range(0,24,1):
            for j in range(0,31,1):
                if (type(lista_nodo_internos[k][1]) == str):
                    lista_nodo_internos[k][1] = int(lista_nodo_internos[k][1])
                if (type(lista_nodo_internos[k][2]) == str):
                    lista_nodo_internos[k][2] = int(lista_nodo_internos[k][2])
                for k in range(0, len(lista_nodo_internos)):
                    if lista_nodo_internos[k][1] == i and lista_nodo_internos[k][2] == j:
                        if contador == 0: #Contador para ver si se debe conenctar con la cabecera o no
                            cadena+="f"+str(i)+" -> "+lista_nodo_internos[k][0]+"\n"
                            ultimo_nodo = lista_nodo_internos[k][0]
                            contador+=1
                        else:
                            cadena+=ultimo_nodo+"->"+lista_nodo_internos[k][0]+"[rank=\"same\"]\n"
                        #cadena+="c"+str(j)+" -> "+lista_nodo_internos[k][0]+"\n"
            ultimo_nodo = ""
            contador = 0

        return cadena


    def get_posx(self,elemento):
        return elemento[1]

    #Metodo para peticion get de recordatorios
    def get_informacion_tareas(self,dia,hora):
        if type(dia) == str:
            dia=int(dia)
        if type(hora) == str:
            hora=int(hora)
        tmp = self.cabeceras_filas.primero
        while tmp is not None:
            subtmp = tmp.lista_interna.primero  #Se accede a lista interna dentro del nodo cabecera
            while subtmp is not None:
                #print(subtmp.posx," == ",hora," ---- ",subtmp.posy, " == " ,dia)
                if type(subtmp.posx == str):
                    subtmp.posx = int(subtmp.posx)
                if type(subtmp.posy == str):
                    subtmp.posy = int(subtmp.posy)
                if subtmp.posx == hora and subtmp.posy == dia:
                    #print("Hora: ",subtmp.posx," Dia: ",subtmp.posy)
                    return subtmp.tareas.get_reporte_tareas()
                subtmp = subtmp.siguiente
            tmp = tmp.siguiente

    def graficar_tareas(self, dia, hora):
        if type(dia) == str:
            dia = int(dia)
        if type(hora) == str:
            hora = int(hora)
        tmp = self.cabeceras_filas.primero
        while tmp is not None:
            subtmp = tmp.lista_interna.primero  # Se accede a lista interna dentro del nodo cabecera
            while subtmp is not None:
                if type(subtmp.posx == str):
                    subtmp.posx = int(subtmp.posx)
                if type(subtmp.posy == str):
                    subtmp.posy = int(subtmp.posy)
                if subtmp.posx == hora and subtmp.posy == dia:
                    subtmp.tareas.graficar()
                    break
                    break
                subtmp = subtmp.siguiente
            tmp = tmp.siguiente

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



