#ifndef NODOUSUARIO_H
#define NODOUSUARIO_H
#include <Usuarios.h>


class NodoUsuario
{
    public:
        NodoUsuario();
        NodoUsuario *siguiente;
        NodoUsuario *anterior;
        Usuarios usuario;
        virtual ~NodoUsuario();

    protected:

    private:
};

#endif // NODOUSUARIO_H
