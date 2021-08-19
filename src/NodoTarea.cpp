#include "NodoTarea.h"

NodoTarea::NodoTarea()
{
    //ctor
        this->tarea = Tarea();
        this->anterior = nullptr;
        this->siguiente = nullptr;
}

NodoTarea::NodoTarea(Tarea tarea,NodoTarea *anterior,NodoTarea *siguiente){
    this->tarea = tarea;
    this->anterior = anterior;
    this->siguiente = siguiente;
}

NodoTarea::~NodoTarea()
{
    //dtor
}
