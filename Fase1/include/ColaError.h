#ifndef COLAERROR_H
#define COLAERROR_H
#include<Error.h>
#include<NodoError.h>

class ColaError
{
    public:
        ColaError();
        NodoError *primero;
        int tamanio;
        int estaVacia();
        void encolar(Error *err);
        void mostrarCola();
        void desencolar();
        void graficarErrores();

        virtual ~ColaError();

    protected:

    private:
};

#endif // COLAERROR_H
