#ifndef TAREA_H
#define TAREA_H
#include<string>
#include<iostream>

using namespace std;

class Tarea
{
    public:
        Tarea();
        Tarea(int mes, int dia, int hora, string carnet, string nombre, string descripcion, string materia, string fecha, string estado);
        void cargarTareas();
        bool validarFormatoFehca(string fecha);
        void insertarTarea();
        void eliminarTarea();
        void modificarTarea();
        void graficarLista();
        void busquedaLinealizada(int posicion);
        string generarCodigoSalida();
        string id;
        string carnet;
        string nombre;
        string descripcion;
        string materia;
        string fecha;
        int mes;
        int dia;
        int hora;
        string estado;
        virtual ~Tarea();

    protected:

    private:
};

#endif // TAREA_H
