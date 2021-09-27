from flask import Flask, jsonify, request
from flask_cors import CORS
import estudiante
from arbol_avl import Arbol_avl
from arbol_b.arbol_b_cursos import Arbol_B
import tarea
import json

arbol_estudiantes = Arbol_avl()
arbol_pensum = Arbol_B()
info_estudiante = []
lista_reportes_tareas = []


app = Flask(__name__)
CORS(app)

@app.route("/", methods =['GET'])
def inicio():
    return "El servidor flask está funcionando"


@app.route("/carga", methods =['POST'])
def cargar():
    import io
    global arbol_estudiantes
    path = request.json['path']
    tipoArchivo = request.json['tipo']
    file = open(path)
    texto = file.read()
    if tipoArchivo == "estudiante" or tipoArchivo == "recordatorio":
        estudiante.cargarEstudiantes(texto,arbol_estudiantes)
        print("Se han cargado los estudiantes")
        tarea.cargar_tareas(texto, arbol_estudiantes)
        print("Se han cargado las tareas")
        #arbol_estudiantes.imprimir_lista(arbol_estudiantes.raiz)
    elif tipoArchivo == "curso":
        from arbol_b.curso import cargar_cursos
        file = open(path, encoding="latin-1")
        texto = file.read()
        texto = json.loads(texto)
        cargar_cursos(texto,arbol_estudiantes,arbol_pensum)

    return jsonify({"Mensaje":"Se ha realizado la carga correctamente"})

#*************METODOS PARA ARBOL ESTUDIANTE******************
@app.route("/estudiante",methods=['POST'])
def insertar_estudiante():
    global arbol_estudiantes
    carnet = request.json['carnet']
    dpi = request.json['DPI']
    nombre = request.json['nombre']
    carrera = request.json['carrera']
    correo = request.json['correo']
    password = request.json['password']
    creditos = request.json['creditos']
    edad = request.json['edad']
    nuevo_estudiante = estudiante.Estudiante(carnet,dpi,nombre,carrera,password,creditos,edad)
    nuevo_estudiante.correo = correo
    arbol_estudiantes.insertar(nuevo_estudiante,carnet)
    return jsonify({"Mensaje": "Se ha agregado al estudiante correctamente"})

@app.route("/estudiante",methods=['UPDATE'])
def modificar_estudiante():
    global arbol_estudiantes
    carnet = request.json['carnet']
    dpi = request.json['DPI']
    nombre = request.json['nombre']
    carrera = request.json['carrera']
    correo = request.json['correo']
    password = request.json['password']
    creditos = request.json['creditos']
    edad = request.json['edad']
    nuevo_estudiante = estudiante.Estudiante(carnet, dpi, nombre, carrera, password, creditos, edad)
    nuevo_estudiante.correo = correo
    arbol_estudiantes.modificar(nuevo_estudiante)
    return jsonify({"Mensaje": "Se ha modificado al estudiante correctamente"})

@app.route("/estudiante",methods=['GET'])
def get_estudiante():
    global arbol_estudiantes
    global info_estudiante
    carnet = request.json['carnet']
    arbol_estudiantes.get_informacion_estudiante(carnet,arbol_estudiantes.raiz,info_estudiante)
    if len(info_estudiante)>0:
        print(info_estudiante[0])
        return info_estudiante[0]
    else:
        return {'Mensaje':'No se ha encontrado al estudiante'}

@app.route("/estudiante",methods=['DELETE'])
def eliminar_estudiante():
    global arbol_estudiantes
    carnet = request.json['carnet']
    arbol_estudiantes.eliminar(carnet)
    return {"Mensaje":"Se ha eliminado al estudiante con exito"}


#*********METODOS PARA TAREAS******************
#Crear recordatorio
@app.route("/recordatorios",methods=['POST'])
def crear_recordatorios():
    global arbol_estudiantes
    carnet = request.json['Carnet']
    nombre = request.json['Nombre']
    descripcion = request.json['Descripcion']
    materia = request.json['Materia']
    fecha = request.json['Fecha']
    hora = request.json['Hora']
    estado = request.json['Estado']
    no_anio = fecha.split("/")[2]
    no_mes = fecha.split("/")[1]
    dia = fecha.split("/")[0]
    nueva_tarea = tarea.tarea(carnet,nombre,descripcion,materia,estado,fecha,no_anio,no_mes,dia,hora)
    arbol_estudiantes.insertar_anio(carnet, arbol_estudiantes.raiz, no_anio)
    arbol_estudiantes.insertar_mes(carnet, arbol_estudiantes.raiz, no_anio, no_mes)
    arbol_estudiantes.insertar_tarea(carnet, arbol_estudiantes.raiz, no_anio, no_mes, nueva_tarea)

    return {'Mensaje':'Se ha guardado la tarea exitosamente'}


#Conseguir informacion tarea
@app.route("/recordatorios",methods=['GET'])
def get_info_tarea():
    global arbol_estudiantes
    global lista_reportes_tareas
    carnet = request.json['Carnet']
    fecha = request.json['Fecha']
    hora = request.json['Hora']
    no_anio = fecha.split("/")[2]
    no_mes = fecha.split("/")[1]
    dia = fecha.split("/")[0]
    arbol_estudiantes.get_informacion_tareas(carnet,arbol_estudiantes.raiz,no_anio,no_mes,dia,hora,lista_reportes_tareas)
    if len(lista_reportes_tareas)>0:
        json_tareas = jsonify(lista_reportes_tareas)
        return json_tareas
    return {'Mensaje':'No se ha encontrado ninguna tarea que coincida con los datos proporcionados'}


#****************REPORTES***********************
@app.route("/reporte", methods =['GET'])
def graficar():
    tipo_grafica = request.json['tipo']
    if tipo_grafica == 0:
        arbol_estudiantes.graficar()
    elif tipo_grafica == 1:
        carnet = request.json['carnet']
        anio = request.json['año']
        mes = request.json['mes']
        arbol_estudiantes.graficar_matriz_dispersa(carnet,arbol_estudiantes.raiz,anio,mes)
    elif tipo_grafica == 2:
        carnet = request.json['carnet']
        anio = request.json['año']
        mes = request.json['mes']
        dia = request.json['dia']
        hora = request.json['hora']
        arbol_estudiantes.graficar_tareas(carnet, arbol_estudiantes.raiz, anio, mes, dia, hora)
    elif tipo_grafica == 3:
        arbol_pensum.graficar()
    elif tipo_grafica == 4:
        carnet = request.json['carnet']
        anio = request.json['año']
        semestre = request.json['semestre']
        arbol_estudiantes.graficar_arbol_cursos(carnet,arbol_estudiantes.raiz,anio,semestre)
    return {'Mensaje':'Se ha graficado el arbol correctamente'}


if __name__=="__main__":
    import os
    if os.path.exists(r"C:\Users\Adrian Aguilar\Desktop\Reportes_F2") is not True:
        os.mkdir(r"C:\Users\Adrian Aguilar\Desktop\Reportes_F2")
    app.run(port=3000, debug=True)