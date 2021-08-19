#include "NodoError.h"
#include<Error.h>

NodoError::NodoError()
{
    //ctor
    this->siguiente = nullptr;
}

NodoError::NodoError(Error *err,NodoError *siguiente){
    this->err = err;
    this->siguiente = siguiente;

}



NodoError::~NodoError()
{
    //dtor
}
