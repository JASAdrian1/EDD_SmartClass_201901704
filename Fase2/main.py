from flask import Flask, jsonify, request
from flask_cors import CORS
import estudiante
from arbol_avl import Arbol_avl
import tarea

arbol_estudiantes = Arbol_avl()


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



if __name__=="__main__":
    app.run(port=3000, debug=True)