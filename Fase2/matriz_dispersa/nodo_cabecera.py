from matriz_dispersa.lista_interna_matriz import lista_interna_matriz

class nodo_cabecera:
    def __init__(self,id):
        self.id = id
        self.siguiente = None
        self.anterior = None
        self.lista_interna = lista_interna_matriz()
