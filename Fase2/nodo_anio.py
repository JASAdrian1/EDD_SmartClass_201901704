from anio import anio as Anio_clase

class nodo_anio:
    def __init__(self,no_anio):
        self.anio = Anio_clase(no_anio)
        self.siguiente = None
        self.anterior = None