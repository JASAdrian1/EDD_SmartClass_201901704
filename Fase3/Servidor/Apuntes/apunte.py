

class Apunte:
    def __init__(self,carnet,titulo,apunte):
        self.carnet = carnet
        self.titulo = titulo
        self.apunte = apunte



def cargarApuntes(texto, tablaHash):
    for key in list(texto):
        if key == "usuarios":
            texto = texto["usuarios"]
            print(len(texto))
            """for i in range(0,len(texto),1):
                print(texto[i]["carnet"])
                carnet = texto[i]["carnet"]
                for apunte in texto[i]["apuntes"]:
                    titulo = apunte["titulo"]
                    contenido = apunte["contenido"]
                    nuevoApunte = Apunte(str(carnet), titulo, contenido)
                    tablaHash.insertar(carnet, nuevoApunte)"""

            for estudiante in texto:
                carnet = estudiante["carnet"]
                for apunte in estudiante["apuntes"]:
                    titulo = apunte["titulo"]
                    contenido = apunte["contenido"]
                    nuevoApunte = Apunte(str(carnet),titulo,contenido)
                    tablaHash.insertar(carnet,nuevoApunte)