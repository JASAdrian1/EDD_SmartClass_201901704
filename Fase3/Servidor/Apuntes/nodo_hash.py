from Apuntes.lista_apunte import Lista_apunte

class Nodo_Hash:
    def __init__(self,id,apunte):
        self.id = id
        self.apuntes = Lista_apunte()
        self.apuntes.insertar(id,apunte)