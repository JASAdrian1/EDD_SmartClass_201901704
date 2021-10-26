from Apuntes.apunte import Apunte
import tabla_hash

tabla = tabla_hash.Tabla_Hash()

apunte1 = Apunte(201901704,"Proyecto edd","Tengo que terminar el proyecto :c")
apunte2 = Apunte(215615112,"Proyecto compi","Tengo que terminar el proyecto :c")
apunte3 = Apunte(846510104,"Proyecto io","Tengo que terminar el proyecto :c")
apunte4 = Apunte(516168845,"Proyecto lfp","Tengo que terminar el proyecto :c")
apunte5 = Apunte(661655984,"Proyecto ipc","Tengo que terminar el proyecto :c")
apunte6 = Apunte(255888555,"Proyecto estadistica","Tengo que terminar el proyecto :c")
apunte7 = Apunte(223215222,"Proyecto orga","Tengo que terminar el proyecto :c")
apunte8 = Apunte(201955254,"Proyecto psico","Tengo que terminar el proyecto :c")
apunte9 = Apunte(515151541,"Proyecto analisis","Tengo que terminar el proyecto :c")
apunte10 = Apunte(141774747,"Proyecto teo","Tengo que terminar el proyecto :c")

tabla.insertar(201901704,apunte1)
tabla.insertar(215615112,apunte2)
tabla.insertar(846510104,apunte3)
tabla.insertar(516168845,apunte4)
tabla.insertar(661655984,apunte5)
tabla.insertar(255888555,apunte6)
tabla.insertar(223215222,apunte7)
tabla.insertar(201955254,apunte8)
tabla.insertar(515151541,apunte9)
tabla.insertar(141774747,apunte10)

tabla.recorrer_tabla()

