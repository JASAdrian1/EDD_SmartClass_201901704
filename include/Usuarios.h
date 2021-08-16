#ifndef USUARIOS_H
#define USUARIOS_H
#include<string>




class Usuarios
{
    public:
        Usuarios();
        Usuarios(std::string id, std::string dpi, std::string nombre, std::string carrera, std::string correo, std::string password, std::string creditos, std::string edad);
        static void cargarUsuarios();
        static void insertarUsuario();
        static void modificarUsuario();
        static void eliminarUsuario();
        std::string id;
        std::string dpi;
        std::string nombre;
        std::string carrera;
        std::string correo;
        std::string password;
        std::string creditos;
        std::string edad;

        virtual ~Usuarios();

    protected:

    private:
};

#endif // USUARIOS_H
