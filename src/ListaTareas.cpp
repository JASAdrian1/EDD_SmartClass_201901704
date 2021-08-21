#include "ListaTareas.h"
#include<iostream>
#include<string>
#include<conio.h>
#include <fstream>

ListaTareas::ListaTareas()
{
    //ctor
    this->primero = nullptr;
    this->ultimo = nullptr;
}

int ListaTareas::listaVacia(){
    //Valida si la lista contiene algun elemento
    return this->primero == nullptr;

}

void ListaTareas::insertar(Tarea *tarea){
    NodoTarea *nuevo =new NodoTarea(*tarea,nullptr,nullptr);
    if(this->listaVacia()){
        this->primero = nuevo;
        this->ultimo = nuevo;
        this->primero->anterior = this->ultimo;
        this->ultimo->siguiente = this->primero;
        //cout<<primero->usuario.nombre<<endl;
    }else{
        NodoTarea *tmp = this->ultimo;
        this->ultimo->siguiente = nuevo;
        this->ultimo = nuevo;
        this->ultimo->anterior = tmp;
        //cout<<ultimo->usuario.nombre<<endl;

    }
}

void ListaTareas::imprimirTareas(){
    NodoTarea *tmp = this->primero;
    while(tmp != this->ultimo->siguiente){
        cout<<"*************************"<<endl;
        cout<<"Id: "<<tmp->tarea.id<<endl;
        cout<<"Carnet: "<<tmp->tarea.carnet<<endl;
        cout<<"Nombre: "<<tmp->tarea.nombre<<endl;
        cout<<"Descripcion: "<<tmp->tarea.descripcion<<endl;
        cout<<"Materia: "<<tmp->tarea.materia<<endl;
        cout<<"Fecha: "<<tmp->tarea.fecha<<endl;
        cout<<"Estado: "<<tmp->tarea.estado<<endl;
        cout<<"Hora: "<<tmp->tarea.hora<<endl;
        cout<<"Dia: "<<tmp->tarea.dia<<endl;
        cout<<"Mes: "<<tmp->tarea.mes<<endl;
        cout<<"*************************"<<endl;
        tmp = tmp->siguiente;
    }
}

void ListaTareas::busquedaLinealizada(int posicion){
    if(!this->listaVacia()){
        NodoTarea *tmp = this->primero;
        int contador = 0;
        while(tmp != this->ultimo->siguiente){
            if(to_string(posicion) == tmp->tarea.id){
                cout<<"*************************"<<endl;
                cout<<"Id: "<<tmp->tarea.id<<endl;
                cout<<"Carnet: "<<tmp->tarea.carnet<<endl;
                cout<<"Nombre: "<<tmp->tarea.nombre<<endl;
                cout<<"Descripcion: "<<tmp->tarea.descripcion<<endl;
                cout<<"Materia: "<<tmp->tarea.materia<<endl;
                cout<<"Fecha: "<<tmp->tarea.fecha<<endl;
                cout<<"Estado: "<<tmp->tarea.estado<<endl;
                cout<<"Hora: "<<tmp->tarea.hora<<endl;
                cout<<"Dia: "<<tmp->tarea.dia<<endl;
                cout<<"Mes: "<<tmp->tarea.mes<<endl;
                cout<<"*************************"<<endl;
                getch();
                return ;
            }
            tmp = tmp->siguiente;
            contador+=1;
        }
        cout<<"No se ha encontrado la tarea"<<endl;
        getch();
        return;
    }else{
        cout<<"La lista esta vacia, no se ha realizado la busqueda";
    }
    getch();
}


int contGraphTareas = 0;
void ListaTareas::graficarLista(){
    contGraphTareas+=1;
    if(!this->listaVacia()){
        ofstream fs("graficaListaTareas"+to_string(contGraphTareas)+".dot");
        fs<<"digraph g {"<<endl;
        fs<<"rankdir=LR;"<<endl;
        fs<<"node[shape=circle];"<<endl;
        int contador = 0;
        NodoTarea *tmp = this->primero;
        while(tmp->siguiente!=nullptr){
            string info = "ID:"+tmp->tarea.id+"\\nCarnet: "+tmp->tarea.carnet+
            "\\nNombre: "+tmp->tarea.nombre+"\\nDescripcion: "+tmp->tarea.descripcion+
            +"\\nMateria: "+tmp->tarea.materia+"\\nFecha: "+tmp->tarea.fecha+
            +"\\nHora: "+to_string(tmp->tarea.hora)+"\\nEstado: "+tmp->tarea.estado;
            fs<<contador<<"[label=\""<<info<<"\"];"<<endl;
            contador+=1;
            tmp = tmp->siguiente;
        }
        //Se crea el ultimo nodo de la grafica
        string info = "ID:"+tmp->tarea.id+"\\nCarnet: "+tmp->tarea.carnet+
            "\\nNombre: "+tmp->tarea.nombre+"\\nDescripcion: "+tmp->tarea.descripcion+
            +"\\nMateria: "+tmp->tarea.materia+"\\nFecha: "+tmp->tarea.fecha+
            +"\\nHora: "+to_string(tmp->tarea.hora)+"\\nEstado: "+tmp->tarea.estado;
            fs<<contador<<"[label=\""<<info<<"\"];"<<endl;
            contador+=1;
        fs<<contador<<"[label=\""<<info<<"\"];"<<endl;


        for(int i=0;i<contador;i++){
            fs<<i<<"->"<<i+1<<endl;
        }
        fs<<"}"<<endl;
        fs.close();
        string nombreGraficaTareas = "graficaListaTareas"+to_string(contGraphTareas);
        system(("dot -Tsvg "+nombreGraficaTareas+".dot -o "+nombreGraficaTareas+".svg").c_str() );
        system((nombreGraficaTareas+".svg").c_str() );
        cout<<"Se ha creado la grafica exitosamente"<<endl;
        getch();
    }else{
        cout<<"No se ha creado la grafica ya que la lista de estudiantes esta vacia"<<endl;
    }
}


string ListaTareas::generarCodigoSalida(){
    string codigo = "";
    NodoTarea *tmp = this->primero;
    while(tmp != this->ultimo->siguiente){
        if(tmp->tarea.nombre != "-1"){
            codigo+="\t¿element type=\"task\"$?\n";
            codigo+="\t\t¿item Carnet: "+tmp->tarea.carnet+"$?\n";
            codigo+="\t\t¿item Nombre: "+tmp->tarea.nombre+"$?\n";
            codigo+="\t\t¿item Descripcion: "+tmp->tarea.descripcion+"$?\n";
            codigo+="\t\t¿item Materia: "+tmp->tarea.materia+"$?\n";
            codigo+="\t\t¿item Fecha: "+tmp->tarea.fecha+"$?\n";
            codigo+="\t\t¿item Hora: "+to_string(tmp->tarea.hora)+"$?\n";
            codigo+="\t\t¿item Estado: "+tmp->tarea.estado+"$?\n";
            codigo+="\t¿$element\"\n";
        }
        tmp = tmp->siguiente;
    }
    return codigo;
}




ListaTareas::~ListaTareas()
{
    //dtor
}
