from arbol_b.arbol_b_cursos import Arbol_B

class nodo_semestre:
    def __init__(self,no_semestre):
        self.no_semestre = no_semestre
        self.arbol_cursos = Arbol_B()
        self.siguiente = None

class lista_semestre:
    def __init__(self):
        self.primero = None


    def insertar(self,no_semestre):
        nuevo_nodo = nodo_semestre(no_semestre)
        if self.primero is None:
            self.primero = nuevo_nodo
            print("Se inserto el semestre ", no_semestre)
        else:
            tmp = self.primero
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            if self.verificar_semestre_repetido(no_semestre) is False:
                print("Se inserto el semestre ",no_semestre)
                aux = tmp
                tmp.siguiente = nuevo_nodo
                tmp.anterior = aux

    def insertar_curso(self,no_semestre,curso):
        tmp = self.primero
        if tmp is not None:
            while tmp is not None:
                if no_semestre == tmp.no_semestre:
                    tmp.arbol_cursos.insertar(curso)
                    return
                tmp = tmp.siguiente
        print("No se ha podido insertar el curso ",curso.codigo)


    def graficar_arbol_cursos(self,no_semestre):
        tmp = self.primero
        if tmp is not None:
            while tmp is not None:
                if no_semestre == tmp.no_semestre:
                    tmp.arbol_cursos.graficar()
                    return
                tmp = tmp.siguiente
        print("No se ha podido graficar ya que no se encontró el semestre solicitado")


    def verificar_semestre_repetido(self,no_semestre):
        tmp = self.primero
        if tmp is not None:
            while tmp is not None:
                if no_semestre == tmp.no_semestre:
                    return True
                tmp = tmp.siguiente
            return False
        else:
            return False
        return False

    def imprimir_semestres(self):
        tmp = self.primero
        if tmp is not None:
            while tmp is not None:
                print("Semestre: ",tmp.no_semestre)
                tmp = tmp.siguiente

