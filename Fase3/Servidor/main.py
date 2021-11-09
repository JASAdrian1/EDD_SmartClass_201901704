from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from Usuarios.usuario import Usuario
from Usuarios import usuario
from Usuarios.arbol_avl import Arbol_avl
from Apuntes import apunte
from Apuntes.tabla_hash import Tabla_Hash
from Cursos import curso
from Cursos.grafo_cursos import Grafos_cursos


app = Flask(__name__)
CORS(app)

arbol_usuarios = Arbol_avl()
tabla_apuntes = Tabla_Hash()
grafo_pensum = Grafos_cursos()
usuario_admin = Usuario("admin","0","admin","admin","admin","admin",0,"admin")
arbol_usuarios.insertar(usuario_admin,"0")

@app.route("/", methods =['GET'])
def inicio():
    arbol_usuarios.imprimir_lista(arbol_usuarios.raiz)
    return "El servidor flask está funcionando"


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
        return jsonify({'Mensaje':'Ha ingresado correctamente','ingresar':True,'rol':rol})
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

@app.route("/admin/cargarUsuarios", methods =['POST'])
def cargarUsuarios():
    global arbol_usuarios
    contenidoArchivo = request.json['contenido']
    contenidoArchivo = json.loads(contenidoArchivo)
    usuario.cargarEstudiantes(contenidoArchivo,arbol_usuarios)
    arbol_usuarios.imprimir_usuarios(arbol_usuarios.raiz)
    arbol_usuarios.graficar()
    print("Se han cargado los estudiantes")
    return jsonify({"Mensaje":"Se ha realizado la carga correctamente"})

@app.route("/admin/graficarUsuarios", methods=['GET'])
def graficarUsuarios():
    global arbol_usuarios
    grafica = arbol_usuarios.graficar()
    return jsonify({"grafica":grafica})


@app.route("/admin/cargarApuntes", methods =['POST'])
def cargarApuntes():
    global tabla_apuntes
    contenidoArchivo = request.json['contenido']
    contenidoArchivo = json.loads(contenidoArchivo)
    apunte.cargarApuntes(contenidoArchivo,tabla_apuntes)
    tabla_apuntes.recorrer_tabla()
    print("Se han cargado los apuntes")
    return jsonify({"Mensaje":"Se ha realizado la carga correctamente"})

@app.route("/user/guardarApunte", methods =['POST'])
def guaradarApunte():
    global tabla_apuntes
    global arbol_usuarios
    user = request.json["usuario"]
    titulo = request.json["titulo"]
    contenido = request.json["contenido"]
    nuevo_apunte = apunte.Apunte(str(user),titulo,contenido)
    tabla_apuntes.insertar(str(user),nuevo_apunte)
    print("Se ha insertado el apunte")
    return jsonify({"Mensaje":"Se ha realizado la carga correctamente"})

@app.route("/user/listarApuntes/<string:user>", methods =['GET'])
def listarApuntes(user):
    global tabla_apuntes
    print(user)
    apuntes = tabla_apuntes.get_apuntes_usuario(user)
    print("Se listó los apuntes") 
    return jsonify({"apuntes":apuntes})

@app.route("/admin/graficarApuntes", methods=['GET'])
def graficarApuntes():
    global tabla_apuntes
    grafica = tabla_apuntes.graficar_apuntes()
    return jsonify({"grafica":grafica})


@app.route("/admin/cargarPensum", methods =['POST'])
def cargarPensum():
    global grafo_pensum
    global arbol_usuarios
    contenidoArchivo = request.json['contenido']
    contenidoArchivo = json.loads(contenidoArchivo)
    curso.cargar_cursos(contenidoArchivo,arbol_usuarios,grafo_pensum)
    grafo_pensum.graficar_grafo()
    print("Se han cargado el pensum")
    return jsonify({"Mensaje":"Se ha realizado la carga correctamente"})

@app.route("/admin/graficarPensum", methods=['GET'])
def graficarPensum():
    global grafo_pensum
    grafica = grafo_pensum.graficar_grafo()
    return jsonify({"grafica":grafica})

@app.route("/admin/reporteCursos", methods=['POST'])
def reporteCursos():
    global grafo_pensum
    id_curso = request.json["id_curso"]
    return jsonify({"grafica":curso.reporte_cursos(grafo_pensum,id_curso)})

@app.route("/admin/cargarCursosEstudiantes", methods =['POST'])
def cargarCursosEstudiantes():
    global grafo_pensum

if __name__=="__main__":
    import os
    if os.path.exists(r"C:\Users\Adrian Aguilar\Desktop\Reportes_F3") is not True:
        os.mkdir(r"C:\Users\Adrian Aguilar\Desktop\Reportes_F3")
    app.run(port=3000, debug=True)