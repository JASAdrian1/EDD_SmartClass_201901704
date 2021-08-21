#ifndef ERROR_H
#define ERROR_H
#include<string>
#include<iostream>
#include<Usuarios.h>
#include<NodoTarea.h>
#include<Tarea.h>

using namespace std;


class Error
{
    public:
        Error();
        Error(string tipo, string descripcion,Usuarios *usuario);
        Error(string tipo, string descripcion,Tarea *tarea);
        int id;
        string tipo;
        string descripcion;
        Usuarios *usuario;
        Tarea *tarea;
        static void insetarError(Error *err);
        static void imprimirColaError();
        static void graficarErrores();

        virtual ~Error();

    protected:

    private:
};

#endif // ERROR_H
