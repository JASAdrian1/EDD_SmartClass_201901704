from matriz_dispersa.matriz import matriz


class nodo_mes:
    def __init__(self, mes):
        self.mes = mes
        self.matriz_tareas = matriz()
        self.siguiente = None
        self.anterior = None