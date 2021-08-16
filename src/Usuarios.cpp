#include "Usuarios.h"
#include<iostream>
#include<fstream>
#include<string>
#include<ListaUsuarios.h>

using namespace std;

ListaUsuarios * listaUs = new ListaUsuarios();

Usuarios::Usuarios(string id, string dpi, string nombre, string carrera, string correo, string password, string creditos, string edad)
{
    this->id = id;
    this->dpi = dpi;
    this->nombre = nombre;
    this->carrera = carrera;
    this->correo = correo;
    this->password = password;
    this->creditos = creditos;
    this->edad = edad;

    //ctor
}
Usuarios::Usuarios()
{
    //ctor
}

void Usuarios::cargarUsuarios(){

    ifstream archivo;
    string ruta;
    cout<<"Ingrese la ruta del archivo: ";
    cin.ignore();
    getline(cin,ruta);
    //cout<<ruta<<endl;
    archivo.open(ruta,ios::in);
    if (archivo.good()){
        string linea;
        int contEnc = 0;
        while(getline(archivo,linea)){
            string del = ",";
            int start = 0;
            int endS = linea.find(del);
            int contador = 0;
            //VARIABLES PARA ALMACENAR LA INFORMACION DEL USUARIO
            string id = "";
            string dpi = "";
            string nombre = "";
            string carrera = "";
            string correo = "";
            string password = "";
            string creditos = "";
            string edad = "";
            if(contEnc>0){
                while (endS != -1) {
                    /*cout << linea.substr(start, endS - start) << "----";
                    cout<<contador<<endl;*/
                    switch(contador){
                        case 0:
                            //cout<<linea.substr(start, endS - start)<<endl;
                            id = linea.substr(start, endS - start);
                            //cout<<"Carnet: "<<id<<endl;

                            break;
                        case 1:
                            dpi = linea.substr(start, endS - start);
                            //cout<<"DPI: "<<dpi<<endl;
                            break;
                        case 2:
                            nombre = linea.substr(start, endS - start);
                            //cout<<"Nombre: "<<nombre<<endl;
                            break;
                        case 3:
                            carrera = linea.substr(start, endS - start);
                            //cout<<"Carrera: "<<carrera<<endl;
                            break;
                        case 4:
                            password = linea.substr(start, endS - start);
                            //cout<<"Password: "<<password<<endl;
                            break;
                        case 5:
                            creditos = linea.substr(start, endS - start);
                            //cout<<"Creditos: "<<creditos<<endl;
                            break;
                        case 6:
                            edad = linea.substr(start, endS - start);
                            //cout<<"Edad: "<<edad<<endl;
                            break;

                    }
                    start = endS + del.size();
                    endS = linea.find(del, start);
                    contador+=1;

                }
                correo = linea.substr(start, endS - start);
                Usuarios *usuario = new Usuarios(id,dpi,nombre,carrera,correo,password,creditos,edad);
                listaUs->insertar(usuario);
            }
            contEnc+=1;
            //cout<<contador;

        }
        listaUs->imprimirUsuarios();

        printf("Se ha cargado el archivo correctamente");

    }else{
        cout<<"No se ha encontrado el archivo"<<endl;
    }


}


void Usuarios::insertarUsuario(){
    string id;
    string dpi;
    string nombre;
    string carrera;
    string correo;
    string password;
    string creditos;
    string edad;
    cout<<"Ingrese el ID: "<<endl;  cin >> id;
    cout<<"Ingrese el DPI: "<<endl;  cin >> dpi;
    cout<<"Ingrese el nombre: "<<endl;  cin >> nombre;
    cout<<"Ingrese la carrera: "<<endl;  cin >> carrera;
    cout<<"Ingrese el correo: "<<endl;  cin >> correo;
    cout<<"Ingrese el password: "<<endl;  cin >> password;
    cout<<"Ingrese los creditos: "<<endl;  cin >> creditos;
    cout<<"Ingrese la edad: "<<endl;  cin >> edad;
    Usuarios *nuevoUsuario = new Usuarios(id,dpi,nombre,carrera,correo,password,creditos,edad);
    listaUs->insertar(nuevoUsuario);
    listaUs->imprimirUsuarios();
}


void Usuarios::modificarUsuario(){
    string dpi = "";
    cout<<"Ingrese el DPI del usuario al que desea modificar la informacion: "<<endl;
    cin >> dpi;
    listaUs->modificarUsuario(dpi);
}

void Usuarios::eliminarUsuario(){
    if(listaUs!=nullptr){
        string dpi = "";
        cout<<"Ingrese el DPI del usuario al que desea modificar la informacion: "<<endl;
        cin >> dpi;
        listaUs->eliminarUsuario(dpi);
    }

}

Usuarios::~Usuarios()
{
    //dtor
}
