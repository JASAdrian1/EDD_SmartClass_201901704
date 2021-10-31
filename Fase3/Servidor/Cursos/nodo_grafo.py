from Cursos.lista_adyacente import Lista_adyacente

class Nodo_grafo:
    def __init__(self,id,curso):
        self.curso = curso
        self.id = id
        self.lista_adyacentes = Lista_adyacente()
        self.siguiente = None

