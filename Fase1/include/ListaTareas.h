#ifndef LISTATAREAS_H
#define LISTATAREAS_H
#include<NodoTarea.h>
#include<string>
#include<ColaError.h>


class ListaTareas
{
    public:
        ListaTareas();
        int listaVacia();
        NodoTarea *primero;
        NodoTarea *ultimo;
        void insertar(Tarea *tarea);
        NodoTarea* buscarTarea(int indice);
        void modificarTarea(int indice);
        void imprimirTareas();
        void eliminarTarea(int indice);
        void graficarLista();
        void busquedaLinealizada(int posicion);
        string generarCodigoSalida();
        virtual ~ListaTareas();

    protected:

    private:
};

#endif // LISTATAREAS_H
