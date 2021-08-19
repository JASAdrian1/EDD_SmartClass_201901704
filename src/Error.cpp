#include "Error.h"
#include<ColaError.h>
#include<NodoUsuario.h>


ColaError *colaErrores = new ColaError();
int idError =0;

Error::Error()
{
    //ctor
}


Error::Error(string tipo, string descripcion, Usuarios *usuario){
    idError+=1;
    this->id = idError;
    this->tipo = tipo;
    this->descripcion = descripcion;
}

void Error::insetarError(Error *err){

    colaErrores->encolar(err);
}

void Error::imprimirColaError(){
    colaErrores->mostrarCola();
}

void Error::graficarErrores(){
    colaErrores->graficarErrores();
}


Error::~Error()
{
    //dtor
}
