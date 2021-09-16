from Analizadores.sintactico import parser
from main import arbol_estudiantes


class Estudiante():
    def __init__(self,carnet, dpi, nombre, carrera, password, creditos, edad, lista_años = None):
        self.carnet = carnet
        self.dpi = dpi
        self.nombre = nombre
        self.carrera = carrera
        self.password = password
        self.creditos = creditos
        self.edad = edad

    def imprimirInformacion(self):
        print("Carnet: ",self.carnet)
        print("DPI: ", self.dpi)
        print("Nombre: ", self.nombre)
        print("Carrera: ", self.carrera)
        print("Password: ", self.password)
        print("Creditos: ", self.creditos)
        print("Edad: ", self.edad)



def cargarEstudiantes(texto):
    texto_analizado = parser.parse(texto)
    for item in texto_analizado:
        if item['type'] == "user":
            contador = 0
            for atributo in item['atributos']:
                try:
                    if contador == 0:
                        carnet = atributo['Carnet']
                    if contador == 1:
                        dpi = atributo['DPI']
                    if contador == 2:
                        nombre = atributo['Nombre']
                    if contador == 3:
                        carrera = atributo['Carrera']
                    if contador == 4:
                        password = atributo['Password']
                    if contador == 5:
                        creditos = atributo['Creditos']
                    if contador == 6:
                        edad = atributo['Edad']
                    contador += 1
                except:
                    print(atributo)
                    print("La estructura de este estudiante no era la correcta")
            nuevoEstudiante = Estudiante(carnet[1:-1],dpi[1:-1],nombre[1:-1],carrera[1:-1],password[1:-1],creditos,edad)
            arbol_estudiantes.insertar(nuevoEstudiante,nuevoEstudiante.carnet)
    arbol_estudiantes.preorden(arbol_estudiantes.raiz)


