from graphviz import Source

from Apuntes.nodo_hash import Nodo_Hash
from Apuntes.lista_apunte import Lista_apunte

class Tabla_Hash:
    def __init__(self):
        self.claves = [None,None,None,None,None,None,None]
        self.tam_tabla = 7
        self.claves_usadas = 0
        self.num_r = 0


    def insertar(self,id,apunte):
        if type(id) == str:
            id = int(id)
        indice = self.calcular_clave(id)
        if self.claves[indice-1] == None:
            nuevo_nodo = Nodo_Hash(id, apunte)
            self.claves[indice-1] = nuevo_nodo
            self.claves_usadas+=1
        else:
            if id == self.claves[indice-1].id:
                self.claves[indice -1 ].apuntes.insertar(id,apunte)
            else:
                nuevo_nodo = Nodo_Hash(id, apunte)
                nuevo_indice = self.resolver_colision(indice)
                self.claves[nuevo_indice-1] = nuevo_nodo
                self.claves_usadas+=1

        #print(self.claves_usadas)
        #print(self.tam_tabla)
        porcentaje_ocupado = self.claves_usadas / self.tam_tabla
        if porcentaje_ocupado >=0.7:
            #print(porcentaje_ocupado)
            self.rehash()

        self.num_r+=1


    def calcular_clave(self,id):
         return id % self.tam_tabla


    def resolver_colision(self,indice):
        nuevo_indice = 0
        disponible = False
        i = 0

        while(disponible == False):
            nuevo_indice = indice + pow(i,2)
            if(nuevo_indice>self.tam_tabla):
                nuevo_indice = nuevo_indice - self.tam_tabla * (nuevo_indice//self.tam_tabla)
            #print(indice)
            if self.claves[nuevo_indice -1 ] == None:
                disponible = True
            i+=1
        return  nuevo_indice


    def rehash(self):
        nuevo_tam = self.buscar_primo(self.tam_tabla)
        #print(nuevo_tam)
        claves_aux = self.claves
        self.tam_tabla = nuevo_tam
        self.claves = []
        self.claves_usadas = 0
        for i in range(0,nuevo_tam,1):
            self.claves.append(None)

        for i in range(0, len(claves_aux),1):
            if claves_aux[i] != None:
                tmp = claves_aux[i].apuntes.primero
                while tmp is not None:
                    self.insertar(claves_aux[i].id, tmp.apunte)
                    tmp = tmp.siguiente




    def buscar_primo(self,numero_actual):
        es_primo = False
        numero_primo = numero_actual
        while es_primo is False:
            numero_primo += 1
            for i in range(2,numero_primo,1):
                if numero_primo % i == 0:
                    break
                if i == numero_primo -1 :
                    es_primo = True

        return numero_primo

    def recorrer_tabla(self):
        for nodo in self.claves:
            if nodo != None:
                print("Carnet: ",nodo.id,"   Titulo: ",end="")
                tmp = nodo.apuntes.primero

                while tmp is not None:
                    print(tmp.apunte.titulo,end=", ")
                    tmp = tmp.siguiente
                print()
            else:
                print("Vacio")

    def get_apuntes_usuario(self,id):
        apuntes = []
        for nodo in self.claves:
            if nodo != None:
                print(type(id),"    ",type(nodo.id))
                print(id," == ",nodo.id)
                if id == str(nodo.id):
                    tmp = nodo.apuntes.primero
                    while tmp is not None:
                        apuntes.append([tmp.apunte.titulo,tmp.apunte.apunte])
                        tmp = tmp.siguiente
                    return apuntes

        print("No se ha encontrado el usuario para poder retornar sus apuntes")

    def graficar_apuntes(self):
        texto = "digraph D{\n"
        texto += "tabla [\nshape=plaintext\n"
        texto += "label=<\n"
        texto +="<table border='1' cellborder='1'>\n"
        texto +="<tr><td colspan='"+str(len(self.claves))+"'>Apuntes</td></tr>\n"
        texto += "<tr>\n"
        for nodo in self.claves:
            contador = 0
            if nodo != None:
                texto +="<td port='"+str(nodo.id)+"'>"+str(nodo.id)+"</td>\n"
            else:
                texto += "<td>Vacio</td>"
        texto += "</tr>"

        #texto +="}\n"
        texto +="</table>\n"
        texto +=">];\n"
        for nodo in self.claves:
            if nodo is not None:
                texto += "a_" + str(nodo.id) + " [shape=plaintext\n"
                texto += "label=<\n"
                texto += "<table border='1'>\n"
                tmp = nodo.apuntes.primero
                contador_apuntes = 0
                while tmp is not None:
                    texto += "<tr>\n"
                    texto+="<td>"+tmp.apunte.titulo+"</td>"
                    contador_apuntes += 1
                    tmp = tmp.siguiente
                    texto += "</tr>\n"
                texto+="</table>>];\n"

        for nodo in self.claves:
            if nodo is not None:

                texto += "tabla:"+str(nodo.id)+" ->" +"a_"+str(nodo.id)+";\n"

        texto+="}"
        """archivo = open("grafica_apuntes.dot", "w+")
        archivo.write(texto)
        archivo.close()
        s = Source.from_file("grafica_apuntes.dot")
        s.view()"""
        return texto
