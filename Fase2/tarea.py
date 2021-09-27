from Analizadores.sintactico import parser
from anio import anio



class tarea:
    def __init__(self, carnet, nombre, descripcion, materia, estado, fecha, anio, mes, dia, hora):
        self.carnet = carnet
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado
        self.fecha = fecha
        self.anio = anio
        self.mes = mes
        self.dia = dia
        self.hora = hora
        self.materia = materia


class anio:
    def __init__(self, no_anio, semestre=None, meses=None):
        self.no_anio = no_anio
        self.semestre = semestre
        self.meses = meses


def cargar_tareas(texto,arbol_estudiantes):
    texto_analizado = parser.parse(texto)
    for item in texto_analizado:
        if item['type'] == "task":
            for atributo in item['atributos']:
                try:
                    for key in list(atributo):
                        if key == "Carnet":
                            carnet = atributo['Carnet']
                        elif key == "Nombre":
                            nombre = atributo['Nombre']
                        elif key == "Descripcion":
                            descripcion = atributo['Descripcion']
                        elif key == "Materia":
                            materia = atributo['Materia']
                        elif key == "Fecha":
                            fecha = atributo['Fecha']
                        elif key == "Hora":
                            hora = atributo['Hora']
                        elif key == "Estado":
                            estado = atributo['Estado']
                except:
                    print(atributo)
                    print("La estructura de este estudiante no era la correcta")
            carnet = carnet[1:-1]
            nombre = nombre[1:-1]
            descripcion = descripcion[1:-1]
            materia = materia[1:-1]
            fecha = fecha[1:-1]
            hora = hora[1:-1]
            estado = estado[1:-1]
            #SE HACE SPLIT A LA FECHA PARA SACAR EL AÑO Y EL MES
            no_anio = fecha.split("/")[2]
            no_mes = fecha.split("/")[1]
            dia = fecha.split("/")[0]

            nueva_tarea = tarea(carnet,nombre,descripcion,materia,estado,fecha,no_anio,no_mes,dia,hora)
            arbol_estudiantes.insertar_anio(carnet, arbol_estudiantes.raiz, no_anio)

            arbol_estudiantes.insertar_mes(carnet, arbol_estudiantes.raiz, no_anio, no_mes)
            arbol_estudiantes.insertar_tarea(carnet, arbol_estudiantes.raiz, no_anio, no_mes,nueva_tarea)




    """texto_analizado = parser.parse(texto)
        for item in texto_analizado:
            if item['type'] == "task":
                contador = 0
                for atributo in item['atributos']:
                    try:
                        if contador == 0:
                            carnet = atributo['Carnet']
                        if contador == 1:
                            nombre = atributo['Nombre']
                        if contador == 2:
                            descripcion = atributo['Descripcion']
                        if contador == 3:
                            materia = atributo['Materia']
                        if contador == 4:
                            fecha = atributo['Fecha']
                        if contador == 5:
                            hora = atributo['Hora']
                        if contador == 6:
                            estado = atributo['Estado']
                        contador += 1
                    except:
                        print(atributo)
                        print("La estructura de este estudiante no era la correcta")
                carnet = carnet[1:-1]
                nombre = nombre[1:-1]
                descripcion = descripcion[1:-1]
                materia = materia[1:-1]
                fecha = fecha[1:-1]
                hora = hora[1:-1]
                estado = estado[1:-1]
                #SE HACE SPLIT A LA FECHA PARA SACAR EL AÑO
                no_anio = fecha.split("/")[2]
                arbol_estudiantes.insertar_anio(carnet,arbol_estudiantes.raiz,no_anio)"""