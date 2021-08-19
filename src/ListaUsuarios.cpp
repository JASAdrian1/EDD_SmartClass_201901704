#include "ListaUsuarios.h"
#include<iostream>
#include<string>
#include<conio.h>
#include <fstream>


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

NodoUsuario* ListaUsuarios::buscarUsuario(string dpi){
     NodoUsuario *tmp = this->primero;
     while(tmp != this->ultimo->siguiente){
        if (tmp->usuario.dpi == dpi){
            return tmp;
        }
        tmp = tmp->siguiente;
     }
     return nullptr;

}


void ListaUsuarios::modificarUsuario(string dpi){
    string opcion = "";
    string nuevoDato="";
    NodoUsuario *usuario = new NodoUsuario();
    while(opcion!="9"){
        usuario = this->buscarUsuario(dpi);
        if (usuario!=nullptr){
            cout<<"1. Modificar ID"<<endl;
            cout<<"2. Modificar DPI"<<endl;
            cout<<"3. Modificar nombre"<<endl;
            cout<<"4. Modificar carrera"<<endl;
            cout<<"5. Modificar correo"<<endl;
            cout<<"6. Modificar password"<<endl;
            cout<<"7. Modificar creditos"<<endl;
            cout<<"8. Modificar edad"<<endl;
            cout<<"9. Salir"<<endl;
            cout<<"Ingrese la opcion que desea ejecutar: ";
            cin >> opcion;
            if (opcion == "1"){
                cout<<"Ingrese el nuevo ID: "<<endl; cin >> nuevoDato;
                usuario->usuario.id = nuevoDato;
                cout<<"Se ha modificado exitosamente el ID"<<endl;
                getch();
                this->imprimirUsuarios();
            }else if(opcion == "2"){
                cout<<"Ingrese el nuevo DPI: "<<endl; cin >> nuevoDato;
                usuario->usuario.dpi = nuevoDato;
                cout<<"Se ha modificado exitosamente el DPI"<<endl;
                getch();
                this->imprimirUsuarios();
            }else if(opcion == "3"){
                cout<<"Ingrese el nuevo nombre: "<<endl; cin >> nuevoDato;
                usuario->usuario.nombre = nuevoDato;
                cout<<"Se ha modificado exitosamente el nombre"<<endl;
                getch();
                this->imprimirUsuarios();
            }else if(opcion == "4"){
                cout<<"Ingrese la nueva carrera: "<<endl; cin >> nuevoDato;
                usuario->usuario.carrera = nuevoDato;
                cout<<"Se ha modificado exitosamente la carrera"<<endl;
                getch();
                this->imprimirUsuarios();
            }else if(opcion == "5"){
                cout<<"Ingrese el nuevo correo: "<<endl; cin >> nuevoDato;
                usuario->usuario.correo = nuevoDato;
                cout<<"Se ha modificado exitosamente el correo"<<endl;
                getch();
                this->imprimirUsuarios();
            }else if(opcion == "6"){
                cout<<"Ingrese el nuevo password: "<<endl; cin >> nuevoDato;
                usuario->usuario.password = nuevoDato;
                cout<<"Se ha modificado exitosamente el password"<<endl;
                getch();
                this->imprimirUsuarios();
            }else if(opcion == "7"){
                cout<<"Ingrese la nueva cantidad de creditos: "<<endl; cin >> nuevoDato;
                usuario->usuario.creditos = nuevoDato;
                cout<<"Se ha modificado exitosamente los creditos"<<endl;
                getch();
                this->imprimirUsuarios();
            }else if(opcion == "8"){
                cout<<"Ingrese la nueva edad: "<<endl; cin >> nuevoDato;
                usuario->usuario.edad = nuevoDato;
                cout<<"Se ha modificado exitosamente la edad"<<endl;
                getch();
                this->imprimirUsuarios();
            }
        }else{
            cout<<"No se ha encontrado el usuario"<<endl;
            getch();
        }
    }


}


void ListaUsuarios::eliminarUsuario(string dpi){
    NodoUsuario *usuario = new NodoUsuario();
    usuario = this->buscarUsuario(dpi);
    string confirmacion = "";
    if(usuario!=nullptr){
        while(confirmacion!="si" || confirmacion!="no"){
            cout<<"¿Esta seguro que desea eliminar al usuario con DPI: "<<usuario->usuario.dpi<<"? (si/no)"<<endl;
            cin >>confirmacion;
            if(confirmacion=="si"){
                if(usuario == this->primero){
                    this->primero = usuario->siguiente;
                }else if(usuario == this->ultimo){
                    this->ultimo = usuario->anterior;
                }
                else{
                    NodoUsuario * auxSiguiente = usuario->siguiente;
                    NodoUsuario * auxAnterior = usuario->anterior;
                    auxSiguiente->anterior =auxAnterior;
                    auxAnterior->siguiente = auxSiguiente;
                }
                cout<<"Se ha eliminado al usuario con DPI "<<usuario->usuario.dpi<<" exitosamente"<<endl;
                delete(usuario);

                getch();
                this->imprimirUsuarios();
                break;
            }else if(confirmacion == "no"){
                cout<<"No se ha eliminado al usuario"<<endl;
                getch();
                break;
            }else{
                cout<<"No ha ingresado una opcion valida."<<endl;
            }
        }
    }else{
        cout<<"No se ha encontrado al usuario ingresado";
    }
}


int contGraphError = 0;
void ListaUsuarios::graficarLista(){
    contGraphError+=1;
    if(!this->listaVacia()){
        ofstream fs("graficaListaEstudiantes"+to_string(contGraphError)+".dot");
        fs<<"digraph g {"<<endl;
        fs<<"rankdir=LR;"<<endl;
        fs<<"node[shape=circle];"<<endl;
        int contador = 0;
        NodoUsuario *tmp = this->primero;
        while(tmp->siguiente!=nullptr){
            string info = "ID:"+tmp->usuario.id+"\nDPI: "+tmp->usuario.dpi+
            "\nNombre: "+tmp->usuario.nombre+"\nCarrera: "+tmp->usuario.carrera+
            +"\nPassword: "+tmp->usuario.password+"\nCreditos: "+tmp->usuario.creditos+
            +"\nEdad: "+tmp->usuario.edad;
            fs<<contador<<"[label=\""<<info<<"\"];"<<endl;
            contador+=1;
            tmp = tmp->siguiente;
        }
        //Se crea el ultimo nodo de la grafica
        string info = "ID:"+tmp->usuario.id+"\nDPI: "+tmp->usuario.dpi+
            "\nNombre: "+tmp->usuario.nombre+"\nCarrera: "+tmp->usuario.carrera+
            +"\nPassword: "+tmp->usuario.password+"\nCreditos: "+tmp->usuario.creditos+
            +"\nEdad: "+tmp->usuario.edad;
        fs<<contador<<"[label=\""<<info<<"\"];"<<endl;

        fs<<0<<"->"<<contador<<endl;
        fs<<contador<<"->"<<0<<endl;
        for(int i=0;i<contador;i++){
            fs<<i<<"->"<<i+1<<endl;
        }
        fs<<"}"<<endl;
        cout<<"Se ha creado la grafica exitosamente"<<endl;
        getch();
    }else{
        cout<<"No se ha creado la grafica ya que la cola de errores se encuentra vacia"<<endl;
    }
}

