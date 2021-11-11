from Analizadores.sintactico import parser
from Cursos.grafo_cursos import Grafos_cursos
from cryptography.fernet import Fernet

llave = Fernet.generate_key()
f = Fernet(llave)

class Usuario:
    def __init__(self,id,dpi,nombre,carrera,correo,password,edad,rol):
        self.id = id
        self.dpi = dpi
        self.nombre = nombre
        self.carrera = carrera
        self.correo = correo
        self.password = password
        self.edad = edad
        self.rol = rol
        self.cursos = Grafos_cursos()

    def get_informacion(self,encriptado):
        if encriptado == True:
            informacion = str(self.id)+"\\n"
            informacion += str(self.nombre) + "\\n"
            informacion += str(self.carrera)
        else:
            informacion = str(self.id)+"\\n"
            if type(self.nombre) == bytes:
                informacion += str(f.decrypt(self.nombre))+ "\\n"
                informacion += str(f.decrypt(self.carrera))
        return informacion

    def insertarCurso(self,nuevo_curso,prerequisitos,codigo,nombre_curso_actual):
        self.cursos.insertar(nuevo_curso)
        #for prerequisito in nuevo_curso.


def cargarEstudiantes(texto, arbol_estudiantes):
    for key in list(texto):
        if key == "estudiantes":
            texto = texto["estudiantes"]
            for estudiante in texto:
                print(estudiante["carnet"])
                carnet = estudiante["carnet"]
                dpi = estudiante["dpi"]
                dpi = f.encrypt(dpi.encode('utf-8'))
                nombre = estudiante["nombre"]
                nombre = f.encrypt(nombre.encode('utf-8'))
                carrera = estudiante["carrera"]
                carrera = f.encrypt(carrera.encode('utf-8'))
                correo = estudiante["correo"]
                correo = f.encrypt(correo.encode('utf-8'))
                password = estudiante["password"]
                password = f.encrypt(password.encode('utf-8'))
                edad = estudiante["edad"]
                nuevoEstudiante = Usuario(str(carnet), str(dpi), nombre, carrera,correo, str(password), edad,"usuario")
                arbol_estudiantes.insertar(nuevoEstudiante, nuevoEstudiante.id)
                print("Se inserto ", nuevoEstudiante.id)


def grafica_desencriptada(arbol_estudiantes):
    arbol_estudiantes.graficar(False)



