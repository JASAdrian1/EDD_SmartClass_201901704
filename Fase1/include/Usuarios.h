#ifndef USUARIOS_H
#define USUARIOS_H
#include<string>




class Usuarios
{
    public:
        Usuarios();
        Usuarios(std::string id, std::string dpi, std::string nombre, std::string carrera, std::string correo, std::string password, std::string creditos, std::string edad);
        void cargarUsuarios();
        void insertarUsuario();
        void modificarUsuario();
        void eliminarUsuario();
        bool validarCorreo(std::string correo);
        void graficarLista();
        std::string generarCodigoSalida();
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
