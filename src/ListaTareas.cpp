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


void ListaTareas::modificarTarea(int indice){
    string opcion = "";
    string nuevoDato="";
    NodoTarea *tarea = new NodoTarea();
    while(opcion!="8"){
        tarea = this->buscarTarea(indice);
        if (tarea!=nullptr){
            cout<<"1. Modificar Carnet"<<endl;
            cout<<"2. Modificar Nombre de la tarea"<<endl;
            cout<<"3. Modificar Descripcion"<<endl;
            cout<<"4. Modificar Materia"<<endl;
            cout<<"5. Modificar Fecha"<<endl;
            cout<<"6. Modificar Hora"<<endl;
            cout<<"7. Modificar Estado"<<endl;
            cout<<"8. Salir"<<endl;
            cout<<"Ingrese la opcion que desea ejecutar: ";
            cin >> opcion;
            if (opcion == "1"){
                cout<<"Ingrese el nuevo carnet: "<<endl; cin >> nuevoDato;
                tarea->tarea.carnet = nuevoDato;
                cout<<"Se ha modificado exitosamente el carnet"<<endl;
                getch();
                //this->imprimirUsuarios();
            }else if(opcion == "2"){
                cout<<"Ingrese el nuevo nombre de la tarea: "<<endl; cin >> nuevoDato;
                tarea->tarea.nombre = nuevoDato;
                cout<<"Se ha modificado exitosamente el nombre"<<endl;
                getch();
                //this->imprimirUsuarios();
            }else if(opcion == "3"){
                cout<<"Ingrese la nueva descripcion: "<<endl; cin >> nuevoDato;
                tarea->tarea.descripcion = nuevoDato;
                cout<<"Se ha modificado exitosamente la descripcion"<<endl;
                getch();
                //this->imprimirUsuarios();
            }else if(opcion == "4"){
                cout<<"Ingrese la nueva materia: "<<endl; cin >> nuevoDato;
                tarea->tarea.materia = nuevoDato;
                cout<<"Se ha modificado exitosamente la materia"<<endl;
                getch();
                //this->imprimirUsuarios();
            }else if(opcion == "5"){
                cout<<"Ingrese la nueva fecha: "<<endl; cin >> nuevoDato;
                tarea->tarea.fecha = nuevoDato;
                cout<<"Se ha modificado exitosamente la fecha"<<endl;
                getch();
                //this->imprimirUsuarios();
            }else if(opcion == "6"){
                cout<<"Ingrese la nueva hora: "<<endl; cin >> nuevoDato;
                tarea->tarea.hora = stoi(nuevoDato);
                cout<<"Se ha modificado exitosamente la hora"<<endl;
                getch();
                //this->imprimirUsuarios();
            }else if(opcion == "7"){
                    cout<<"Ingrese el nuevo estado: "<<endl; cin >> nuevoDato;
                    tarea->tarea.estado = nuevoDato;
                    cout<<"Se ha modificado exitosamente el estado"<<endl;
                    getch();
                    //this->imprimirUsuarios();
            }
        }else{
                cout<<"No se ha encontrado la tarea"<<endl;
                getch();
            }
    }
}


void ListaTareas::eliminarTarea(int indice){
    NodoTarea *tarea = new NodoTarea();
    tarea = this->buscarTarea(indice);
    string confirmacion = "";
    if(tarea!=nullptr){
        while(confirmacion!="si" || confirmacion!="no"){
            cout<<"¿Esta seguro que desea eliminar la tarea?(si/no)"<<endl;
            cin >>confirmacion;
            if(confirmacion=="si"){
                if(tarea == this->primero){
                    this->primero = tarea->siguiente;
                }else if(tarea == this->ultimo){
                    this->ultimo = tarea->anterior;
                }
                else{
                    NodoTarea * auxSiguiente = tarea->siguiente;
                    NodoTarea * auxAnterior = tarea->anterior;
                    auxSiguiente->anterior =auxAnterior;
                    auxAnterior->siguiente = auxSiguiente;
                }
                cout<<"Se ha eliminado la tarea exitosamente exitosamente"<<endl;
                delete(tarea);
                getch();
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

NodoTarea *ListaTareas::buscarTarea(int indice){
    if(!this->listaVacia()){
        NodoTarea *tmp = this->primero;
        int contador = 0;
        while(tmp != this->ultimo->siguiente){
            if(to_string(indice) == tmp->tarea.id && tmp->tarea.nombre != "-1"){
                return tmp;
            }
            tmp = tmp->siguiente;
            contador+=1;
        }
        cout<<"No se ha encontrado la tarea"<<endl;
        getch();
        return nullptr;
    }else{
        cout<<"La lista esta vacia, no se ha realizado la busqueda"<<endl;
        return nullptr;
    }
    getch();
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
