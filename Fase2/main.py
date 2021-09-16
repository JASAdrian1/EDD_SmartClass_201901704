from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import estudiante
from arbol_avl import Arbol_avl
from Analizadores.sintactico import parser


arbol_estudiantes = Arbol_avl()


app = Flask(__name__)
CORS(app)

@app.route("/", methods =['GET'])
def inicio():
    return "El servidor flask está funcionando"


@app.route("/carga", methods =['POST'])
def cargar():
    path = request.json['path']
    tipoArchivo = request.json['tipo']
    file = open(path)
    texto = file.read()
    if tipoArchivo == "estudiante" or tipoArchivo == "recordatorio":
        estudiante.cargarEstudiantes(texto)
        print("Se han cargado los estudiantes")

    elif tipoArchivo == "curso":
        print("Sen han cargado los cursos")


    return jsonify({"Mensaje":"Se ha realizado la carga correctamente"})



if __name__=="__main__":
    app.run(port=3000, debug=True)