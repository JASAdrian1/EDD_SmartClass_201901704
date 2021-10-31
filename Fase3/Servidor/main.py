from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from Usuarios.usuario import Usuario
from Usuarios import usuario
from Usuarios.arbol_avl import Arbol_avl


app = Flask(__name__)
CORS(app)

arbol_usuarios = Arbol_avl()
usuario_admin = Usuario("admin","0","admin","admin","admin","admin",0,"admin")
arbol_usuarios.insertar(usuario_admin,"0")

@app.route("/", methods =['GET'])
def inicio():
    arbol_usuarios.imprimir_lista(arbol_usuarios.raiz)
    return "El servidor flask está funcionando"


@app.route("/cargaUsuarios", methods =['POST'])
def cargarUsuarios():
    global arbol_usuarios
    contenidoArchivo = request.json['contenido']
    contenidoArchivo = json.loads(contenidoArchivo)
    usuario.cargarEstudiantes(contenidoArchivo,arbol_usuarios)
    arbol_usuarios.imprimir_usuarios(arbol_usuarios.raiz)
    print("Se han cargado los estudiantes")
    return jsonify({"Mensaje":"Se ha realizado la carga correctamente"})


@app.route("/login/",methods=['POST'])
def login():
    global arbol_usuarios
    usuario = str(request.json['usuario'])
    password = request.json['password']
    print(usuario)
    print(password)
    arbol_usuarios.login(usuario,password)
    if arbol_usuarios.validacion_login != None:
        rol = ""
        if arbol_usuarios.validacion_login.rol == "admin":
            rol = "admin"
            print("Ingreso como administrador")
        else:
            rol = "usuario"
            print("Ingreso correctamente")
        return jsonify({'Mensaje':'Ha ingresado correctamente','':True,'rol':rol})
    else:
        return jsonify({'Mensaje':'Los datos ingresados son incorrectos','ingresar':False,'rol':None})


@app.route("/registro/",methods=['POST'])
def registro_usuario():
    global arbol_usuarios
    carnet = request.json['carnet']
    dpi = request.json['dpi']
    nombre = request.json['nombre']
    carrera = request.json['carrera']
    correo = request.json['correo']
    edad = request.json['edad']
    password = request.json['password']
    nuevo_usuario = Usuario(carnet,dpi,nombre,carrera,correo,password,edad,"estudiante")
    arbol_usuarios.insertar(nuevo_usuario,carnet)
    arbol_usuarios.imprimir_usuarios(arbol_usuarios.raiz)
    return jsonify({'Mensaje': 'Se ha registrado correctamente'})


if __name__=="__main__":
    import os
    if os.path.exists(r"C:\Users\Adrian Aguilar\Desktop\Reportes_F3") is not True:
        os.mkdir(r"C:\Users\Adrian Aguilar\Desktop\Reportes_F3")
    app.run(port=3000, debug=True)