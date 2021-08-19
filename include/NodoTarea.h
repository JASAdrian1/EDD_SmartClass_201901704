#ifndef NODOTAREA_H
#define NODOTAREA_H
#include<Tarea.h>


class NodoTarea
{
    public:
        NodoTarea();
        NodoTarea(Tarea tarea,NodoTarea *anterior, NodoTarea *siguiente);
        NodoTarea *siguiente;
        NodoTarea *anterior;
        Tarea tarea;
        virtual ~NodoTarea();

    protected:

    private:
};

#endif // NODOTAREA_H
