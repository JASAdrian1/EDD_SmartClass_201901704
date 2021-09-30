

class curso:
    def __init__(self,codigo,nombre,creditos,cod_prerre,obligatorio):
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos
        self.cod_prerre = cod_prerre
        self.obligatorio = obligatorio


def cargar_cursos(texto,arbol_estudiantes,arbol_pensum):
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
                            nuevo_curso = curso(codigo,nombre,creditos,prere,obligatorio)
                            #Se inserta el año al estudiante si el año no existe en su usuario
                            arbol_estudiantes.insertar_anio(carnet, arbol_estudiantes.raiz, no_anio)
                            #Se inserta el semetre al año correspondiente
                            arbol_estudiantes.insertar_semestre(carnet,arbol_estudiantes.raiz,no_anio,no_semestre)
                            arbol_estudiantes.insertar_curso(carnet,arbol_estudiantes.raiz,no_anio,no_semestre,nuevo_curso)
        elif key == "Cursos":
            print(texto["Cursos"])
            texto = texto["Cursos"]
            for cursos in texto:
                codigo = cursos["Codigo"]
                nombre = cursos["Nombre"]
                creditos = cursos["Creditos"]
                prere = cursos["Prerequisitos"]
                obligatorio = cursos["Obligatorio"]
                nuevo_curso = curso(codigo,nombre,creditos,prere,obligatorio)
                arbol_pensum.insertar(nuevo_curso)

