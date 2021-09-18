from anio import anio as Anio_clase
from matriz_dispersa.lista_mes import lista_mes

class nodo_anio:
    def __init__(self,no_anio):
        self.anio = Anio_clase(no_anio)
        self.meses = lista_mes()
        self.siguiente = None
        self.anterior = None