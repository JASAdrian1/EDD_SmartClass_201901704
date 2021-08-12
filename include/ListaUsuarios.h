#ifndef LISTAUSUARIOS_H
#define LISTAUSUARIOS_H
#include <NodoUsuario.h>

class ListaUsuarios
{
    public:
        ListaUsuarios();
        int listaVacia();
        NodoUsuario *primero;
        NodoUsuario *ultimo;
        void insertar(Usuarios *usuario);
        void imprimirUsuarios();

        virtual ~ListaUsuarios();

    protected:

    private:
};

#endif // LISTAUSUARIOS_H
