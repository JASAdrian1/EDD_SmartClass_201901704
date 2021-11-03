from Analizadores.sintactico import parser


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

    def get_informacion(self):
        informacion = self.id+"\\n"
        informacion += self.nombre + "\\n"
        informacion += self.carrera
        return informacion

def cargarEstudiantes(texto, arbol_estudiantes):
    for key in list(texto):
        if key == "estudiantes":
            texto = texto["estudiantes"]
            for estudiante in texto:
                print(estudiante["carnet"])
                carnet = estudiante["carnet"]
                dpi = estudiante["DPI"]
                nombre = estudiante["nombre"]
                carrera = estudiante["carrera"]
                correo = estudiante["correo"]
                password = estudiante["password"]
                edad = estudiante["edad"]
                nuevoEstudiante = Usuario(str(carnet), str(dpi), nombre, carrera,correo, str(password), edad,"usuario")
                arbol_estudiantes.insertar(nuevoEstudiante, nuevoEstudiante.id)
                print("Se inserto ", nuevoEstudiante.id)


