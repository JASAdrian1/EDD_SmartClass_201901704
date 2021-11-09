from Apuntes.nodo_apunte import Nodo_apunte

class Lista_apunte:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def lista_vacia(self):
        if self.primero is None:
            return True
        else:
            return False

    def insertar(self, id,apunte):
        nuevo_nodo = Nodo_apunte(id,apunte)
        if self.lista_vacia():
            self.primero = nuevo_nodo
        else:
            tmp = self.primero
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo_nodo

    def buscar_apunte(self, id):
        tmp = self.primero
        while tmp is not None:
            print(type(id)," == ",type(tmp.id))
            if id == tmp.id:
                return tmp
            tmp = tmp.siguiente
        print("No se ha encontrado el apunte")