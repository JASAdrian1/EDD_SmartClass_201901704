from Cursos.grafo_cursos import Grafos_cursos


grafo = Grafos_cursos()

grafo.insertar(34,"Mate")
grafo.insertar(777,"Compiladores")
grafo.insertar(772,"EDD")
grafo.insertar(114,"Basica 2")
grafo.insertar(890,"IO")

grafo.asociar_nodo(890,34,"Mate")
grafo.asociar_nodo(114,777,"Compiladores")

grafo.graficar_grafo()
