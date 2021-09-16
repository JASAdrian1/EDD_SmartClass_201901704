#include "NodoUsuario.h"
#include<Usuarios.h>

NodoUsuario::NodoUsuario(Usuarios usuario,NodoUsuario *anterior, NodoUsuario *siguiente)
{
    this->usuario = usuario;
    this->anterior = anterior;
    this->siguiente = siguiente;
    //ctor
}

NodoUsuario::NodoUsuario()
{
    this->usuario = Usuarios();
    this->anterior = nullptr;
    this->siguiente = nullptr;
    //ctor
}

NodoUsuario::~NodoUsuario()
{
    //dtor
}
