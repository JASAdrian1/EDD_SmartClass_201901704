#ifndef USUARIOS_H
#define USUARIOS_H
#include<string>



class Usuarios
{
    public:
        Usuarios();
        static void cargarUsuarios();
        int id;
        int dpi;
        std::string nombre;
        std::string carrera;
        std::string correo;
        std::string password;
        int creditos;
        int edad;

        virtual ~Usuarios();

    protected:

    private:
};

#endif // USUARIOS_H
