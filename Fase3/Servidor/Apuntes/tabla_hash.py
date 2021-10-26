from Apuntes.nodo_hash import Nodo_Hash

class Tabla_Hash:
    def __init__(self):
        self.claves = [None,None,None,None,None,None,None]
        self.tam_tabla = 7
        self.claves_usadas = 0
        self.num_r = 0


    def insertar(self,id,apunte):
        if type(id) == str:
            id = int(id)
        nuevo_nodo = Nodo_Hash(id,apunte)
        indice = self.calcular_clave(id)
        if self.claves[indice-1] == None:
            self.claves[indice-1] = nuevo_nodo
            self.claves_usadas+=1
        else:
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
                self.insertar(claves_aux[i].id,claves_aux[i].apunte)



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
                print("Carnet: ",nodo.id,"   Titulo: ",nodo.apunte.titulo)
            else:
                print("Vacio")
