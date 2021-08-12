#include "ListaUsuarios.h"
#include<iostream>

using namespace std;

ListaUsuarios::ListaUsuarios()
{

    this->primero = nullptr;
    this->ultimo = nullptr;
    //ctor
}

ListaUsuarios::~ListaUsuarios()
{
    //dtor
}

int ListaUsuarios::listaVacia(){
    NodoUsuario* primero = this->primero;
    //cout<<primero<<endl;
    return this->primero == nullptr;

}

void ListaUsuarios::insertar(Usuarios *usuario){
    NodoUsuario *nuevo =new NodoUsuario(*usuario,nullptr,nullptr);
    if(this->listaVacia()){
        this->primero = nuevo;
        this->ultimo = nuevo;
        this->primero->anterior = this->ultimo;
        this->ultimo->siguiente = this->primero;
        //cout<<primero->usuario.nombre<<endl;
    }else{
        NodoUsuario *tmp = this->ultimo;
        this->ultimo->siguiente = nuevo;
        this->ultimo = nuevo;
        this->ultimo->anterior = tmp;
        //cout<<ultimo->usuario.nombre<<endl;

    }
}



void ListaUsuarios::imprimirUsuarios(){
    NodoUsuario *tmp = this->primero;
    while(tmp != this->ultimo->siguiente){
        cout<<"*************************"<<endl;
        cout<<"ID: "<<tmp->usuario.id<<endl;
        cout<<"DPI: "<<tmp->usuario.dpi<<endl;
        cout<<"Nombre: "<<tmp->usuario.nombre<<endl;
        cout<<"Carrera: "<<tmp->usuario.carrera<<endl;
        cout<<"Correo: "<<tmp->usuario.correo<<endl;
        cout<<"Password: "<<tmp->usuario.password<<endl;
        cout<<"Creditos: "<<tmp->usuario.creditos<<endl;
        cout<<"Edad: "<<tmp->usuario.edad<<endl;
        cout<<"*************************"<<endl;
        tmp = tmp->siguiente;
    }
    /*cout<<"ID: "<<tmp->usuario.id<<endl;
    cout<<"DPI: "<<tmp->usuario.dpi<<endl;
    cout<<"Nombre: "<<tmp->usuario.nombre<<endl;
    cout<<"Carrera: "<<tmp->usuario.carrera<<endl;
    cout<<"Correo: "<<tmp->usuario.correo<<endl;
    cout<<"Password: "<<tmp->usuario.password<<endl;
    cout<<"Creditos: "<<tmp->usuario.creditos<<endl;
    cout<<"Edad: "<<tmp->usuario.edad<<endl;
    cout<<"*************************"<<endl;*/
}
