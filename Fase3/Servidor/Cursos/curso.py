
class Curso:
    def __init__(self,id,nombre,creditos,prerre,obligatorio):
        self.id = id
        self.nombre = nombre
        self.creditos = creditos
        self.prerre = prerre
        self.obligatorio = obligatorio



def cargar_cursos(texto,arbol_estudiantes,grafo_cursos):
    print("Cargando cursos")
    for key in list(texto):
        if key == "Estudiantes":
            print(texto["Estudiantes"])
            texto = texto["Estudiantes"]
            for estudiante in texto:
                carnet = estudiante["Carnet"]
                print(estudiante["Carnet"])
                for anio in estudiante["Años"]:
                    no_anio = anio["Año"]
                    print("Año: ",no_anio)
                    #print(anio)
                    for semestre in anio["Semestres"]:
                        #print("Semestre: ",semestre["Semestre"])
                        no_semestre = semestre["Semestre"]
                        for cursos in semestre["Cursos"]:
                            codigo = cursos["Codigo"]
                            nombre = cursos["Nombre"]
                            creditos = cursos["Creditos"]
                            prere = cursos["Prerequisitos"]
                            obligatorio = cursos["Obligatorio"]
                            #nuevo_curso = curso(codigo,nombre,creditos,prere,obligatorio)
                            #arbol_estudiantes.insertar_curso(carnet,arbol_estudiantes.raiz,no_anio,no_semestre,nuevo_curso)
        elif key == "Cursos":
            #print(texto["Cursos"])
            texto = texto["Cursos"]
            for cursos in texto:
                id = cursos["Codigo"]
                nombre = cursos["Nombre"]
                creditos = cursos["Creditos"]
                prerre = cursos["Prerequisitos"]
                obligatorio = cursos["Obligatorio"]
                nuevo_curso = Curso(id,nombre,creditos,prerre,obligatorio)
                grafo_cursos.insertar(id,nuevo_curso)

            for cursos in texto:
                prerrequisitos =cursos["Prerequisitos"].split(",")
                #print(prerrequisitos)
                id_acutal = cursos["Codigo"]
                nombre_actual = cursos["Nombre"]
                for prerrequisito in prerrequisitos:
                    if prerrequisito != "":
                        curso_prerre = grafo_cursos.buscar_nodo(prerrequisito)
                        if curso_prerre is not None:
                            #print(prerequisito)
                            #print(curso_prerre)
                            grafo_cursos.asociar_nodo(curso_prerre.curso.id,id_acutal,nombre_actual)
