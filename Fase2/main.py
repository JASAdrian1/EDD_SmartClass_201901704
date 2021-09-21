from flask import Flask, jsonify, request
from flask_cors import CORS
import estudiante
from arbol_avl import Arbol_avl
import tarea

arbol_estudiantes = Arbol_avl()
info_estudiante = []


app = Flask(__name__)
CORS(app)

@app.route("/", methods =['GET'])
def inicio():
    return "El servidor flask está funcionando"


@app.route("/carga", methods =['POST'])
def cargar():
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
        arbol_estudiantes.imprimir_lista(arbol_estudiantes.raiz)
    elif tipoArchivo == "curso":
        print("Sen han cargado los cursos")

    return jsonify({"Mensaje":"Se ha realizado la carga correctamente"})

#*********METODOS PARA ARBOL ESTUDIANTE
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
    print(info_estudiante[0])
    return info_estudiante[0]

@app.route("/estudiante",methods=['DELETE'])
def eliminar_estudiante():
    global arbol_estudiantes
    carnet = request.json['carnet']
    arbol_estudiantes.eliminar(carnet)
    return {"Mensaje":"Se ha eliminado al estudiante con exito"}


@app.route("/recordatorios",methods=['GET'])
def get_info_tarea():
    print("PENDIENTE")
    return {'Mensaje':'Pendiente'}

@app.route("/reporte", methods =['GET'])
def graficar():
    tipo_grafica = request.json['tipo']
    if tipo_grafica == 0:
        arbol_estudiantes.graficar()
    return {'Mensaje':'Se ha graficado el arbol correctamente'}


if __name__=="__main__":
    import os
    if os.path.exists(r"C:\Users\Adrian Aguilar\Desktop\Reportes_F2") is not True:
        os.mkdir(r"C:\Users\Adrian Aguilar\Desktop\Reportes_F2")
    app.run(port=3000, debug=True)