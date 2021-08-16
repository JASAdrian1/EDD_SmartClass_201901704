#ifndef LISTAUSUARIOS_H
#define LISTAUSUARIOS_H
#include <NodoUsuario.h>
#include<string>


using namespace std;

class ListaUsuarios
{
    public:
        ListaUsuarios();
        int listaVacia();
        NodoUsuario *primero;
        NodoUsuario *ultimo;
        void insertar(Usuarios *usuario);
        NodoUsuario* buscarUsuario(string dpi);
        void modificarUsuario(string dpi);
        void eliminarUsuario(string dpi);
        void imprimirUsuarios();

        virtual ~ListaUsuarios();

    protected:

    private:
};

#endif // LISTAUSUARIOS_H
