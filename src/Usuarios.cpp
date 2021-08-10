#include "Usuarios.h"
#include<iostream>
#include<fstream>
#include<string>

using namespace std;

Usuarios::Usuarios()
{
    //ctor
}

void Usuarios::cargarUsuarios(){
    ifstream archivo;
    string ruta, texto;
    cout<<"Ingrese la ruta del archivo: ";
    cin.ignore();
    getline(cin,ruta);
    //cout<<ruta<<endl;
    archivo.open(ruta,ios::in);
    if (archivo.good()){
        while(!archivo.eof()){
            getline(archivo,texto);
            cout<<texto<<endl;
        }
        string del = "\n";
        int start = 0;
        int endS = texto.find(del);
        printf("Se ha cargado el archivo correctamente");

    }else{
        cout<<"No se ha encontrado el archivo"<<endl;
    }


}

Usuarios::~Usuarios()
{
    //dtor
}
