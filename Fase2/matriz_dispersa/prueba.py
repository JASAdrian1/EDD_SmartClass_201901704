from matriz_dispersa.nodo_cabecera import nodo_cabecera
from matriz_dispersa.lista_cabecera import lista_cabecera
from tarea import tarea
from matriz_dispersa.matriz import matriz
from arbol_b.curso import curso
from arbol_b.arbol_b_cursos import Arbol_B

"""lista_prueba = lista_cabecera()
lista_prueba.insertar(nodo_cabecera(4))
lista_prueba.insertar(nodo_cabecera(10))
lista_prueba.insertar(nodo_cabecera(20))
lista_prueba.insertar(nodo_cabecera(1))
lista_prueba.insertar(nodo_cabecera(16))
lista_prueba.insertar(nodo_cabecera(6))
lista_prueba.insertar(nodo_cabecera(23))
lista_prueba.insertar(nodo_cabecera(2))
lista_prueba.insertar(nodo_cabecera(14))
lista_prueba.insertar(nodo_cabecera(7))
lista_prueba.imprimir_encabezado()"""

tarea1 = tarea(201901704,"Adrian","efsgsfgdsfgdf","Lenguajes","Finalizado","11/01/2020",2020,8,7,4)
tarea2 = tarea(201901704,"Adrian","efsgsfgdsfgdf","Mate","Finalizado","11/01/2020",2020,10,7,8)
tarea3 = tarea(201901704,"Adrian","efsgsfgdsfgdf","IPC","Finalizado","11/01/2020",2020,11,21,2)
tarea4 = tarea(201901704,"Adrian","efsgsfgdsfgdf","Quimica","Finalizado","11/01/2020",2020,5,7,4)
tarea5 = tarea(201901704,"Adrian","efsgsfgdsfgdf","EDD","Finalizado","11/01/2020",2020,10,7,10)
tarea6 = tarea(201901704,"Adrian","efsgsfgdsfgdf","Compi","Finalizado","11/01/2020",2020,5,28,2)
tarea7 = tarea(201901704,"Adrian","efsgsfgdsfgdf","Orga","Finalizado","11/01/2020",2020,5,7,21)
tarea8 = tarea(201901704,"Adrian","efsgsfgdsfgdf","IO1","Finalizado","11/01/2020",2020,10,7,4)
tarea9 = tarea(201901704,"Adrian","efsgsfgdsfgdf","Fisica","Finalizado","11/01/2020",2020,10,7,4)
tarea10 = tarea(201901704,"Adrian","efsgsfgdsfgdf","Seminario","Finalizado","11/01/2020",2020,10,7,11)
tarea11 = tarea(201901704,"Adrian","efsgsfgdsfgdf","Lenguajes","Finalizado","11/01/2020",2020,11,7,11)
tarea12 = tarea(201901704,"Adrian","efsgsfgdsfgdf","Materia","Finalizado","11/01/2020",2020,8,7,4)
tarea13 = tarea(201901704,"Adrian","efsgsfgdsfgdf","Archivos","Finalizado","11/01/2020",2020,8,28,8)
tarea14 = tarea(201901704,"Adrian","efsgsfgdsfgdf","Logica","Finalizado","11/01/2020",2020,8,28,21)

matriz_tareas = matriz()
matriz_tareas.insertar(tarea1,tarea1.hora,tarea1.dia)
matriz_tareas.insertar(tarea2,tarea2.hora,tarea2.dia)
matriz_tareas.insertar(tarea3,tarea3.hora,tarea3.dia)
matriz_tareas.insertar(tarea4,tarea4.hora,tarea4.dia)
matriz_tareas.insertar(tarea5,tarea5.hora,tarea5.dia)
matriz_tareas.insertar(tarea6,tarea6.hora,tarea6.dia)
matriz_tareas.insertar(tarea7,tarea7.hora,tarea7.dia)
matriz_tareas.insertar(tarea8,tarea8.hora,tarea8.dia)
matriz_tareas.insertar(tarea9,tarea9.hora,tarea9.dia)
matriz_tareas.insertar(tarea10,tarea10.hora,tarea10.dia)
matriz_tareas.insertar(tarea11,tarea11.hora,tarea11.dia)
matriz_tareas.insertar(tarea12,tarea12.hora,tarea12.dia)
matriz_tareas.insertar(tarea13,tarea13.hora,tarea13.dia)
matriz_tareas.insertar(tarea14,tarea14.hora,tarea14.dia)

#matriz_tareas.eliminar(tarea11.hora,tarea11.dia)
#matriz_tareas.buscar_dato(tarea4.hora,tarea4.dia)
#matriz_tareas.get_informacion_tareas(tarea11.dia,tarea11.hora)
#matriz_tareas.graficar_tareas(tarea12.dia,tarea12.hora)
#matriz_tareas.graficar_matriz()
#matriz_tareas.imprimir_matriz()


arbol_curos = Arbol_B()

curso1 = curso(117,"Mate",85,161,False)
curso2 = curso(110,"Mate",85,161,False)
curso3 = curso(135,"Mate",85,161,False)
curso4 = curso(777,"Compiladores",85,161,False)
curso5 = curso(8,"Mate",85,161,False)
curso6 = curso(6,"Mate",85,161,False)
curso7 = curso(656,"Mate",85,161,False)
curso8 = curso(654,"Mate",85,161,False)
curso9 = curso(118,"Mate",85,161,False)
curso10 = curso(907,"Mate",85,161,False)
curso11 = curso(55,"Mate",85,161,False)

arbol_curos.insertar(curso1)
arbol_curos.insertar(curso2)
arbol_curos.insertar(curso3)
arbol_curos.insertar(curso4)
arbol_curos.insertar(curso5)
arbol_curos.insertar(curso6)
arbol_curos.insertar(curso7)
arbol_curos.insertar(curso8)
arbol_curos.insertar(curso9)
arbol_curos.insertar(curso10)
arbol_curos.insertar(curso11)

arbol_curos.graficar()



