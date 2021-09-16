#ifndef NODOERROR_H
#define NODOERROR_H
#include<Error.h>


class NodoError
{
    public:
        NodoError();
        NodoError(Error *err, NodoError *siguiente);
        Error *err;
        NodoError * siguiente;

        virtual ~NodoError();

    protected:

    private:
};

#endif // NODOERROR_H
