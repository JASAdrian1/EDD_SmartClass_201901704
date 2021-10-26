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


def cargarEstudiantes(texto, arbol_estudiantes):

    for item in texto:
        if item['type'] == "user":
            for atributo in item['atributos']:
                try:
                    for key in list(atributo):
                        if key == "Carnet":
                            carnet = atributo['Carnet']
                        elif key == "DPI":
                            dpi = atributo['DPI']
                        elif key == "Nombre":
                            nombre = atributo['Nombre']
                        elif key == "Carrera":
                            carrera = atributo['Carrera']
                        elif key == "Password":
                            password = atributo['Password']
                        elif key == "Creditos":
                            creditos = atributo['Creditos']
                        elif key == "Edad":
                            edad = atributo['Edad']
                except:
                    print(atributo)
                    print("La estructura de este estudiante no era la correcta")
            nuevoEstudiante = Usuario(carnet[1:-1], dpi[1:-1], nombre[1:-1], carrera[1:-1], password[1:-1],
                                         creditos, edad)
            arbol_estudiantes.insertar(nuevoEstudiante, nuevoEstudiante.carnet)

    # arbol_estudiantes.preorden(arbol_estudiantes.raiz)
    # arbol_estudiantes.graficar()

