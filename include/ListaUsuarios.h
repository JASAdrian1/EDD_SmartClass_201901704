#ifndef LISTAUSUARIOS_H
#define LISTAUSUARIOS_H
#include <NodoUsuario.h>
#include<string>
#include<ColaError.h>


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
        void graficarLista();
        string generarCodigoSalida();



        virtual ~ListaUsuarios();

    protected:

    private:
};

#endif // LISTAUSUARIOS_H
