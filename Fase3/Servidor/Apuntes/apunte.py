

class Apunte:
    def __init__(self,carnet,titulo,apunte):
        self.carnet = carnet
        self.titulo = titulo
        self.apunte = apunte



def cargarApuntes(texto, tablaHash):
    for key in list(texto):
        if key == "usuarios":
            texto = texto["usuarios"]
            for estudiante in texto:
                print(estudiante["carnet"])
                carnet = estudiante["carnet"]
                for apunte in estudiante["apuntes"]:
                    titulo = apunte["Título"]
                    contenido = apunte["Contenido"]
                    nuevoApunte = Apunte(str(carnet),titulo,contenido)
                    tablaHash.insertar(carnet,nuevoApunte)